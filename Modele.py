import random
from helper import Helper as hlp
from Vaisseau import *
from Planete import *
from ArtificialDumbness import *


class Joueur():
    def __init__(self, parent, nom, planetemere, couleur, id):
        self.parent = parent
        self.id = id
        self.nom = nom
        self.metal = 100
        self.gaz = 100
        self.bouffe = 100
        self.artefact = 0
        self.planetemere = planetemere
        self.planetemere.proprietaire = self.nom
        self.couleur = couleur
        self.planetescontrolees = [planetemere]
        self.totalcolons = 10
        self.flotte = []
        self.actions = {"creervaisseau": self.creervaisseau,
                        "ciblerflotte": self.ciblerflotte,
                        "deplacerVaisseau": self.deplacerVaisseau}


    def creervaisseau(self, planete):
        v = VaisseauGuerre(self.nom, self.planetemere.x + 10, self.planetemere.y,
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
        self.AI = AI(self)
        self.joueurs = {}
        self.joueurs2 = []
        self.actionsafaire = {}
        self.planetes = []
        self.terrain = []
        self.np = len(joueurs)
        self.largeur = 2040 + self.np * 680  # self.parent.vue.root.winfo_screenwidth()
        self.hauteur = 1920 + self.np * 480  # self.parent.vue.root.winfo_screenheight()
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
        planes = []    #liste des planete meres seulement
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

        couleurs = ["red", "blue", "lightgreen", "yellow",
                    "lightblue", "pink", "gold", "purple"]

        for i in joueurs:
            self.joueurs[i] = Joueur(self, i, planes.pop(0), couleurs.pop(0), self.parent.idActuel.prochainid())

        # self.joueurs[self.np +1] = Joueur(self, self.np + 1, self.AI.planetecontrolees, "orange", self.parent.idActuel.prochainid)
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
                planetePlacees = []                                         #deprecated
                planeteTemp = []  # ajouter liste avec types de planetes par parsec

                for k in range(planetPerParsec):


                    x = random.randrange(680 * i + bordure, 680 * (i + 1))
                    y = random.randrange(480 * j + bordure, 480 * (j + 1))
                    planeteTemp.append(Planete(x, y, self.parent.idActuel.prochainid()))

                #on exclue les doublons a 125 'pixels' de distance et moins
                compteurDoublon = 0
                for L in planeteTemp:
                    for M in planeteTemp:
                        if ((((L.x - M.x) ** 2 + (L.y - M.y) ** 2) ** 0.5) < 125 and L is not M):
                            planeteTemp.remove(M)           #self.planeteTemp.append(Planete(L.x, L.y, self.parent.idActuel.prochainid()))
                            compteurDoublon +=1
                    for N in planes:
                        if (((L.x - N.x) ** 2 + (L.y - N.y) ** 2) ** 0.5) < 175:
                            planeteTemp.remove(L)
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

                    #DEBUG deprecated planeteDoublon = planeteTemp
                    compteurDoublon = 0
                    for L in planeteTemp:
                        for M in planeteTemp:
                            if (((L.x - M.x) ** 2 + (L.y - M.y) ** 2) ** 0.5) < 125 and L is not M:
                                planeteTemp.remove(M)                            # self.planeteTemp.append(Planete(L.x, L.y, self.parent.idActuel.prochainid()))
                                compteurDoublon += 1
                        for N in planes:                                        #liste d'exclusion distincte pour planetes meres
                            if (((L.x - N.x) ** 2 + (L.y - N.y) ** 2) ** 0.5) < 175:
                                planeteTemp.remove(L)
                                compteurDoublon += 1
                                #DEBUG pour fins de statistiques  :  print(i, "  " , j, "  ", len(planeteTemp))
                for Z in planeteTemp:
                    self.planetes.append(Z)


        ##DEBUG  pour fins de statistiquess :  print(len(self.planetes))

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

class AI():
    def __init__(self, parent):
        self.nom = "HAL"
        self.parent = parent
        self.grandPa = parent.parent
        self.id = self.grandPa.idActuel.prochainid()

        self.shipYardValue = 4                      ##variable de base d'evaluation de la valeur des planete ship building
        self.planetecontrolees = []
                            #parent.largeur / 2, parent.hauteur /2, parent.idActuel.prochainid()))
        self.planetemere = PlaneteMere(525, 325, self.grandPa.idActuel.prochainid())
        self.planetemere.proprietaire = self.nom
        self.couleur = "blue"
        self.planetecontrolees.append(self.planetemere)
        self.threatShips = []
        self.threatMinDistance = 600
        self.threatenedPlanet = [[]]
        self.flotteAI = []
        self.gestionnaireAI(self, self.grandPa)
        self.player = Joueur(self, self.nom, self.planetemere, self.couleur, self.id)
        self.actions = {"creervaisseauAI": self.player.creervaisseauAI,
                        "ciblerflotte": self.player.ciblerflotte,
                        "deplacerVaisseau": self.player.deplacerVaisseau}


    def gestionnaireAI(self, parent, grandPa):
        for i in range (5):
            grandPa.creervaisseauAI()

    def creervaisseauAI(self, parent):
        for i in range (2):
            #batirVaisseau(parent.planetecontrolees.index(0), grandPa)
            v = VaisseauGuerre(self.nom, self.planetemere.x + 10, self.planetemere.y,
                               self.parent.parent.idActuel.prochainid())
            print("Vaisseau AI bati", v.id)
            self.flotteAI.append(v)
            #grandPa.creervaisseauAI()
        '''
        self.mod1 = grandPapa
        for j in self.planeteControlees:
            planetthreatened = False
            parent.threatShips = []
            for i in self.mod1.joueurs.flotte:
                     #pour chaque vaisseau joueur on evalue la menace (proximite et direction) vis-a-vis chaque planete AI
                if (((j.x - i.x) ** 2 + (j.y - i.y) ** 2) ** 0.5) < self.threatMinDistance \
                        or (((j.x - i.cible.x) ** 2 + (j.y - i.cible.y) ** 2) ** 0.5) < self.threatMinDistance /2:
                    parent.threatShips.append(i)
                    planetThreatened = True
        if planetthreatened:
            parent.threatenedPlanet.append(j)
            parent.threatenedPlanet[j].append(parent.threatShips)
        '''

    def batirVaisseau(self, planete, grandPapa):
        v = VaisseauGuerre(self.nom, self.planetemere.x + 10, self.planetemere.y,
                           self.parent.parent.idActuel.prochainid())
        print("Vaisseau AI bati", v.id)
        self.flotteAI.append(v)
        grandPapa.creervaisseau()





    def analyseMenaces(self):
        pass
       # for i in visibleShips

