from tkinter import *
import os,os.path
import random
from Vaisseau import *

class Vue():
	def __init__(self,parent,ip,nom):
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
		self.cadreapp=Frame(self.root,width=800,height=600)			#Frame de base a mes fenetre
		self.cadreapp.pack(fill="none", expand=True) # Pour centrer la fenetre
		self.creercadresplash(ip,nom)
		self.creercadrelobby()
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
		
		self.nbetoile=Entry(self.cadrelobby,bg='#A3C5D8',width=30,relief=FLAT,font='arial 12',justify=CENTER)
		self.nbetoile.insert(0, 100)
		self.nbetoile.pack(pady=(50,10),padx=(10,75));
		
		self.largeespace=Entry(self.cadrelobby,bg='#A3C5D8',width=30,relief=FLAT,font='arial 12',justify=CENTER) 
		self.largeespace.insert(0, 1000)
		self.largeespace.pack(pady=(10,10),padx=(10,75));
		
		self.hautespace=Entry(self.cadrelobby,bg='#A3C5D8',width=30,relief=FLAT,font='arial 12',justify=CENTER)
		self.hautespace.insert(0, 800)
		self.hautespace.pack(pady=(10,10),padx=(10,5));
		
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
		self.modele=mod
		
		joueur=self.modele.joueurs[self.nom]
		self.cadrepartie=Frame(self.cadreapp)
		self.cadrejeu=Frame(self.cadrepartie)
		self.canevas=Canvas(self.cadrepartie,width=1600,height=1000,bg="grey11",scrollregion=(0,0,self.modele.largeur,self.modele.hauteur))
		#self.hbar=Scrollbar(self.cadrepartie,orient=HORIZONTAL, width=0)
		#self.hbar.pack(side=BOTTOM,fill=X)
		#self.hbar.config(command=self.canevas.xview)
		#self.vbar=Scrollbar(self.cadrepartie,orient=VERTICAL,width = 0)
		#self.vbar.pack(side=RIGHT,fill=Y)
		#self.vbar.config(command=self.canevas.yview)
		#self.canevas.config(width=1080,height=1080)
		#self.canevas.config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)
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
		
		self.labidcolonvaisseau=Label(self.cadreinfo,fg="#fbbfda",bg="#455571",font=("Helvetica",10))
		self.boutoncolonsajout=Button(self.cadreinfo,text="[LOAD COLONS]",font=("Helvetica",8),bg="#455565",fg="#fbbfda",relief=RAISED,command=self.modifcolonsmodele)
		#,command=self.modifcolonsmodele(1,mod)
		self.boutoncolonsretrait=Button(self.cadreinfo,text="[DELOAD COLONS]",font=("Helvetica",8),bg="#455565",fg="#fbbfda",relief=RAISED)
		#,command=self.modifcolonsmodele(-1,mod)
		
		self.cadreinfobtm=Frame(self.cadreapp,width=704, height=120, bg="#455571")
		self.cadreinfobtm.pack(side=BOTTOM,fill=Y)
		
		self.btncreervaisseauAtt=Button(self.cadreinfo,text="Fregate",font=("Helvetica",8),bg="#455565",fg="#fbbfda",relief=RAISED,command=self.creervaisseauAtt)
		self.btncreervaisseauSonde=Button(self.cadreinfo,text="Sonde",font=("Helvetica",8),bg="#455565",fg="#fbbfda",relief=RAISED,command=self.creervaisseauSonde)
		self.btncreervaisseauTrans=Button(self.cadreinfo,text="Cargo",font=("Helvetica",8),bg="#455565",fg="#fbbfda",relief=RAISED,command=self.creervaisseauTrans)
		self.lbselectecible=Label(self.cadreinfo,text="Choisir cible",bg="#455571",fg="red")
		
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
			elif self.maselection[1]=="flotte":
				for i in joueur.flotte:
					if i.id == int(self.maselection[2]):
						x=i.x
						y=i.y
						t=10
						self.canevas.create_rectangle(x-t,y-t,x+t,y+t,dash=(2,2),outline=mod.joueurs[self.nom].couleur,
												 tags=("select","marqueur"))
		#else:
		#	 self.canevas.delete("marqueur")
			
		
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
		print(str(t))
		if t and t[0]==self.nom:
			self.maselection=[self.nom,t[1],t[2]]  #self.canevas.find_withtag(CURRENT)#[0]
			if t[1] == "planete":
				self.montreplaneteselection()
			elif t[1] == "flotte":
				self.montreflotteselection(0)

	def cliqueDroitCosmos(self,evt):
		self.unpackBtnPlanete()
		t=self.canevas.gettags(CURRENT)
		

		if "planete" in t and t[0]!=self.nom:
			if self.maselection:
				#pass # attribuer cette planete a la cible de la flotte selectionne
				self.parent.ciblerflotte(self.maselection[2],t[2])
			self.lbselectecible.pack_forget()
		
		else:
			if self.maselection:
				self.parent.deplacerVaisseau(self.canevas.canvasx(evt.x),self.canevas.canvasy(evt.y),self.maselection[2])
				self.lbselectecible.pack_forget()
			
	def montreplaneteselection(self):
		self.packBtnPlanete()
		#self.boutoncolonsrretrait.pack()
		
	def montreflotteselection(self,i):
		self.lbselectecible.pack()
		joueur=self.modele.joueurs[self.nom]
		self.lbselectecible.pack()
		self.labidcolonvaisseau.config(text="Colons dans le vaisseau : "+str(joueur.flotte[i].inventaire))
		self.labidcolonvaisseau.pack()
		self.boutoncolonsajout.pack()
		self.boutoncolonsretrait.pack()
		
	
	def afficherartefacts(self,joueurs):
		pass #print("ARTEFACTS de ",self.nom)
	
	def unpackBtnPlanete(self):
		self.btncreervaisseauAtt.pack_forget()
		self.btncreervaisseauSonde.pack_forget()
		self.btncreervaisseauTrans.pack_forget()
		self.boutoncolonsajout.pack_forget()
		
	def unpackBtnFlotte(self):
		self.labidcolonvaisseau.pack_forget()
		self.boutoncolonsajout.pack_forget()
		self.boutoncolonsretrait.pack_forget()
		
	def packBtnPlanete(self):
		self.btncreervaisseauAtt.pack()
		self.btncreervaisseauSonde.pack()
		self.btncreervaisseauTrans.pack()
		
	def modifcolonsmodele(self):
		joueur=self.mod.joueurs[self.nom]
		joueur.flotte[0].load(1)
		self.labidcolonvaisseau.pack()