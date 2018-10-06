import random
from helper import Helper as hlp


class Id():
    id=0
    def prochainid():
        Id.id+=1
        return Id.id

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

class VaisseauGuerre(Vaisseau):
    def __init__(self, nom,x,y):
        self.id=Id.prochainid()
        self.proprietaire=nom
        self.x=x
        self.y=y
        self.inventaire=0
        self.vitesse=2.5
        self.hp = 350
        self.damage = 40
        self.attackspeed = 0.5
        self.viewdistance = 100
        self.range = 75
        self.cible=None
    
    def attack(self):
        
        distance = math.sqrt(math.pow(self.x-self.cible.x,2)+math.pow(self.y-self.cible.y,2))
        
        if distance < self.range:
            self.parent.parent.Vue.canevas.create_line(self.cible.x, self.cible.y, self.x, self.y, color="red")
            self.cible.hp -= self.damage
            tk.after(self.attackspeed, self.attack())
            
class VaisseauTransport(Vaisseau):
    def __init__(self, nom,x,y):
        self.id=Id.prochainid()
        self.proprietaire=nom
        self.x=x
        self.y=y
        self.inventaire=20
        self.vitesse=1.8
        self.hp = 500
        self.damage = 0
        self.attackspeed = 0
        self.viewdistance = 100
        self.range = 0
        self.cible=None
        
    def load():
        pass
    def unload():
        pass
        
class Sonde(Vaisseau):
    def __init__(self, nom,x,y):
        self.id=Id.prochainid()
        self.proprietaire=nom
        self.x=x
        self.y=y
        self.inventaire=0
        self.vitesse=3
        self.hp = 60
        self.damage = 0
        self.attackspeed = 0
        self.viewdistance = 125
        self.range = 0
        self.cible=None

class DeathStar(Vaisseau):
    def __init__(self, nom,x,y):
        self.id=Id.prochainid()
        self.proprietaire=nom
        self.x=x+30
        self.y=y+30
        self.inventaire=0
        self.vitesse=0
        self.hp = 800
        self.damage = 99999
        self.attackspeed = 0.1
        self.viewdistance = 125
        self.range = 999999999
        self.cible=None    

class Planete():
    def __init__(self,x,y):
        self.id=Id.prochainid()
        self.proprietaire="inconnu"
        self.x=x
        self.y=y
        self.taille=random.randrange(4,6)
        self.metal=(random.randrange(1000,2000)*self.taille)
        self.gaz=(random.randrange(1000,2000)*self.taille)
        self.espace = 6*self.taille
        self.hp = 5000

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
            """
            else:
                i.cible=random.choice(self.parent.planetes)
            """
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