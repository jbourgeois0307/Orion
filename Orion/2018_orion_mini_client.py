# -*- coding: utf-8 -*-
from tkinter import *
import os,os.path
import sys
import xmlrpc.client
import socket
import random
from subprocess import Popen 
from helper import Helper as hlp

class Id():
    id=0
    def prochainid():
        Id.id+=1
        return Id.id

class Vue():
    def __init__(self,parent,ip,nom):
        self.parent=parent
        self.root=Tk()
        self.largeur=640
        self.hauteur=480
        self.root.protocol("WM_DELETE_WINDOW", self.fermerfenetre)
        self.terrain=[]
        self.cadreactif=None
        self.maselection=None
        self.root.title(os.path.basename(sys.argv[0]))
        self.modele=None
        self.nom=""
        self.cadreapp=Frame(self.root,width=800,height=600)
        self.cadreapp.pack()
        self.creercadresplash(ip,nom)
        self.creercadrelobby()
        self.changecadre(self.cadresplash)
        
    def fermerfenetre(self):
        self.parent.fermefenetre()
        
    def changecadre(self,cadre):
        if self.cadreactif:
            self.cadreactif.pack_forget()
        self.cadreactif=cadre
        self.cadreactif.pack()
            
    def creercadresplash(self,ip,nom):
        self.cadresplash=Frame(self.cadreapp)
        self.canevassplash=Canvas(self.cadresplash,width=640,height=480,bg="red")
        self.canevassplash.pack()
        self.nomsplash=Entry(bg="pink")
        self.nomsplash.insert(0, nom)
        self.ipsplash=Entry(bg="pink")
        self.ipsplash.insert(0, ip)
        labip=Label(text=ip,bg="red",borderwidth=0,relief=RIDGE)
        btncreerpartie=Button(text="Creer partie",bg="pink",command=self.creerpartie)
        btnconnecterpartie=Button(text="Connecter partie",bg="pink",command=self.connecterpartie)
        self.canevassplash.create_window(200,200,window=self.nomsplash,width=100,height=30)
        self.canevassplash.create_window(200,250,window=self.ipsplash,width=100,height=30)
        self.canevassplash.create_window(200,300,window=labip,width=100,height=30)
        self.canevassplash.create_window(200,350,window=btncreerpartie,width=100,height=30)
        self.canevassplash.create_window(200,400,window=btnconnecterpartie,width=100,height=30) 
            
    def creercadrelobby(self):
        self.cadrelobby=Frame(self.cadreapp)
        self.canevaslobby=Canvas(self.cadrelobby,width=640,height=480,bg="lightblue")
        self.canevaslobby.pack()
        self.listelobby=Listbox(bg="red",borderwidth=0,relief=FLAT)
        self.nbetoile=Entry(bg="pink")
        self.nbetoile.insert(0, 100)
        self.largeespace=Entry(bg="pink")
        self.largeespace.insert(0, 1000)
        self.hautespace=Entry(bg="pink")
        self.hautespace.insert(0, 800)
        btnlancerpartie=Button(text="Lancer partie",bg="pink",command=self.lancerpartie)
        self.canevaslobby.create_window(440,240,window=self.listelobby,width=200,height=400)
        self.canevaslobby.create_window(200,200,window=self.largeespace,width=100,height=30)
        self.canevaslobby.create_window(200,250,window=self.hautespace,width=100,height=30)
        self.canevaslobby.create_window(200,300,window=self.nbetoile,width=100,height=30)
        self.canevaslobby.create_window(200,400,window=btnlancerpartie,width=100,height=30)
        
    def connecterpartie(self):
        nom=self.nomsplash.get()
        ip=self.ipsplash.get()
        if nom and ip:
            self.parent.inscrirejoueur()
            self.changecadre(self.cadrelobby)
            print("BOUCLEATTENTE de CONNECTER")
            self.parent.boucleattente()
        
    def creerpartie(self):
        nom=self.nomsplash.get()
        ip=self.ipsplash.get()
        if nom and ip:
            self.parent.creerpartie()
            self.parent.inscrirejoueur()
            self.changecadre(self.cadrelobby)
            print("BOUCLEATTENTE de CREER")
            self.parent.boucleattente()
        
    def lancerpartie(self):
        self.parent.lancerpartie()
        
    def affichelisteparticipants(self,lj):
        self.listelobby.delete(0,END)
        self.listelobby.insert(0,lj)
        
    def creeraffichercadrepartie(self,mod):
        self.nom=self.parent.monnom
        self.mod=mod
        self.cadrepartie=Frame(self.cadreapp)
        self.cadrejeu=Frame(self.cadrepartie)
        self.canevas=Canvas(self.cadrepartie,width=mod.largeur,height=mod.hauteur,bg="grey11")
        self.canevas.pack(side=LEFT)
        self.canevas.bind("<Button>",self.cliquecosmos)
        self.cadreinfo=Frame(self.cadrepartie,width=200,height=200,bg="darkgrey")
        self.cadreinfo.pack(side=LEFT,fill=Y)
        self.cadreinfogen=Frame(self.cadreinfo,width=200,height=200,bg="grey50")
        self.cadreinfogen.pack()
        self.labid=Label(self.cadreinfogen,text=self.nom,fg=mod.joueurs[self.nom].couleur)
        self.labid.bind("<Button>",self.afficherplanemetemere)
        self.labid.pack()
        self.cadreinfochoix=Frame(self.cadreinfo,height=200,width=200,bg="grey30")
        self.cadreinfochoix.pack()
        self.btncreervaisseau=Button(self.cadreinfo,text="Vaisseau",command=self.creervaisseau)
        self.lbselectecible=Label(self.cadreinfo,text="Choisir cible",bg="darkgrey")
        
        self.afficherdecor(mod)
        
        self.changecadre(self.cadrepartie)
        
    def afficherdecor(self,mod):
        
        for i in range(len(mod.planetes)*3):
            x=random.randrange(mod.largeur)
            y=random.randrange(mod.hauteur)
            self.canevas.create_oval(x,y,x+1,y+1,fill="white",tags=("fond",))
        
        for i in mod.planetes:
            t=i.taille
            self.canevas.create_oval(i.x-t,i.y-t,i.x+t,i.y+t,fill="grey80",
                                     tags=(i.proprietaire,"planete",str(i.id)))
        for i in mod.joueurs.keys():
            for j in mod.joueurs[i].planetescontrolees:
                t=j.taille
                self.canevas.create_oval(j.x-t,j.y-t,j.x+t,j.y+t,fill=mod.joueurs[i].couleur,
                                     tags=(j.proprietaire,"planete",str(j.id),"possession"))
                
        self.afficherpartie(mod)
                
    def afficherplanemetemere(self,evt):
        j=self.mod.joueurs[self.nom]
        couleur=j.couleur
        x=j.planetemere.x
        y=j.planetemere.y
        t=10
        self.canevas.create_oval(x-t,y-t,x+t,y+t,dash=(3,3),width=2,outline=couleur,
                                 tags=("planetemere","marqueur"))
    def creervaisseau(self):
        print("Creer vaisseau")
        self.parent.creervaisseau()
        self.maselection=None
        self.canevas.delete("marqueur")
        self.btncreervaisseau.pack_forget()
        
    def afficherpartie(self,mod):
        self.canevas.delete("artefact")
        
        if self.maselection!=None:
            joueur=mod.joueurs[self.maselection[0]]
            if self.maselection[1]=="planete":
                for i in joueur.planetescontrolees:
                    if i.id == int(self.maselection[2]):
                        x=i.x
                        y=i.y
                        t=10
                        self.canevas.create_oval(x-t,y-t,x+t,y+t,dash=(2,2),outline=mod.joueurs[self.nom].couleur,
                                                 tags=("select","marqueur"))
            elif self.maselection[1]=="flotte":
                for i in joueur.flotte:
                    if i.id == int(self.maselection[2]):
                        x=i.x
                        y=i.y
                        t=10
                        self.canevas.create_rectangle(x-t,y-t,x+t,y+t,dash=(2,2),outline=mod.joueurs[self.nom].couleur,
                                                 tags=("select","marqueur"))
        #else:
        #    self.canevas.delete("marqueur")
            
        
        for i in mod.joueurs.keys():
            i=mod.joueurs[i]
            for j in i.flotte:
                self.canevas.create_rectangle(j.x-3,j.y-3,j.x+3,j.y+3,fill=i.couleur,
                                     tags=(j.proprietaire,"flotte",str(j.id),"artefact"))

    def cliquecosmos(self,evt):
        self.btncreervaisseau.pack_forget()
        t=self.canevas.gettags(CURRENT)
        if t and t[0]==self.nom:
            #self.maselection=self.canevas.find_withtag(CURRENT)#[0]
            self.maselection=[self.nom,t[1],t[2]]  #self.canevas.find_withtag(CURRENT)#[0]
            print(self.maselection)
            if t[1] == "planete":
                self.montreplaneteselection()
            elif t[1] == "flotte":
                self.montreflotteselection()
        elif "planete" in t and t[0]!=self.nom:
            if self.maselection:
                pass # attribuer cette planete a la cible de la flotte selectionne
                self.parent.ciblerflotte(self.maselection[2],t[2])
            print("Cette planete ne vous appartient pas - elle est a ",t[0])
            self.maselection=None
            self.lbselectecible.pack_forget()
            self.canevas.delete("marqueur")
        else:
            print("Region inconnue")
            self.maselection=None
            self.lbselectecible.pack_forget()
            self.canevas.delete("marqueur")
            
    def montreplaneteselection(self):
        self.btncreervaisseau.pack()
    def montreflotteselection(self):
        self.lbselectecible.pack()
    
    def afficherartefacts(self,joueurs):
        pass #print("ARTEFACTS de ",self.nom)
        
