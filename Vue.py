from tkinter import *
import os,os.path
import random

class Vue():
	def __init__(self,parent,ip,nom):
		self.parent=parent
		self.root=Tk()

		self.root.attributes('-fullscreen', 1) #Pour full screen
		self.root.configure(bg='#1c4873') # Background de ma page
		
		self.button = Button(self.root, text="X", command=self.root.destroy, font='arial 20', relief=FLAT,bg='#1c4873',foreground="white")
		self.button.pack(side=TOP, anchor=E)   
		
		self.cadreactif=None
		self.maselection=None
		self.root.title(os.path.basename(sys.argv[0]))
		self.modele=None
		self.nom=""
		self.cadreapp=Frame(self.root,width=800,height=600)			#Frame de base a mes fenetre
		self.cadreapp.pack(fill="none", expand=True) # Pour centrer la fenetre
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
		
		self.cadresplash=Frame(self.cadreapp,bg='#15243d')
	
		self.titre = Label(self.cadresplash, text = "Bienvenue dans la galaxie orion voyageur!",bg='#15243d',font='arial 20',foreground="white")
		self.titre.pack(pady=(100,20),padx=100);
		
		soustitre=Label(self.cadresplash, text = "Pour des fin de securite veuillez vous identifier",bg='#15243d',font='arial 16',foreground="white")
		soustitre.pack(pady=10,padx=10);
		
		self.nomsplash=Entry(self.cadresplash,bg='#A3C5D8',relief=FLAT,foreground="white",font='arial 14',highlightthickness=2,highlightcolor='#849fae')
		self.nomsplash.insert(0, nom)
		self.nomsplash.pack(pady=10)
		
		self.ipsplash=Entry(self.cadresplash,bg='#A3C5D8',relief=FLAT,foreground="white",font='arial 14',highlightthickness=2,highlightcolor='#849fae')
		self.ipsplash.insert(0, ip)
		self.ipsplash.pack(pady=20)
		
		
		btncreerpartie=Button(self.cadresplash,text="Creer partie",bg='#A3C5D8',command=self.creerpartie,relief=FLAT,font='arial 12')
		btncreerpartie.pack(fill="both", expand=True,side=LEFT, padx=(75,5),pady=(0,50))
		btnconnecterpartie=Button(self.cadresplash,text="Connecter partie",bg='#A3C5D8',command=self.connecterpartie,relief=FLAT,font='arial 12')
		btnconnecterpartie.pack(fill="both", expand=True,side=LEFT,padx=(5,75),pady=(0,50))
		

            
    def creercadrelobby(self):
        self.cadrelobby=Frame(self.cadreapp,bg='#15243d')
        
        self.titre=Label(self.cadrelobby,text="Rebonjour Voyageur",bg='#15243d',font='arial 20',foreground="white")
        self.titre.pack(pady=(50,0))
             
        
        self.listelobby=Listbox(self.cadrelobby,bg='#A3C5D8',borderwidth=0,relief=FLAT,width=60,height=20)
        self.listelobby.pack(side=LEFT,pady=50,padx=(75,10));
        
        self.MODES = [
        ("Monochrome", "1"),
        ("Grayscale", "2"),
        ("True color", "3"),
        ("Color separation", "4") ]

    v = IntVar()
    v.set("L") # initialize

    for int, mode in self.MODES:
        self.b = Radiobutton(self.cadrelobby, text=text,variable=v, value=mode)
        self.b.pack(anchor=W)
        
        btnlancerpartie=Button(self.cadrelobby,text="Lancer partie",command=self.lancerpartie,bg='#A3C5D8',relief=FLAT,font='arial 12')
        btnlancerpartie.pack(fill=X,pady=(0,50),padx=(10,75),side=BOTTOM)
        

        
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
        
        joueur=self.mod.joueurs[self.nom]
        self.cadrepartie=Frame(self.cadreapp)
        self.cadrejeu=Frame(self.cadrepartie)
        self.canevas=Canvas(self.cadrepartie,width=mod.largeur,height=mod.hauteur,bg="red")
        self.canevas.pack(side=LEFT)
        
        self.canevas.bind("<Button>",self.cliquecosmos)
        
        self.cadreinfo=Frame(self.cadrepartie,width=200,height=100,bg="#455571",relief=RAISED)
        self.cadreinfo.pack(side=LEFT,fill=Y)
        
        self.cadreinfogen=Frame(self.cadreinfo,width=200,height=200,bg="#455571")
        self.cadreinfogen.pack()
        
        self.boiteinfo=Frame(self.cadreinfogen,width=200, height=100,bg="#455571",relief=RAISED)
        self.boiteinfo.pack(side=BOTTOM)
        
        self.boiteinfo2=Frame(self.boiteinfo,width=200, height=100,bg="#455571",relief=RAISED)
        self.boiteinfo2.pack(side=BOTTOM)
        
        self.boiteinfo3=Frame(self.boiteinfo2,width=200, height=100,bg="#455571",relief=RAISED)
        self.boiteinfo3.pack(side=BOTTOM)
        
        
        self.labid=Label(self.cadreinfogen,text="MINI\nORION",fg="#fbbfda",bg="#455571",font=("Helvetica",20),pady=10)
        self.labid.bind("<Button>",self.afficherplanemetemere)
        self.labid.pack()
        
        self.labid2=Label(self.boiteinfo,text="Gestion Colon\n", font=("Helvetica",15),bg="#455571",fg="#fbbfda")
        self.labid2.pack()
        
        self.labidcolons=Label(self.boiteinfo,text="Colons disponibles: ",font=("Helvetica",10),bg="#455571",fg="#fbbfda")
        self.labidcolons.pack(side=LEFT)
        self.labidcbcolons=Label(self.boiteinfo,text=joueur.totalcolons,font=("Helvetica",10),bg="#455571",fg="#fbbfda")
        self.labidcbcolons.pack(side=RIGHT)
        
        self.boutoncolonsajout=Button(self.cadreinfo,text="[CREER COLONS]",font=("Helvetica",8),bg="#455565",fg="#fbbfda",relief=RAISED,command=self.modifcolonsmodele(1))
        #self.boutoncolonsretrait=Button(self.cadreinfo,text="[RETRAIT COLONS]",font=("Helvetica",8),bg="#455565",fg="#fbbfda",relief=RAISED)
        
        self.cadreinfobtm=Frame(self.cadreapp,width=704, height=120, bg="#455571")
        self.cadreinfobtm.pack(side=BOTTOM,fill=Y)
        
        self.btncreervaisseau=Button(self.cadreinfo,text="Vaisseau",font=("Helvetica",8),bg="#455565",fg="#fbbfda",relief=RAISED,command=self.creervaisseau)
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

	def cliqueDroitCosmos(self,evt):
		self.btncreervaisseau.pack_forget()
		t=self.canevas.gettags(CURRENT)
		print(str(t))
		if t and t[0]==self.nom:
			self.maselection=[self.nom,t[1],t[2]]  #self.canevas.find_withtag(CURRENT)#[0]
			if t[1] == "planete":
				self.montreplaneteselection()
			elif t[1] == "flotte":
				self.montreflotteselection()

	def cliqueGaucheCosmos(self,evt):
		self.btncreervaisseau.pack_forget()
		t=self.canevas.gettags(CURRENT)

		if "planete" in t and t[0]!=self.nom:
			if self.maselection:
				#pass # attribuer cette planete a la cible de la flotte selectionne
				self.parent.ciblerflotte(self.maselection[2],t[2])
			self.lbselectecible.pack_forget()
		
		else:
			if self.maselection:	
				self.parent.deplacerVaisseau(evt.x,evt.y,self.maselection[2])
				self.lbselectecible.pack_forget()
			
	def montreplaneteselection(self):
		self.btncreervaisseau.pack()
		self.boutoncolonsajout.pack()
		#self.boutoncolonsrretrait.pack()
		
	def montreflotteselection(self):
		self.lbselectecible.pack()
	
	
	def modifcolonsmodele(self,nb):
		joueur=self.mod.joueurs[self.nom]
		#joueur.totalcolons+=nb
	
	def afficherartefacts(self,joueurs):
		pass #print("ARTEFACTS de ",self.nom)
