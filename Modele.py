import random
from helper import Helper as hlp
from time import sleep
from Vaisseau import *
from Planete import *


class Joueur():
    def __init__(self, parent, nom, planetemere, id):
        self.parent = parent
        self.id = id
        self.nom = nom
        self.metal = 100
        self.gaz = 100
        self.bouffe = 100
        self.artefact = 0
        self.planetemere = planetemere
        self.planetemere.proprietaire = self.nom
        self.couleur = None
        self.planetescontrolees = [planetemere]
        self.totalcolons = 10
        self.flotte = []
        self.actions = {"creervaisseauAtt": self.creervaisseauAtt,
                        "creervaisseauSonde": self.creervaisseauSonde,
                        "creervaisseauTrans": self.creervaisseauTrans,
                        "ciblerflotte": self.ciblerflotte,
                        "deplacerVaisseau": self.deplacerVaisseau}

    def creervaisseauAtt(self, planete):
        v = VaisseauGuerre(self.nom,self.planetemere.x + 50, self.planetemere.y,
                           self.parent.parent.idActuel.prochainid())
        print("Vaisseau", v.id)
        self.flotte.append(v)
        
    def creervaisseauSonde(self, planete):
        v = Sonde(self.nom, self.planetemere.x + 50, self.planetemere.y,
                           self.parent.parent.idActuel.prochainid())
        print("Vaisseau", v.id)
        self.flotte.append(v)
        
    def creervaisseauTrans(self, planete):
        v = VaisseauTransport(self.nom, self.planetemere.x + 50, self.planetemere.y,
                           self.parent.parent.idActuel.prochainid())
        print("Vaisseau", v.id)
        self.flotte.append(v)

    def ciblerflotte(self, ids):
        idori, iddesti = ids
        for i in self.flotte:
            if i.id == int(idori):
                for j in self.parent.planetes:
                    if j.id == int(iddesti):
                        i.cible = j
                        print("GOT TARGET")
                        return
                for l in self.parent.joueurs:
                    for k in self.parent.joueurs[l].flotte:
                        if k.id == int(iddesti):
                            i.cible = k
                            print("GOT VAISSEAU")
                            return
                        
    def deplacerVaisseau(self, coord):
        x, y, idori = coord
        for i in self.flotte:
            if i.id == int(idori):
                i.cible = Planete(x, y, -1)
                i.avancer()

    def prochaineaction(self):
        for i in self.flotte:
            if i.cible:
                i.avancer()

    def recoltePlaneteJoueur(self):
        for i in self.planetescontrolees:
            i.recolte(self)



