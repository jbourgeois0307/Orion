from Id import *
import random
from helper import Helper as hlp

class Vaisseau():
 
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
                
class VaisseauGuerre(Vaisseau):
    def __init__(self,nom,x,y):
        
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
            
        distance = math.sqrt(math.power(self.x-self.cible.x,2)+math.power(self.y-self.cible.y,2))
       
        if distance < self.range:
            missile = self.parent.parent.Vue.canevas.create_line(self.cible.x, self.cible.y, self.x, self.y, color="red")
            self.cible.hp -= self.damage
            tk.after(self.attackspeed, self.attack())
            time.sleep(0.5)
            del missile
            
class VaisseauTransport(Vaisseau):
    def __init__(self, nom,x,y):
        
        self.id=Id.prochainid()
        self.proprietaire=nom
        self.x=x
        self.y=y
        self.inventaireMAX=20
        self.inventaire=0
        self.vitesse=1.8
        self.hp = 500
        self.damage = 0
        self.attackspeed = 0
        self.viewdistance = 100
        self.range = 0
        self.cible=None

        
    def load(self, nombre):
        if self.inventaire < self.inventaireMAX:
            if self.inventaire+nombre <= self.inventaireMAX:
                self.inventaire += nombre
                return nombre
            else:
                nombre = self.inventaireMAX - self.inventaire
                self.inventaire = self.inventaireMAX
                return nombre
    def unload():
        self.cible.colon += self.inventaire
        self.inventaire = 0
        
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
            
    def destroyPlanet(self):
        
        if self.cible in jeu.planetes:
            self.cible.remove