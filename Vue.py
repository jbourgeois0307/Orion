from tkinter import *
import os,os.path
import random
from threading import Thread
from Vaisseau import *

class Vue():
    def __init__(self,parent,ip):
        self.parent=parent
        self.root=Tk()

        #self.root.attributes('-fullscreen', 1) #Pour full screen
        self.root.configure(bg='#1c4873') # Background de ma page
        
        self.button = Button(self.root, text="X", command=self.root.destroy, font='arial 20', relief=FLAT,bg='#1c4873',foreground="white")
        self.button.pack(side=TOP, anchor=E)   
        
        self.cadreactif=None
        self.maselection=None
        self.root.title(os.path.basename(sys.argv[0]))
        self.modele=None
        self.nom=""
        self.cadreapp=Frame(self.root,width=800,height=600)            #Frame de base a mes fenetre
        self.cadreapp.pack(fill="none", expand=True) # Pour centrer la fenetre
        self.creercadresplash(ip)
        self.creercadrelobby_Createur()
        self.creercadrelobby_Connecteur()
        self.changecadre(self.cadresplash)
        self.vbar = None
        self.hbar = None
        
    def fermerfenetre(self):
        self.parent.fermefenetre()
        
    def changecadre(self,cadre):
        if self.cadreactif:
            self.cadreactif.pack_forget()
        self.cadreactif=cadre
        self.cadreactif.pack()
            
    def creercadresplash(self,ip):
        self.cadresplash=Frame(self.cadreapp,bg='#15243d')
    
        self.titre = Label(self.cadresplash, text = "Bienvenue dans la galaxie orion voyageur!",bg='#15243d',font='arial 20',foreground="white")
        self.titre.pack(pady=(100,20),padx=100);
        
        soustitre=Label(self.cadresplash, text = "Pour des fin de securite veuillez vous identifier",bg='#15243d',font='arial 16',foreground="white")
        soustitre.pack(pady=10,padx=10);
        
        self.nomsplash=Entry(self.cadresplash,bg='#A3C5D8',relief=FLAT,foreground="white",font='arial 14',highlightthickness=2,highlightcolor='#849fae')
        self.nomsplash.insert(0, "Entrez votre nom")
        self.nomsplash.pack(pady=10)
        
        self.ipsplash=Entry(self.cadresplash,bg='#A3C5D8',relief=FLAT,foreground="white",font='arial 14',highlightthickness=2,highlightcolor='#849fae')
        self.ipsplash.insert(0, ip)
        self.ipsplash.pack(pady=20)
        
        
        btncreerpartie=Button(self.cadresplash,text="Creer partie",bg='#A3C5D8',command=self.creerpartie,relief=FLAT,font='arial 12')
        btncreerpartie.pack(fill="both", expand=True,side=LEFT, padx=(75,5),pady=(0,50))
        btnconnecterpartie=Button(self.cadresplash,text="Connecter partie",bg='#A3C5D8',command=self.connecterpartie,relief=FLAT,font='arial 12')
        btnconnecterpartie.pack(fill="both", expand=True,side=LEFT,padx=(5,75),pady=(0,50))
        

            
    def creercadrelobby_Createur(self):
        #print(self.parent.inscrirejoueur().monnom)
        self.cadrelobby_Createur=Frame(self.cadreapp,bg='#15243d')
        
        self.titre=Label(self.cadrelobby_Createur,text="Rebonjour Voyageur",bg='#15243d',font='arial 20',foreground="white")
        self.titre.pack(pady=(50,0))
             
        
        self.listelobby_CR=Listbox(self.cadrelobby_Createur,bg='#A3C5D8',borderwidth=0,relief=FLAT,width=60,height=20)
        self.listelobby_CR.pack(side=LEFT,pady=50,padx=(75,10));
        
                
        self.cadreCouleur= Frame(self.cadrelobby_Createur,bg='#A3C5D8')
        self.cadreCouleur.pack()
        
        self.Sous_titre2=Label(self.cadreCouleur,text="Choisiez votre couleur",width=30,bg='#A3C5D8',font='arial 14')
        self.Sous_titre2.pack()
        #choixCouleur = [('#009ee3'),('#e5007d'),('#951b81'),('#95c11e'),('#f39200') ] #Couleur a choisir
        #couleurSelection =[('#80cef1'),('#e680b2'),('#c88fbf'),('#c9dc91'),('#f8c77e') ]    #Liste des couleur pour affichage selection
        
        self.varCouleur=StringVar()
        self.varCouleur.set="red"
        
        #v = IntVar()
        
        Bcouleur1=Radiobutton( self.cadreCouleur, bg='#009ee3',selectcolor='#80cef1', value='#009ee3',fg="white",indicatoron=0,offrelief=FLAT,width=3,variable=self.varCouleur,command=self.definircouleur1 )
        Bcouleur1.pack(anchor=W,pady=5,padx=5,fill="both", expand=True,side=LEFT)
        
        Bcouleur2=Radiobutton( self.cadreCouleur, bg='#e5007d',selectcolor='#e680b2', value='#e5007d',fg="white",indicatoron=0,offrelief=FLAT,width=3,variable=self.varCouleur,command=self.definircouleur2 )
        Bcouleur2.pack(anchor=W,pady=5,padx=5,fill="both", expand=True,side=LEFT)
        
        Bcouleur3=Radiobutton( self.cadreCouleur, bg='#951b81',selectcolor='#c88fbf', value='#951b81',fg="white",indicatoron=0,offrelief=FLAT,width=3,variable=self.varCouleur,command=self.definircouleur3 )
        Bcouleur3.pack(anchor=W,pady=5,padx=5,fill="both", expand=True,side=LEFT)
        
        Bcouleur4=Radiobutton( self.cadreCouleur, bg='#95c11e',selectcolor='#c9dc91', value='#95c11e',fg="white",indicatoron=0,offrelief=FLAT,width=3,variable=self.varCouleur,command=self.definircouleur4 )
        Bcouleur4.pack(anchor=W,pady=5,padx=5,fill="both", expand=True,side=LEFT)
        
        Bcouleur5=Radiobutton( self.cadreCouleur, bg='#f39200',selectcolor='#f8c77e', value='#f39200',fg="white",indicatoron=0,offrelief=FLAT,width=3,variable=self.varCouleur,command=self.definircouleur5 )
        Bcouleur5.pack(anchor=W,pady=5,padx=5,fill="both", expand=True,side=LEFT)
        
        Bcouleur6=Radiobutton( self.cadreCouleur, bg='#009ee3',selectcolor='#80cef1', value='#009ee3',fg="white",indicatoron=0,offrelief=FLAT,width=3,variable=self.varCouleur,command=self.definircouleur1 )
        Bcouleur6.pack(anchor=W,pady=5,padx=5,fill="both", expand=True,side=LEFT)
        #self.couleurChoisi=choixCouleur[val]
        
        Bcouleur2.select()
            
         
        #self.parent.modele.joueurs.couleur= self.couleurChoisi
       # self.test=Label(text="self.parent.modele.joueurs.couleur=)    
        
        btnlancerpartie=Button(self.cadrelobby_Createur,text="Lancer partie",command=self.lancerpartie,bg='#A3C5D8',relief=FLAT,font='arial 12')
        btnlancerpartie.pack(fill=X,pady=(0,50),padx=(10,75),side=BOTTOM)
        
    def creercadrelobby_Connecteur(self):   
        #print(self.parent.inscrirejoueur().monnom)
        self.cadrelobby_Connecteur=Frame(self.cadreapp,bg='#15243d')
        
        self.titre=Label(self.cadrelobby_Connecteur,text="Rebonjour Voyageur",bg='#15243d',font='arial 20',foreground="white")
        self.titre.pack(pady=(50,0))
             
        
        self.listelobby_CO=Listbox(self.cadrelobby_Connecteur,bg='#A3C5D8',borderwidth=0,relief=FLAT,width=60,height=20)
        self.listelobby_CO.pack(side=LEFT,pady=50,padx=(75,10));
        
                
        self.cadreCouleur= Frame(self.cadrelobby_Connecteur,bg='#A3C5D8')
        self.cadreCouleur.pack()
        
        self.Sous_titre2=Label(self.cadreCouleur,text="Choisiez votre couleur",width=30,bg='#A3C5D8',font='arial 14')
        self.Sous_titre2.pack()
        #choixCouleur = [('#009ee3'),('#e5007d'),('#951b81'),('#95c11e'),('#f39200') ] #Couleur a choisir
        #couleurSelection =[('#80cef1'),('#e680b2'),('#c88fbf'),('#c9dc91'),('#f8c77e') ]    #Liste des couleur pour affichage selection
        
        self.varCouleur=StringVar()
        self.varCouleur.set="red"
        
        #v = IntVar()
        
        Bcouleur1=Radiobutton( self.cadreCouleur, bg='#009ee3',selectcolor='#80cef1', value='#009ee3',fg="white",indicatoron=0,offrelief=FLAT,width=3,variable=self.varCouleur,command=self.definircouleur1 )
        Bcouleur1.pack(anchor=W,pady=5,padx=5,fill="both", expand=True,side=LEFT)
        
        Bcouleur2=Radiobutton( self.cadreCouleur, bg='#e5007d',selectcolor='#e680b2', value='#e5007d',fg="white",indicatoron=0,offrelief=FLAT,width=3,variable=self.varCouleur,command=self.definircouleur2 )
        Bcouleur2.pack(anchor=W,pady=5,padx=5,fill="both", expand=True,side=LEFT)
        
        Bcouleur3=Radiobutton( self.cadreCouleur, bg='#951b81',selectcolor='#c88fbf', value='#951b81',fg="white",indicatoron=0,offrelief=FLAT,width=3,variable=self.varCouleur,command=self.definircouleur3 )
        Bcouleur3.pack(anchor=W,pady=5,padx=5,fill="both", expand=True,side=LEFT)
        
        Bcouleur4=Radiobutton( self.cadreCouleur, bg='#95c11e',selectcolor='#c9dc91', value='#95c11e',fg="white",indicatoron=0,offrelief=FLAT,width=3,variable=self.varCouleur,command=self.definircouleur4 )
        Bcouleur4.pack(anchor=W,pady=5,padx=5,fill="both", expand=True,side=LEFT)
        
        Bcouleur5=Radiobutton( self.cadreCouleur, bg='#f39200',selectcolor='#f8c77e', value='#f39200',fg="white",indicatoron=0,offrelief=FLAT,width=3,variable=self.varCouleur,command=self.definircouleur5 )
        Bcouleur5.pack(anchor=W,pady=5,padx=5,fill="both", expand=True,side=LEFT)
        
        Bcouleur6=Radiobutton( self.cadreCouleur, bg='#009ee3',selectcolor='#80cef1', value='#009ee3',fg="white",indicatoron=0,offrelief=FLAT,width=3,variable=self.varCouleur,command=self.definircouleur5 )
        Bcouleur6.pack(anchor=W,pady=5,padx=5,fill="both", expand=True,side=LEFT)
        #self.couleurChoisi=choixCouleur[val]
        
        #Bcouleur2.select()
        #self.couleurChoisi=choixCouleur[val]
            
         
        #self.parent.modele.joueurs.couleur= self.couleurChoisi
       # self.test=Label(text="self.parent.modele.joueurs.couleur=) 

        
    def connecterpartie(self):
        nom=self.nomsplash.get()
        ip=self.ipsplash.get()
        if nom and ip:
            self.parent.inscrirejoueur()
            self.changecadre(self.cadrelobby_Connecteur)
            print("BOUCLEATTENTE de CONNECTER")
            self.parent.boucleattente()
        
    def creerpartie(self):
        nom=self.nomsplash.get()
        ip=self.ipsplash.get()
        if nom and ip:
            self.parent.creerpartie()
            self.parent.inscrirejoueur()
            self.changecadre(self.cadrelobby_Createur)
            print("BOUCLEATTENTE de CREER")
            self.parent.boucleattente()
        
    def lancerpartie(self):
        self.parent.lancerpartie()
        
    def affichelisteparticipants(self,lj):
        self.listelobby_CR.delete(0,END)
        self.listelobby_CR.insert(0,lj)
        self.listelobby_CO.delete(0,END)
        self.listelobby_CO.insert(END,lj)
        
    def creeraffichercadrepartie(self,mod):
        self.nom=self.parent.monnom
        self.modele=mod
        joueur=self.modele.joueurs[self.nom]
        self.cadrepartie=Frame(self.cadreapp)
        self.cadrejeu=Frame(self.cadrepartie)
        self.canevas=Canvas(self.cadrepartie,width=1600,height=1000,bg="grey11",scrollregion=(0,0,self.modele.largeur,self.modele.hauteur))
        self.canevas.pack(side=LEFT,expand=True,fill=BOTH)
        self.canevas.pack(side=LEFT)
        self.canevas.bind("<1>", lambda event: self.canevas.focus_set())
        self.canevas.bind("<w>", lambda event: self.canevas.yview_scroll(-1, "units"))
        self.canevas.bind("<a>", lambda event: self.canevas.xview_scroll(-1, "units"))
        self.canevas.bind("<s>", lambda event: self.canevas.yview_scroll( 1, "units"))
        self.canevas.bind("<d>", lambda event: self.canevas.xview_scroll( 1, "units"))
        self.canevas.focus_set()
        self.canevas.bind("<Button-1>",self.cliqueGaucheCosmos)
        self.canevas.bind("<Button-3>",self.cliqueDroitCosmos)
        self.cadreinfo=Frame(self.cadrepartie,width=1000,height=100,bg="#455571",relief=RAISED)
        self.cadreinfo.pack(side=LEFT,fill=Y)
        
        self.cadreinfogen=Frame(self.cadreinfo,width=200,height=200,bg="#455571")
        self.cadreinfogen.pack()
        
        self.boiteinfo=Frame(self.cadreinfogen,width=220, height=100,bg="#455571",relief=RAISED)
        self.boiteinfo.pack(side=BOTTOM)
        self.boiteinfoMETAL=Frame(self.cadreinfogen,width=220, height=10,bg="#455571",relief=RAISED)
        self.boiteinfo.pack(side=BOTTOM)
        
        self.labid=Label(self.cadreinfogen,text="MINI\nORION",fg="#fbbfda",bg="#455571",font=("Helvetica",20),pady=10)
        self.labid.bind("<Button>",self.afficherplanemetemere)
        self.labid.pack()
        
        self.labid2=Label(self.boiteinfo,text="Gestion Colon\n", font=("Helvetica",15),bg="#455571",fg="#fbbfda")
        self.labid2.pack()
        
        self.labidcolons=Label(self.boiteinfo,text="Colons disponibles:  " +str(joueur.totalcolons),font=("Helvetica",10),bg="#455571",fg="#fbbfda")
        self.labidcolons.pack()
        self.labidjgaz=Label(self.boiteinfo,text="Gaz :  " +str(joueur.gaz),font=("Helvetica",10),bg="#455571",fg="#fbbfda")
        self.labidjgaz.pack()
        self.labidjmetal=Label(self.boiteinfo,text="Metal :  " +str(joueur.metal),font=("Helvetica",10),bg="#455571",fg="#fbbfda")
        self.labidjmetal.pack()
        self.labidjbouffe=Label(self.boiteinfo,text="Bouffe :  " +str(joueur.bouffe),font=("Helvetica",10),bg="#455571",fg="#fbbfda")
        self.labidjbouffe.pack()
        
        self.labidmetal=Label(self.cadreinfo, text="Metal sur planete : ",font=("Helvetica",10),bg="#455571",fg="#77D9D3" )
        self.labidgaz=Label(self.cadreinfo, text="Gaz sur planete: ",font=("Helvetica",10),bg="#455571",fg="#cc98e5" )
        self.labidvaisseauhp=Label(self.cadreinfo, text="HP : ",font=("Helvetica",10),bg="#455571",fg="#ffffff" )
        
        self.labidcolonplanete=Label(self.cadreinfo,fg="#fbbfda",bg="#455571",font=("Helvetica",10))
        
        self.labidcolonvaisseau=Label(self.cadreinfo,fg="#fbbfda",bg="#455571",font=("Helvetica",10))
        self.boutoncolonsajout=Button(self.cadreinfo,text="[EMBARQUER COLONS]",font=("Helvetica",8),bg="#455565",fg="#fbbfda",relief=RAISED,command=self.ajoutcolonsmodele)
        self.boutoncolonsretrait=Button(self.cadreinfo,text="[EJECTER COLONS]",font=("Helvetica",8),bg="#455565",fg="#fbbfda",relief=RAISED,command=self.retraitcolonsmodele)
        self.boutoncolonsdebarquer=Button(self.cadreinfo,text="[DEBARQUER COLONS]",font=("Helvetica",8),bg="#455565",fg="#fbbfda",relief=RAISED,command=self.debarquercolonsmodele)
        self.labiddebarquement=Label(self.cadreinfo,text="QUELLE PLANETE?",fg="#ff0000",bg="#455571",font=("Helvetica",15))
        
        self.btncreervaisseauAtt=Button(self.cadreinfo,text="Fregate",font=("Helvetica",8),bg="#455565",fg="#fbbfda",relief=RAISED,command=self.creervaisseauAtt)
        self.btncreervaisseauSonde=Button(self.cadreinfo,text="Sonde",font=("Helvetica",8),bg="#455565",fg="#fbbfda",relief=RAISED,command=self.creervaisseauSonde)
        self.btncreervaisseauTrans=Button(self.cadreinfo,text="Cargo",font=("Helvetica",8),bg="#455565",fg="#fbbfda",relief=RAISED,command=self.creervaisseauTrans)
        self.btnrecolte=Button(self.cadreinfo,text="[RECOLTE]",font=("Helvetica",8),bg="#455565",fg="#fbbfda",relief=RAISED,command=self.recoltemodele)
        self.afficherdecor(mod)
        
        self.changecadre(self.cadrepartie)
        
    def afficherdecor(self,mod):
        for i in range(len(mod.planetes)*3):
            x=random.randrange(mod.largeur)
            y=random.randrange(mod.hauteur)
            self.canevas.create_oval(x,y,x+1,y+1,fill="white",tags=("fond",))
            
        for i in mod.planetes:
            couleurfill = ""
            t=i.taille
            self.canevas.create_oval(i.x-t,i.y-t,i.x+t,i.y+t,fill="grey80",
                                    tags=(i.proprietaire,"planete",str(i.id)))
            
        for i in mod.joueurs:
            print(len(mod.joueurs[i].planetescontrolees))
            for j in mod.joueurs[i].planetescontrolees:
                t=j.taille
                self.canevas.create_oval(j.x-t,j.y-t,j.x+t,j.y+t,fill=mod.joueurs[i].couleur,
                                     tags=(j.proprietaire,"planete",str(j
                                     .id),"possession"))
                
        self.afficherpartie(mod)
                
    def afficherplanemetemere(self,evt):
        j=self.mod.joueurs[self.nom]
        couleur=j.couleur
        x=j.planetemere.x
        y=j.planetemere.y
        t=10
        self.canevas.create_oval(x-t,y-t,x+t,y+t,dash=(3,3),width=2,outline=couleur,
                                 tags=("planetemere","marqueur"))
    def creervaisseauAtt(self):
        print("Creer vaisseau")
        self.parent.creervaisseauAtt()
        #self.maselection=None
        #self.canevas.delete("marqueur")
        #self.btncreervaisseau.pack_forget()
        
    def creervaisseauTrans(self):
        print("Creer vaisseau")
        self.parent.creervaisseauTrans()
        #self.maselection=None
        #self.canevas.delete("marqueur")
        #self.btncreervaisseau.pack_forget()
        
    def creervaisseauSonde(self):
        print("Creer vaisseau")
        self.parent.creervaisseauSonde()
        #self.maselection=None
        #self.canevas.delete("marqueur")
        #self.btncreervaisseau.pack_forget()
            
    def afficherpartie(self,mod):
        self.canevas.delete("artefact")
        self.canevas.delete("marqueur")
        
        #for plan in self.canvas.gettags("planete"):
        j=mod.joueurs[self.nom]
        for joueur in mod.joueurs.keys():
            for p in mod.planetes:
                nonControlee = True
                for v in mod.joueurs[joueur].flotte:
                    if nonControlee:
                        if abs(v.x-p.x)<=3 and abs(v.y-p.y)<=3:
                            for autre_joueur in mod.joueurs.keys():
                                if autre_joueur!=joueur:
                                    if p in mod.joueurs[autre_joueur].planetescontrolees:
                                        mod.joueurs[autre_joueur].planetescontrolees.remove(p)
                            mod.joueurs[joueur].planetescontrolees.append(p)
                            p.proprietaire = joueur
                            self.canevas.itemconfig(self.canevas.find_closest(v.x, v.y), fill=mod.joueurs[joueur].couleur, outline="black", tags=(p.proprietaire,"planete",str(p.id), "possession") )
                            nonControlee = False
                            
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
                        if i.colon>0:
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
                        
        for i in mod.joueurs.keys():
            i=mod.joueurs[i]
            for j in i.flotte:
                if isinstance(j, VaisseauGuerre):
                    self.canevas.create_rectangle(j.x-3,j.y-3,j.x+3,j.y+3,fill=i.couleur,
                                                tags=(j.proprietaire,"flotte",str(j.id),"artefact"))
                if isinstance(j, Sonde):
                    self.canevas.create_oval(j.x-5,j.y-2,j.x+5,j.y+2,fill=i.couleur,
                                                tags=(j.proprietaire,"flotte",str(j.id),"artefact"))
                if isinstance(j, VaisseauTransport):
                    self.canevas.create_rectangle(j.x-5,j.y-4,j.x+5,j.y+4,fill=i.couleur,
                                                tags=(j.proprietaire,"flotte",str(j.id),"artefact"))
        
    def cliqueGaucheCosmos(self,evt):
        self.unpackBtnPlanete()
        self.unpackBtnFlotte()
        t=self.canevas.gettags(CURRENT)
        if t and t[0]==self.nom:
            self.maselection=[self.nom,t[1],t[2]]  #self.canevas.find_withtag(CURRENT)#[0]
            if t[1] == "planete":
                self.montreplaneteselection()
            elif t[1] == "flotte":
                self.montreflotteselection()

    def cliqueDroitCosmos(self,evt):
        self.unpackBtnPlanete()
        t=self.canevas.gettags(CURRENT)
        if "planete" in t and t[0]!=self.nom:
            if self.maselection:
                self.parent.ciblerflotte(self.maselection[2],t[2])
        else:
            if self.maselection:
                self.parent.deplacerVaisseau(self.canevas.canvasx(evt.x),self.canevas.canvasy(evt.y),self.maselection[2])
                    
    def montreplaneteselection(self):
        t=self.canevas.gettags(CURRENT)
        joueur=self.modele.joueurs[self.nom]
        for i in joueur.planetescontrolees:
            if t[2]==str(i.id):
                temp=joueur.planetescontrolees.index(i)
                self.tempRecolte=temp
        self.packBtnPlanete()
        self.labidcolonplanete.config(text="Colons sur la planete : "+str(joueur.planetescontrolees[temp].colon))
        self.labidcolonplanete.pack()
        self.labidmetal.config(text="Metal sur planete: "+str(joueur.planetescontrolees[temp].metal))
        self.labidmetal.pack()
        self.labidgaz.config(text="Gaz sur planete: "+str(joueur.planetescontrolees[temp].gaz))
        self.labidgaz.pack()
        
    def montreflotteselection(self):
        t=self.canevas.gettags(CURRENT)
        joueur=self.modele.joueurs[self.nom]
        for i in joueur.flotte:
            if t[2]==str(i.id):
                temp=joueur.flotte.index(i)
                self.indexLongTerme=temp
        self.labidcolonvaisseau.config(text="Colons dans le vaisseau : "+str(joueur.flotte[temp].inventaire))
        self.labidcolonvaisseau.pack()
        self.labidvaisseauhp.config(text="HP : "+str(joueur.flotte[temp].hp))
        self.labidvaisseauhp.pack()
        self.boutoncolonsajout.pack()
        self.boutoncolonsretrait.pack()
        self.boutoncolonsdebarquer.pack()
        if joueur.flotte[temp].inventaire==0:
            self.boutoncolonsretrait.config(state=DISABLED)
            self.boutoncolonsretrait.pack()
            self.boutoncolonsdebarquer.config(state=DISABLED)
            self.boutoncolonsdebarquer.pack()
        else:
            self.boutoncolonsretrait.config(state=NORMAL)
            self.boutoncolonsretrait.pack()
            self.boutoncolonsdebarquer.config(state=NORMAL)
            self.boutoncolonsdebarquer.pack()

    def afficherartefacts(self,joueurs):
        pass #print("ARTEFACTS de ",self.nom)
    
    def unpackBtnPlanete(self):
        self.labidcolonplanete.pack_forget()
        self.labidmetal.pack_forget()
        self.labidgaz.pack_forget()
        self.btncreervaisseauAtt.pack_forget()
        self.btncreervaisseauSonde.pack_forget()
        self.btncreervaisseauTrans.pack_forget()
        self.boutoncolonsajout.pack_forget()
        self.btnrecolte.pack_forget()
        
    def unpackBtnFlotte(self):
        self.labidvaisseauhp.pack_forget()
        self.labidcolonvaisseau.pack_forget()
        self.boutoncolonsajout.pack_forget()
        self.boutoncolonsretrait.pack_forget()
        self.boutoncolonsdebarquer.pack_forget()
        
    def packBtnPlanete(self):
        self.labidcolonplanete.pack()
        self.btncreervaisseauAtt.pack()
        self.btncreervaisseauSonde.pack()
        self.btncreervaisseauTrans.pack()
        self.btnrecolte.pack()
        
    def ajoutcolonsmodele(self):
        joueur=self.modele.joueurs[self.nom]
        t=self.canevas.gettags(CURRENT)
        if joueur.planetescontrolees[0].colon > 0:
            for i in joueur.flotte:
                if self.maselection[2]==str(i.id):
                    temp=joueur.flotte.index(i)
                    joueur.flotte[temp].load(1)
                    joueur.planetescontrolees[0].colon-=1
                    self.labidcolonvaisseau.config(text="Colons dans le vaisseau : "+str(joueur.flotte[temp].inventaire))
                    self.labidcolonvaisseau.pack()
                    self.boutoncolonsretrait.config(state=NORMAL)
                    self.boutoncolonsretrait.pack()
                    self.boutoncolonsdebarquer.config(state=NORMAL)
                    self.boutoncolonsdebarquer.pack()
            if joueur.flotte[temp].inventaire==joueur.flotte[temp].inventaireMAX:
                self.boutoncolonsajout.config(state=DISABLED)
                self.boutoncolonsajout.pack()
        else:
            self.boutoncolonsajout.config(state=DISABLED)
            self.boutoncolonsajout.pack()
            
    def retraitcolonsmodele(self):
        joueur=self.modele.joueurs[self.nom]
        t=self.canevas.gettags(CURRENT)
        for i in joueur.flotte:
            if self.maselection[2]==str(i.id):
                temp=joueur.flotte.index(i)
        joueur.totalcolons-=joueur.flotte[temp].inventaire
        joueur.flotte[temp].unload()
        self.labidcolons.config(text="Colons disponibles:  " +str(joueur.totalcolons))
        self.labidcolons.pack()
        self.labidcolonvaisseau.config(text="Colons dans le vaisseau : "+str(joueur.flotte[temp].inventaire))
        self.labidcolonvaisseau.pack()
        self.boutoncolonsretrait.config(state=DISABLED)
        #self.boutoncolonsretrait.pack()
        self.boutoncolonsajout.config(state=NORMAL)
        self.boutoncolonsdebarquer.config(state=DISABLED)
        #self.boutoncolonsajout.pack()
    
    def debarquercolonsmodele(self):
        self.labiddebarquement.pack()
        self.canevas.bind("<Button-1>",self.cliqueGauchePlanete)

    def cliqueGauchePlanete(self,evt):
        joueur=self.modele.joueurs[self.nom]
        self.canevas.bind("<Button-1>",self.cliqueGaucheCosmos)
        t=self.canevas.gettags(CURRENT)
        if t and t[0]==self.nom:
            self.maselection=[self.nom,t[1],t[2]]  #self.canevas.find_withtag(CURRENT)#[0]
            if t[1] == "planete":
                for i in joueur.planetescontrolees:
                    if t[2]==str(i.id):
                        tempPlanete=joueur.planetescontrolees.index(i)
                joueur.planetescontrolees[tempPlanete].colon+=joueur.flotte[self.indexLongTerme].inventaire
                joueur.flotte[self.indexLongTerme].inventaire=0
                self.indexLongTerme=-1
                self.labiddebarquement.pack_forget()
                self.unpackBtnFlotte()
                self.montreplaneteselection()
        else:
            self.unpackBtnFlotte()
            
    def recoltemodele(self):
        joueur=self.modele.joueurs[self.nom]
        joueur.recoltePlaneteJoueur()
        joueur.ranOnce=False
        self.parent.chronoRecolte()
        if joueur.recolteActivee==True:
            self.btnrecolte.config(state=DISABLED)
        elif joueur.recolteActivee==False:
            self.btnrecolte.config(state=NORMAL)
        self.labidjgaz.pack_forget()
        self.labidjmetal.pack_forget()
        self.labidjbouffe.pack_forget()
        self.labidjgaz=Label(self.boiteinfo,text="Gaz :  " +str(joueur.gaz),font=("Helvetica",10),bg="#455571",fg="#fbbfda")
        self.labidjgaz.pack()
        self.labidjmetal=Label(self.boiteinfo,text="Metal :  " +str(joueur.metal),font=("Helvetica",10),bg="#455571",fg="#fbbfda")
        self.labidjmetal.pack()
        self.labidjbouffe=Label(self.boiteinfo,text="Bouffe :  " +str(joueur.bouffe),font=("Helvetica",10),bg="#455571",fg="#fbbfda")
        self.labidjbouffe.pack()
        
    def definircouleur1(self):
        self.varCouleur='#009ee3'
        print("===============+++======="+self.varCouleur)
    def definircouleur2(self):
        self.varCouleur='#e5007d'
        print("==============+++========"+self.varCouleur)
    def definircouleur3(self):
        self.varCouleur='#951b81'
        print("==========++++============"+self.varCouleur)
    def definircouleur4(self):
        self.varCouleur='#95c11e'
        print("======================"+self.varCouleur)
    def definircouleur5(self):
        self.varCouleur='#f39200'
        print("============++++=========="+self.varCouleur)
        
    def metAJourData(self):
        joueur=self.modele.joueurs[self.nom]
        self.labidcolons.config(text="Colons disponibles:  " +str(joueur.totalcolons))
        self.labidjgaz.config(text="Gaz :  " +str(joueur.gaz))
        self.labidjmetal.config(text="Metal :  " +str(joueur.metal))
        self.labidjbouffe.config(text="Bouffe :  " +str(joueur.bouffe))
