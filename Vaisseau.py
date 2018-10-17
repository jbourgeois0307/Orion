import random
from helper import Helper as hlp
import math

class Vaisseau():
    def __init__(self,nom,x,y,id):
        self.id=id
        self.proprietaire=nom
        self.vitesse=6
        self.x=x
        self.y=y
        self.cible = None
 
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
            if isinstance(self.cible, Vaisseau):
                if self.cible.proprietaire != self.proprietaire:
                    self.attack()
        else:
            print("PAS DE CIBLE")
            
    def load(self, nombre):
        if self.inventaire < self.inventaireMAX:
            if self.inventaire+nombre <= self.inventaireMAX:
                self.inventaire += nombre
                return nombre
            else:
                nombre = self.inventaireMAX - self.inventaire
                self.inventaire = self.inventaireMAX
                return nombre
            
    def unload(self):
        #self.cible.colon += self.inventaire
        self.inventaire = 0
        
                
class VaisseauGuerre(Vaisseau):
    def __init__(self, nom,x,y,id):
        Vaisseau.__init__(self, nom, x, y,id)
        self.inventaireMAX=5
        self.inventaire=0
        self.vitesse=2.5
        self.hp = 350
        self.damage = 40
        self.attackspeed = 0.5
        self.viewdistance = 100
        self.range = 75

    
    def attack(self):
            
        distance = math.sqrt(math.pow(self.x-self.cible.x,2)+math.pow(self.y-self.cible.y,2))
       
        if distance < self.range:
            ##refaire missile et checker le tk.after
    
            self.cible.hp -= self.damage
            if self.cible.hp == 0:
                self.cible.remove
            #tk.after(self.attackspeed, self.attack())
        else:
            self.cible = None
            #del missile
            
class VaisseauTransport(Vaisseau):
    def __init__(self,nom,x,y,id):
        Vaisseau.__init__(self, nom, x, y,id)
        self.inventaireMAX=20
        self.inventaire=0
        self.vitesse=1.8
        self.hp = 500
        self.damage = 0
        self.attackspeed = 0
        self.viewdistance = 100
        self.range = 0
        
    def attack(self):
        pass
        
class Sonde(Vaisseau):
    def __init__(self,nom,x,y,id):
        Vaisseau.__init__(self, nom, x, y,id)
        print("teste")
        self.inventaireMAX=1
        self.inventaire=0
        self.vitesse=3
        self.hp = 60
        self.damage = 0
        self.attackspeed = 0
        self.viewdistance = 125
        self.range = 0
    
    def attack(self):
        pass
    
class DeathStar():
    def __init__(self, nom,x,y):
        self.inventaireMAX=100
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
     
    def attack(self):
        pass     
      
    def destroyPlanet(self):
        if self.cible in jeu.planetes:
            self.cible.remove