# -*- coding: utf-8 -*-
# Restart Apache server : httpd -k restart

from Id import *
import random

class Planete():
    def __init__(self,x,y):
        self.id=Id.prochainid()
        self.proprietaire="inconnu"
        self.x=x
        self.y=y
        self.type = random.randrange (1,10)
        self.taille= random.randrange(4, 6)
        self.quantityRess = 800 * self.taille * random.randrange(3,5)  #800 hard coder, devrait vari� en fonction du secteur
        
class PlaneteMere():
    def __init__(self,x,y):
        self.id=Id.prochainid()
        self.proprietaire="inconnu"                     #tagger
        self.x=x
        self.y=y
        self.type = 10
        self.taille= 6
        self.quantityRess = 9000            #hard coded for now
        
        