class Planete():
    def __init__(self,x,y):
        self.id=Id.prochainid()
        self.proprietaire="inconnu"
        self.x=x
        self.y=y
        self.taille=random.randrange(4,6)
        
class Vaisseau():
    def __init__(self,nom,x,y):
        self.id=Id.prochainid()
        self.proprietaire=nom
        self.x=x
        self.y=y
        self.cargo=0
        self.energie=100
        self.vitesse=2
        self.cible=None 
        
    def avancer(self):
        if self.cible:
            x=self.cible.x
            y=self.cible.y
            ang=hlp.calcAngle(self.x,self.y,x,y)
            x1,y1=hlp.getAngledPoint(ang,self.vitesse,self.x,self.y)
            self.x,self.y=x1,y1 #int(x1),int(y1)
            if hlp.calcDistance(self.x,self.y,x,y) <=self.vitesse:
                self.cible=None
                #print("Change cible")
        else:
            print("PAS DE CIBLE")
    
    def avancer1(self):
        if self.cible:
            x=self.cible.x
            if self.x>x:
                self.x-=self.vitesse
            elif self.x<x:
                self.x+=self.vitesse
            
            y=self.cible.y
            if self.y>y:
                self.y-=self.vitesse
            elif self.y<y:
                self.y+=self.vitesse
            if abs(self.x-x)<(2*self.cible.taille) and abs(self.y-y)<(2*self.cible.taille):
                self.cible=None
              
