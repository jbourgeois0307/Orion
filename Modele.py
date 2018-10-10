import random
from Planete import *
from Vaisseau import *
from Joueur import *

class Modele():
    def __init__(self,parent,joueurs):
        
        self.parent=parent
        self.joueurs={}
        self.actionsafaire={}
        self.planetes=[]
        self.terrain=[]
        np=len(joueurs)
        self.largeur=2040 + np * 680        #self.parent.vue.root.winfo_screenwidth()
        self.hauteur=1920 + np * 480       #self.parent.vue.root.winfo_screenheight()
        self.creerplanetes(joueurs, self)
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
        
    def creerplanetes(self,joueurs, parent):
        np=len(joueurs)                     #nombre joueurs
        planes=[]
        self.hauteur = parent.hauteur
        self.largeur = parent.largeur
        
        if np == 2:
            planes.append(PlaneteMere(100, self.hauteur /2))
            planes.append(PlaneteMere(self.largeur - 100, self.hauteur /2))
        
        elif np == 3:
            planes.append(PlaneteMere(self.largeur / 2, 100))
            planes.append(PlaneteMere(100, self.hauteur - 100))
            planes.append(PlaneteMere(self.largeur - 100, self.hauteur - 100))
            
        elif np == 4:
            planes.append(PlaneteMere(100 , 100))
            planes.append(PlaneteMere(self.largeur - 100, 100))
            planes.append(PlaneteMere(100, self.hauteur - 100))
            planes.append(PlaneteMere(100, self.hauteur - 100))
       
        elif np == 5:
            planes.append(PlaneteMere(self.largeur /2 , 100))
            planes.append(PlaneteMere(100, self.hauteur / 3.09))
            planes.append(PlaneteMere(self.largeur - 100, self.hauteur / 3.09))
            planes.append(PlaneteMere(self.largeur * 0.25, self.hauteur -100))
            planes.append(PlaneteMere(self.largeur * 0.75, self.hauteur -100))
        
        elif np == 6:
            planes.append(PlaneteMere(self.largeur * 0.24, 50))
            planes.append(PlaneteMere(50, self.hauteur / 2))
            planes.append(PlaneteMere(self.largeur * 0.75, 50))
            planes.append(PlaneteMere(self.largeur - 50, self.hauteur * 0.50))
            planes.append(PlaneteMere(self.largeur * 0.75, self.hauteur -50))
            planes.append(PlaneteMere(self.largeur * 0.24, self.hauteur -50))
            
        
        couleurs=["red","blue","lightgreen","yellow",
                  "lightblue","pink","gold","purple"]
           
        for i in joueurs:
            self.joueurs[i]=Joueur(self,i,planes.pop(0),couleurs.pop(0))
                
        
       
        bordure=24
        for i in range(3 + np):
            for j in range(4 + np):
                planetPerParsec = (range.randrange(14, 22))
                planetePlacees = []                                                 #ajouter liste avec types de planetes par parsec
                for k in range(planetPerParsec):
                    x=random.randrange(680 * i -(2*bordure))+bordure
                    y=random.randrange(480 * j -(2*bordure))+bordure
                    for L in planetePlacees:
                        if((((L.x - x)** 2 + (L.y - y) ** 2) ** 0.5 ) > 35):
                            planetePlacees.append(self.planetes.append(Planete(x,y)))
                        else:
                            k -= 1

       
            
        '''    
        while np:
            p=random.choice(self.planetes)
            if p not in planes:
                planes.append(p)
                self.planetes.remove(p)
                np-=1
       
        '''
        
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