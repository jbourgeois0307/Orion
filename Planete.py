import random
import math


class Planete():
    def __init__(self, x, y, id):
        self.id = id
        self.proprietaire = "inconnu"
        self.x = x
        self.y = y
        self.colon = 0
        self.colonMetal = 0
        self.colonGaz = 0
        self.colonBouffe = 0
        self.taille = 18          #random.randrange(4, 6)
        self.metal = (random.randrange(1000, 2000) * self.taille)
        self.gaz = (random.randrange(1000, 2000) * self.taille)
        self.espace = 6 * self.taille
        self.hp = 5000
        self.batiment = {}
        self.Canon = {}

    def recolte(self, joueur):
        if self.metal > 0:
            if self.metal - 5 * self.colonMetal > 0:
                self.metal -= 5 * self.colonMetal
                joueur.metal += 5 * self.colonMetal
            else:
                joueur.metal += self.metal
                self.metal = 0

        if self.gaz > 0:
            if self.gaz - 5 * self.colonGaz > 0:
                self.gaz -= 5 * self.colonGaz
                joueur.gaz += 5 * self.colonGaz
            else:
                joueur.gaz += self.gaz
                self.gaz = 0

            ##self.proprietaire.bouffe+= 10*self.colonBouffe

    def construireFerme(self, joueur):
        if self.espace > Ferme.espace:
            self.batiment.append(Ferme(self, joueur))

    def construireMine(self, joueur):
        if self.espace > Mine.espace:
            self.batiment.append(Mine(self, joueur))

    def construireHangar(self, joueur):
        if self.espace > Hangar.espace:
            self.batiment.append(Hangar(self, joueur))

    def construireCanon(self, joueur):
        if self.espace > Canon.espace:
            self.Canon.append(Canon(self, joueur))

    def priseDePossession(self, joueur):
        self.proprietaire = joueur.nom
        joueur.planetescontrolees.append(self)
    
    def ajoutColon(self,joueur,nb):
        self.proprietaire = joueur.nom
        self.colon+=nb
        
    # (self.proprietaire).planetescontrolees.append(self)

class PlaneteMere():
    def __init__(self,x,y,id):
        self.id= id
        self.proprietaire="inconnu"                     #tagger
        self.x=x
        self.y=y
        self.colon = 10
        self.type = 10
        self.taille= 24
        self.quantityRess = 9000            #hard coded for now



class Batiment():
    def __init__(self, parent, proprietaire):
        self.parent = parent
        self.proprietaire = proprietaire

    def salvage(self):
        self.proprietaire.metal += 0.35 * self.coutMetal
        self.proprietaire.gaz += 0.35 * self.coutGaz


class Ferme(Batiment):
    def __init__(self):
        Batiment.__init__(self, parent, proprietaire)
        self.espace = 3
        self.coutMetal = 50
        self.coutGaz = 25


class Mine(Batiment):
    def __init__(self):
        Batiment.__init__(self, parent, proprietaire)
        self.espace = 5
        self.coutMetal = 125
        self.coutGaz = 75


class Hangar(Batiment):
    def __init__(self):
        Batiment.__init__(self, parent, proprietaire)
        self.espace = 12
        self.coutMetal = 200
        self.coutGaz = 130


class Canon(Batiment):
    def __init__(self):
        Batiment.__init__(self, parent, proprietaire)
        self.espace = 3
        self.coutMetal = 60
        self.coutGaz = 30
        self.hp = 250
        self.dmg = 35
        self.range = 85
        self.cible

    def attack(self):
        distance = math.sqrt(math.power(self.x - self.cible.x, 2) + math.power(self.y - self.cible.y, 2))

        if distance < self.range:
            ##refaire missile et checker le tk.after
            ##missile = self.parent.parent.Vue.canevas.create_line(self.cible.x, self.cible.y, self.x, self.y, color="red")
            self.cible.hp -= self.damage
            tk.after(self.attackspeed, self.attack())
            time.sleep(0.5)
            ##del missile