class Joueur():
    def __init__(self,parent,nom,planetemere,couleur):
        self.id=Id.prochainid()
        self.parent=parent
        self.nom=nom
        self.planetemere=planetemere
        self.planetemere.proprietaire=self.nom
        self.couleur=couleur
        self.planetescontrolees=[planetemere]
        self.flotte=[]
        self.actions={"creervaisseau":self.creervaisseau,
                      "ciblerflotte":self.ciblerflotte}
        
    def creervaisseau(self,planete):
        v=Vaisseau(self.nom,self.planetemere.x+10,self.planetemere.y)
        print("Vaisseau",v.id)
        self.flotte.append(v)
        
    def ciblerflotte(self,ids):
        idori,iddesti=ids
        for i in self.flotte:
            if i.id== int(idori):
                for j in self.parent.planetes:
                    if j.id== int(iddesti):
                        i.cible=j
                        print("GOT TARGET")
                        return
        
        
    def prochaineaction(self):
        for i in self.flotte:
            if i.cible:
                i.avancer()
            else:
                i.cible=random.choice(self.parent.planetes)
            
    def prochaineaction2(self):
        for i in self.flotte:
            i.avancer()
    
class Modele():
    def __init__(self,parent,joueurs):
        self.parent=parent
        self.largeur=500 #self.parent.vue.root.winfo_screenwidth()
        self.hauteur=400 #self.parent.vue.root.winfo_screenheight()
        self.joueurs={}
        self.actionsafaire={}
        self.planetes=[]
        self.terrain=[]
        self.creerplanetes(joueurs)
        self.creerterrain()
        
    def creerterrain(self):
        self.terrain=[]
        for i in range(10):
            ligne=[]
            for j in range(10):
                n=random.randrange(5)
                if n==0:
                    ligne.append(1)
                else:
                    ligne.append(0)
            self.terrain.append(ligne)
        
    def creerplanetes(self,joueurs):
        bordure=10
        for i in range(100):
            x=random.randrange(self.largeur-(2*bordure))+bordure
            y=random.randrange(self.hauteur-(2*bordure))+bordure
            self.planetes.append(Planete(x,y))
        np=len(joueurs)
        planes=[]
        while np:
            p=random.choice(self.planetes)
            if p not in planes:
                planes.append(p)
                self.planetes.remove(p)
                np-=1
        couleurs=["red","blue","lightgreen","yellow",
                  "lightblue","pink","gold","purple"]
        for i in joueurs:
            self.joueurs[i]=Joueur(self,i,planes.pop(0),couleurs.pop(0))
            
    def prochaineaction(self,cadre):
        if cadre in self.actionsafaire:
            for i in self.actionsafaire[cadre]:
                #print(i)
                self.joueurs[i[0]].actions[i[1]](i[2])
                """
                print("4- le modele distribue les actions au divers participants")
                print("4...- en executant l'action qui est identifie par i[1] le dico")
                print("4...- qui est dans l'attribut actions",i[0],i[1],i[2])
                print("NOTE: ici on applique immediatement cette action car elle consiste soit")
                print("NOTE... a changer la vitesse (accelere/arrete) soit l'angle de l'auto")
                print("NOTE... dans ce cas-ci faire la prochaine action (le prochain for en bas)")
                print("NOTE... c'est seulement changer la position de l'auto si sa vitesse est non-nul")
                """
            del self.actionsafaire[cadre]
                
        for i in self.joueurs:
            self.joueurs[i].prochaineaction()
            
                