class Modele():
    def __init__(self, parent, joueurs):
        self.parent = parent
        self.joueurs = {}
        #self.joueurs2 = []
        self.actionsafaire = {}
        self.planetes = []
        self.terrain = []
        self.np = len(joueurs)
        self.largeur = 2040 + self.np * 680  # self.parent.vue.root.winfo_screenwidth()
        self.hauteur = 1920 + self.np * 480  # self.parent.vue.root.winfo_screenheight(
        self.creerplanetes(joueurs, self)
        self.creerterrain()

    def creerterrain(self):
        self.terrain = []
        for i in range(10):
            ligne = []
            for j in range(10):
                n = random.randrange(5)
                if n == 0:
                    ligne.append(1)
                else:
                    ligne.append(0)
            self.terrain.append(ligne)

    def creerplanetes(self, joueurs, parent):
        bordure = 10
        self.np = len(joueurs)  # nombre joueurs
        planes = []  # liste des planete meres seulement
        self.hauteur = parent.hauteur
        self.largeur = parent.largeur
        '''
        for i in range(100):
            x = random.randrange(self.largeur - (2 * bordure)) + bordure
            y = random.randrange(self.hauteur - (2 * bordure)) + bordure
            self.planetes.append(Planete(x, y, self.parent.idActuel.prochainid()))
        np = len(joueurs)
        planes = []
        while np:
            p = random.choice(self.planetes)
            if p not in planes:
                planes.append(p)
                self.planetes.remove(p)
                np -= 1
        couleurs = ["red", "blue", "lightgreen", "yellow",
                    "lightblue", "pink", "gold", "purple"]
        for i in joueurs:
            self.joueurs[i] = Joueur(self, i, planes.pop(0), couleurs.pop(0), self.parent.idActuel.prochainid())
        '''
        if self.np == 1:
            planes.append(PlaneteMere(50, 50, self.parent.idActuel.prochainid()))

        if self.np == 2:
            planes.append(PlaneteMere(100, self.hauteur / 2, self.parent.idActuel.prochainid()))
            planes.append(PlaneteMere(self.largeur - 100, self.hauteur / 2, self.parent.idActuel.prochainid()))

        elif self.np == 3:
            planes.append(PlaneteMere(self.largeur / 2, 100, self.parent.idActuel.prochainid()))
            planes.append(PlaneteMere(100, self.hauteur - 100, self.parent.idActuel.prochainid()))
            planes.append(PlaneteMere(self.largeur - 100, self.hauteur - 100, self.parent.idActuel.prochainid()))

        elif self.np == 4:
            planes.append(PlaneteMere(100, 100, self.parent.idActuel.prochainid()))
            planes.append(PlaneteMere(self.largeur - 100, 100, self.parent.idActuel.prochainid()))
            planes.append(PlaneteMere(100, self.hauteur - 100, self.parent.idActuel.prochainid()))
            planes.append(PlaneteMere(100, self.hauteur - 100, self.parent.idActuel.prochainid()))

        elif self.np == 5:
            planes.append(PlaneteMere(self.largeur / 2, 100, self.parent.idActuel.prochainid()))
            planes.append(PlaneteMere(100, self.hauteur / 3.09, self.parent.idActuel.prochainid()))
            planes.append(PlaneteMere(self.largeur - 100, self.hauteur / 3.09, self.parent.idActuel.prochainid()))
            planes.append(PlaneteMere(self.largeur * 0.25, self.hauteur - 100, self.parent.idActuel.prochainid()))
            planes.append(PlaneteMere(self.largeur * 0.75, self.hauteur - 100, self.parent.idActuel.prochainid()))

        elif self.np == 6:
            planes.append(PlaneteMere(self.largeur * 0.24, 50, self.parent.idActuel.prochainid()))
            planes.append(PlaneteMere(50, self.hauteur / 2, self.parent.idActuel.prochainid()))
            planes.append(PlaneteMere(self.largeur * 0.75, 50, self.parent.idActuel.prochainid()))
            planes.append(PlaneteMere(self.largeur - 50, self.hauteur * 0.50, self.parent.idActuel.prochainid()))
            planes.append(PlaneteMere(self.largeur * 0.75, self.hauteur - 50, self.parent.idActuel.prochainid()))
            planes.append(PlaneteMere(self.largeur * 0.24, self.hauteur - 50, self.parent.idActuel.prochainid()))

        for i in joueurs:
            couleurs=['#009ee3','#e5007d','#951b81','#95c11e',
                  '#f39200',"#a40606"] #Je donne la couleur que j'ai choisie a mes planet mes les autre sont aleatoire
            print(i)
            print(self.parent.monnom)
            print(self.parent.vue.varCouleur)
            print(couleurs[0])
            self.joueurs[i]=Joueur(self,i,planes.pop(0), self.parent.idActuel.prochainid())
            compteur=0
            for j in couleurs:
                if(j==self.parent.vue.varCouleur):
                    del couleurs[compteur]
                compteur+=1
            if(i==self.parent.monnom):
                self.joueurs[i].couleur=self.parent.vue.varCouleur
            else:
                self.joueurs[i].couleur=couleurs.pop(0)

        bordure = 15
        '''
        for i in range(341):
             x=random.randrange(self.largeur)
             y=random.randrange(self.hauteur)
             self.planetes.append(Planete(x,y))
        '''
        ##creation du reste de l'univers; on divise en secteur (3 de large plus nb player) par 4 de haut + np
        # ensuite en popule entre X et Y planetes par secteur

        for i in range(3 + self.np):
            for j in range(4 + self.np):
                planetPerParsec = (random.randrange(13, 20))
                planetePlacees = []  # deprecated
                planeteTemp = []  # ajouter liste avec types de planetes par parsec

                for k in range(planetPerParsec):
                    x = random.randrange(680 * i + bordure, 680 * (i + 1))
                    y = random.randrange(480 * j + bordure, 480 * (j + 1))
                    planeteTemp.append(Planete(x, y, self.parent.idActuel.prochainid()))

                # on exclue les doublons a 125 pixels de distance et moins
                compteurDoublon = 0
                for L in planeteTemp:
                    for M in planeteTemp:
                        if ((((L.x - M.x) ** 2 + (L.y - M.y) ** 2) ** 0.5) < 125 and L is not M):
                            planeteTemp.remove(
                                M)  # self.planeteTemp.append(Planete(L.x, L.y, self.parent.idActuel.prochainid()))
                            compteurDoublon += 1

                planetToAdd = 20 - len(planeteTemp)
                if planetToAdd <= 0:
                    pass;
                else:
                    planeteTemp = []
                    for k in range(planetToAdd):
                        x = random.randrange(680 * i + bordure, 680 * (i + 1))
                        y = random.randrange(480 * j + bordure, 480 * (j + 1))
                        planeteTemp.append(Planete(x, y, self.parent.idActuel.prochainid()))

                    # laneteDoublon = planeteTemp
                    compteurDoublon = 0
                    for L in planeteTemp:
                        for M in planeteTemp:
                            if (((L.x - M.x) ** 2 + (L.y - M.y) ** 2) ** 0.5) < 125 and L is not M:
                                planeteTemp.remove(
                                    M)  # self.planeteTemp.append(Planete(L.x, L.y, self.parent.idActuel.prochainid()))
                                compteurDoublon += 1

                # pour fins de statistiques    print(i, "  " , j, "  ", len(planeteTemp))
                for Z in planeteTemp:
                    self.planetes.append(Z)


                    ## pour fins de statistiquess   print(len(self.planetes))

    def prochaineaction(self, cadre):
        if cadre in self.actionsafaire:
            for i in self.actionsafaire[cadre]:
                # print(i)
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
