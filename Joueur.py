from Id import *
import random
from Vaisseau import *

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