class Controleur():
    def __init__(self):

        print("IN CONTROLEUR")
        self.attente=0
        self.cadre=0 # le no de cadre pour assurer la syncronisation avec les autres participants
        self.tempo=0 # insert a reconnaitre qu'on a lance le serveur et qu'on peut s'inscrire automatiquement sans cliquer sur inscription dans l'interface
                     # ne peut pas etre remplace par egoserveur car si cette variable test a vrai (1), l'inscription est effectuee et tempo remis a 0 pour ne pas reinscrire deux fois...
                     # NOTE le nom de variable est ici epouvantable, j'en conviens - devrait quelquechose comme 'autoInscription'
        self.egoserveur=0 # est-ce que je suis celui qui a demarre le serveur, a priori, non (0)
        self.actions=[]    # la liste de mes actions a envoyer au serveur pour qu'il les redistribue a tous les participants
        self.statut=0 # etat dans le quel je me trouve : 0 -> rien, 1 -> inscrit, 2 -> demarre, 3-> joue
        self.monip=self.trouverIP() # la fonction pour retourner mon ip
        self.monnom=self.generernom() # un generateur de nom pour faciliter le deboggage (comme il genere un nom quasi aleatoire et on peut demarrer plusieurs 'participants' sur une même machine pour tester)
        self.modele=None
        self.serveur=None
        self.vue=Vue(self,self.monip,self.monnom)
        self.vue.root.mainloop()
        
    def trouverIP(self): # fonction pour trouver le IP en 'pignant' gmail
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # on cree un socket
        s.connect(("gmail.com",80))    # on envoie le ping
        monip=s.getsockname()[0] # on analyse la reponse qui contient l'IP en position 0 
        s.close() # ferme le socket
        return monip
    
    def generernom(self):  # generateur de nouveau nom - accelere l'entree de nom pour les tests - parfois � peut generer le meme nom mais c'est rare
        monnom="jmd_"+str(random.randrange(1000))
        return monnom

    def creerpartie(self):
        if self.egoserveur==0:
            pid = Popen(["C:\\Python 36\\Python.exe", "./2018_orion_mini_serveur.py"],shell=1).pid # on lance l'application serveur
            self.egoserveur=1 # on note que c'est soi qui, ayant demarre le serveur, aura le privilege de lancer la simulation
            self.tempo=1 # on change d'etat pour s'inscrire automatiquement 
                         # (parce que dans ce type de programme on prend pour acquis que celui qui prepare la simulation veut aussi y participer)

    # NOTE si on demarre le serveur, cette fonction est appellee pour nous (voir timer et variable tempo)
    #      ou par un clique sur le bouton 'Creerunclient' du layout
    def inscrirejoueur(self):
        ipserveur=self.vue.ipsplash.get() # lire le IP dans le champ du layout
        nom=self.vue.nomsplash.get() # noter notre nom
        if ipserveur and nom:
            ad="http://"+ipserveur+":9999"
            self.serveur=xmlrpc.client.ServerProxy(ad)
            self.monnom=nom
            rep=self.serveur.inscrireclient(self.monnom)    # on averti le serveur de nous inscrire
            #tester retour pour erreur de nom
            self.statut=1 # statut 1 == attente de lancement de partie
            random.seed(rep[2])
            
    ## ----------- FONCTION POUR CELUI QUI A CREE LA PARTIE SEULEMENT
    def lancerpartie(self): # reponse du bouton de lancement de simulation (pour celui qui a parti le serveur seulement)
        rep=self.serveur.lancerpartie() 
        print("REP DU LANCER",rep)
        if rep==1:
            self.statut=3 # il change son statut pour lui permettre d'initer la simulation, les autres sont en 1 (attente) - voir timer.py
    ## ----------- FIN --
    
    def initierpartie(self,rep):  # initalisation locale de la simulation, creation du modele, generation des assets et suppression du layout de lobby
        if rep[1][0][0]=="lancerpartie":
            self.modele=Modele(self,rep[1][0][1]) # on cree le modele
            self.vue.creeraffichercadrepartie(self.modele)
            print(self.monnom,"LANCE PROCHAINTOUR")
            self.prochaintour()

    def boucleattente(self):
        print("IN BOUCLEATTENTE")
        rep=self.serveur.faireaction([self.monnom,0,0])
        print("RETOUR DU faire action  SERVEUR",rep)
        if rep[0]:
            print("Recu ORDRE de DEMARRER")
            # PATCH pour dico in xmlrpc qui requiert des chaines comme cles
            # On a recu un cle str qu'on retransforme en int (pour compter les cadres de jeu, servant a distribuer les taches)
            cle=list(rep[2].keys())[0]
            rep[2]={int(cle):rep[2][cle]}  # on transforme la cle de str à int avant le transfert - voir aussi prochaintour (plus bas)
            # fin de patch
            self.initierpartie(rep[2])
        elif rep[0]==0:
            self.vue.affichelisteparticipants(rep[2])
            self.vue.root.after(1000,self.boucleattente)
        
    def prochaintour(self): # la boucle de jeu principale, qui sera appelle par la fonction bouclejeu du timer
        if self.serveur: # s'il existe un serveur
            self.cadre=self.cadre+1 # increment du compteur de cadre
            if self.attente==0:
                self.modele.prochaineaction(self.cadre)    # mise a jour du modele
                self.vue.afficherpartie(self.modele) # mise a jour de la vue
            if self.actions: # si on a des actions a partager 
                rep=self.serveur.faireaction([self.monnom,self.cadre,self.actions]) # on les envoie 
            else:
                rep=self.serveur.faireaction([self.monnom,self.cadre,0]) # sinon on envoie rien au serveur on ne fait que le pigner 
                                                                        # (HTTP requiert une requete du client pour envoyer une reponse)
            self.actions=[] # on s'assure que les actions a`envoyer sont maintenant supprimer (on ne veut pas les envoyer 2 fois)
            if rep[0]: # si le premier element de reponse n'est pas vide
                
                # PATCH de dico in xmlrpc (vs Pyro utilise avant)
                cle=list(rep[2].keys())[0]
                #print("AVANT",rep[2])
                rep[2]={int(cle):rep[2][cle]}
                #print("APRES",rep[2])
                # FIN DE PATCH
                
                for i in rep[2]:   # pour chaque action a faire (rep[2] est dictionnaire d'actions en provenance des participants
                                   # dont les cles sont les cadres durant lesquels ses actions devront etre effectuees
                    if i not in self.modele.actionsafaire.keys(): # si la cle i n'existe pas
                        self.modele.actionsafaire[i]=[] #faire une entree dans le dictonnaire
                    for k in rep[2][i]: # pour toutes les actions lies a une cle du dictionnaire d'actions recu
                        self.modele.actionsafaire[i].append(k) # ajouter cet action au dictionnaire sous l'entree dont la cle correspond a i
            if rep[1]=="attend": # si jamais rep[0] est vide MAIS que rep[1] == 'attend', on veut alors patienter
                self.cadre=self.cadre-1  # donc on revient au cadre initial
                self.attente=1
                #print("ALERTE EN ATTENTE",self.monnom)
            else:
                self.attente=0
            self.vue.root.after(20,self.prochaintour)
        else:
            print("Aucun serveur connu")
            
    def fermefenetre(self):
        if self.serveur:
            self.serveur.jequitte(self.monnom)
        self.vue.root.destroy()
            
    def creervaisseau(self):
        self.actions.append([self.monnom,"creervaisseau",""])
        
    def ciblerflotte(self,idorigine,iddestination):
        self.actions.append([self.monnom,"ciblerflotte",[idorigine,iddestination]])
        
if __name__=="__main__":
    c=Controleur()
    print("End Orion_mini")