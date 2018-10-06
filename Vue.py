from tkinter import *
import os,os.path
import random

class Vue():
    def __init__(self,parent,ip,nom):
        self.parent=parent
        self.root=Tk()

        self.root.attributes('-fullscreen', 1) #Pour full screen
        self.root.configure(bg='#1c4873') # Background de ma page
        
        self.cadreactif=None
        self.maselection=None
        self.root.title(os.path.basename(sys.argv[0]))
        self.modele=None
        self.nom=""
        self.cadreapp=Frame(self.root,width=800,height=600)         #Frame de base a mes fenetre
        self.cadreapp.pack()
        self.creercadresplash(ip,nom)
        self.creercadrelobby()
        self.changecadre(self.cadresplash)
        
        self.button = Button(self.root, text="Quit", command=self.root.destroy)
        self.button.pack()        
    def fermerfenetre(self):
        self.parent.fermefenetre()
        
    def changecadre(self,cadre):
        if self.cadreactif:
            self.cadreactif.pack_forget()
        self.cadreactif=cadre
        self.cadreactif.pack()
            
    def creercadresplash(self,ip,nom):
        self.cadresplash=Frame(self.cadreapp,bg='#15243d')
        self.titre = Label(self.cadresplash, text = "Bienvenue dans la galaxie orion voyageur!",bg='#15243d',font='arial 20',foreground="white")
        self.titre.pack(pady=20,padx=100);
        
        soustitre=Label(self.cadresplash, text = "Pour des fin de securite veuillez vous identifier",bg='#15243d',font='arial 16',foreground="white")
        soustitre.pack(pady=10,padx=10);
        
        self.nomsplash=Entry(self.cadresplash,bg='#A3C5D8',relief=FLAT,foreground="white",font='arial 14',highlightthickness=2,highlightcolor='#849fae')
        self.nomsplash.insert(0, nom)
        self.nomsplash.pack(pady=10)
        
        self.ipsplash=Entry(self.cadresplash,bg='#A3C5D8',relief=FLAT,foreground="white",font='arial 14',highlightthickness=2,highlightcolor='#849fae')
        self.ipsplash.insert(0, ip)
        self.ipsplash.pack(pady=20)
        
        
        btncreerpartie=Button(self.cadresplash,text="Creer partie",bg='#A3C5D8',command=self.creerpartie)
        btncreerpartie.pack()
        btnconnecterpartie=Button(self.cadresplash,text="Connecter partie",bg='#A3C5D8',command=self.connecterpartie)
        btnconnecterpartie.pack()
        
            
    def creercadrelobby(self):
        self.cadrelobby=Frame(self.cadreapp)
        self.canevaslobby=Canvas(self.cadrelobby,width=640,height=480,bg="lightblue")
        self.canevaslobby.pack()
        self.listelobby=Listbox(bg="yellow",borderwidth=0,relief=FLAT)
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
        
        self.cadreinfo=Frame(self.cadrepartie,width=150,height=100,bg="#455571",relief=RAISED)
        self.cadreinfo.pack(side=LEFT,fill=Y)
        
        self.cadreinfogen=Frame(self.cadreinfo,width=130,height=200,bg="#FFFFFF",relief=RAISED)
        self.cadreinfogen.pack()
        
        self.labid=Label(self.cadreinfogen,text="MINI\nORION",fg="#fbbfda",bg="#455571",font=("Helvetica",20),pady=10)
        self.labid.bind("<Button>",self.afficherplanemetemere)
        self.labid.pack()
        
        self.cadreinfobtm=Frame(self.cadreapp,width=704, height=120, bg="#455571")
        self.cadreinfobtm.pack(side=BOTTOM,fill=Y)
        
        
        self.cadreinfochoix=Frame(self.cadreinfo,height=200,width=200,bg="#455571")
        self.cadreinfochoix.pack()
        self.btncreervaisseau=Button(self.cadreinfo,text="Vaisseau",command=self.creervaisseau)
        #self.btncreervaisseauguerre=Button(self.cadreinfo,text="Vaisseau Guerre",command=self.creervaisseau)
        self.lbselectecible=Label(self.cadreinfo,text="Choisir cible",bg="#455571",fg="red")
        
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
        