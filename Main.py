import pygame
import time
import os
from functools import partial
import subprocess
import sys

import json

import random

import codecs#Pour lire l'UTF8 si l'on charge avec json des caractères spéciaux

#Importer les joueurs & mobs
from Joueur import Joueur
from Mobs import Mobs
from Bosse import Bosse

from Confirmer import Quitter

# sources externes du jeu
from src import son
from Charger import *

from projectile import Projectile

#importer les niveau
from Niveau_1 import Niveau_1
from Niveau_2 import Niveau_2
from Niveau_3 import Niveau_3
from Niveau_4 import Niveau_4
from Niveau_5 import Niveau_5

#donné intern au program
from src.objects import (
    Button,
    TextRender,
    Image,
)

FPS = 60
SCREEN_SIZE = (900, 400)
BLOCK_SIZE = (36, 20)

BUTTON_FOLDER = "assets/boutton/"
size=MENU_BOUTTON_SIZE = (118, 57)
PM_BUTTON_SIZE = (50, 50) # Plus & Moins button size

VOLUME_CHANGE = 0.1


def charger_icon():
    icon = pygame.image.load("assets/icon/icon.png")
    return icon

def load_button(
    name: str,
    size: tuple,
    pos: tuple = None,
    func = None
):
    button = pygame.image.load(f"{BUTTON_FOLDER}{name}.png")
    button = pygame.transform.scale(button, size)
    button_rect = button.get_rect()
    button_pressed = pygame.image.load(f"{BUTTON_FOLDER}{name}_press.png")
    button_pressed = pygame.transform.scale(button_pressed, size)

    if pos:
        button_rect.x = pos[0]
        button_rect.y = pos[1]

    if func:
        return button, button_pressed, button_rect, func
    return button, button_pressed, button_rect

def chargercredit():
    file = codecs.open("data/generique.txt", "r", 'utf-8')

    lines = file.readlines()

    poscredit = []
    listcredit = []
    file.close()
    pos = 500
    for line in lines:
        poscredit.append(pos)
        pos += 50
        listcredit.append(line.strip())

    return poscredit, listcredit

class Main:
    def __init__(self, niveau, passer, inventaire_joueur):
        self.ingame = True
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Prevakia")
        pygame.display.set_icon(charger_icon())
        self.screen = pygame.display.set_mode((SCREEN_SIZE))

        self.son = son
        
        self.get_volume = lambda: str(round(self.son.volume * 10))
        self.get_bruitage = lambda: str(round(self.son.bruitage * 10))
        
        self.niveau = niveau#savoir qu'elle est le niveau (change à chaque passage de porte)
        self.pos_carte = [0,0]#changer la position de la carte
        self.lieux = 0 #position dans le niveau
        self.tableau_inf = 0 #savoir sur quelle tableau l'on se trouve

        self.passer = passer #variable qui se met en True quand on passe un niveau pour relancer l'animation
        self.encours = False #varibale pour savoir si l'on passe à un nouveau niveau

        self.game_over = False

        self.pos_souris = 0

        self.police = pygame.font.SysFont("monospace" ,15)#ok ça va
        self.police_titre = pygame.font.SysFont("monospace", 30)

        self.niveau_1 = Niveau_1()
        self.niveau_2 = Niveau_2()
        self.niveau_3 = Niveau_3()
        self.niveau_4 = Niveau_4()
        self.niveau_5 = Niveau_5()

        self.niveau_liste = [self.niveau_1, self.niveau_2, self.niveau_3, self.niveau_4, self.niveau_5]
        self.nivactuel = self.niveau_liste[niveau]#va être la variable qui contiadra le init des niveau

        self.joueur = Joueur(self.nivactuel)
        self.mobs = Mobs(niveau)
        self.bosse = Bosse(self.nivactuel)
        self.combat = False
        self.texte_1 = False
        self.texte_2 = False

        self.partieniv = 50
        self.partieniv_2 = 0

        #Lest textes
        self.nsi = self.police_titre.render("a NSI project production",True,  (255,255,255))
        self.titre = self.police_titre.render("Prevakia",True,  (255,255,255))
        self.generique_intro_1 = self.police_titre.render("Crée par : ",True,  (255,255,255))
        self.generique_intro_2 = self.police_titre.render("Joao Toe",True,  (255,255,255))
        self.generique_intro_3 = self.police_titre.render("Vivien Nicolas",True,  (255,255,255))
        self.generique_intro_4 = self.police_titre.render("Elouan Dhennin Lombardot",True,  (255,255,255))

        self.chapitre = [self.police_titre.render("CHAPTER 1 : Where is she",True,  (255,255,255)),
                         self.police_titre.render("CHAPTER 2 : Between light",True,  (255,255,255)),
                         self.police_titre.render("CHAPTER 3 : Shutdown",True,  (255,255,255)),
                         self.police_titre.render("CHAPTER 4 : Close to the edge",True,  (255,255,255)),
                         self.police_titre.render("CHAPTER 5 : Careful with that axe",True,  (255,255,255)),]

        self.texte_game_over = self.police_titre.render("Appuyer sur espace",True,  (0,0,0))

        self.dialogue_eugene =[self.police.render("Où on t'il mis ma putain de hache", True, (255,255,255)),
                               self.police.render("une ficelle ? Mmmmh", True, (255,255,255)),
                               self.police.render("La voilà...", True, (255,255,255))]
                               
        self.dialogue_bosse = [self.police.render("Jamais tu n'aura cette Hache Eugène !", True, (255,255,255)),
                               self.police.render("Viens m'affronter, si tu en es capable . . .", True, (255,255,255)),
                               self.police.render("Attention avec cette hâche Eugène !!!", True, (255,255,255))]
        
        #charger les blocks
        self.fond_plan_fond, self.fond_plan_1, self.game_over_fond, self.secret_img, self.cache_fond_plan_fond, self.cache_fond_plan_1, self.menu_echap_fond, self.classe = charger_fond()
        self.cube , self.pente, self.porte, self.support, self.echelle, self.munition, self.cube_bloquer, self.barille, self.pente_2, self.pente_3, self.bois, self.bois_broken = charger_block()
        self.cle, self.porte_fermer, self.porte_ouverte, self.grappin, self.hache, self.generateur_on, self.generateur_off, self.lumiere, self.flux_lumiere, self.cache_flux_lumiere, self.bouclier_on, self.bouclier_off, self.banniere = charger_item()
        
        self.option_titre = [self.police.render("Musique", True, (255,255,255)),
                             self.police.render("Effet Sonore", True, (255,255,255)),
                             self.police.render(self.get_volume(),True, (255,255,255)),
                             self.police.render(self.get_bruitage(),True, (255,255,255))]
        
        self.option_bouttons = [
            load_button("quitter", size=MENU_BOUTTON_SIZE, pos=(420, 320), func=lambda:self.quitter(False)),
            # volume
            load_button("plus", size=PM_BUTTON_SIZE, pos=(300, 180), func=partial(self.set_volume, +VOLUME_CHANGE)),
            load_button("moins", size=PM_BUTTON_SIZE, pos=(140, 180), func=partial(self.set_volume, -VOLUME_CHANGE)),
            # bruitage
            load_button("plus", size=PM_BUTTON_SIZE, pos=(300, 280), func=partial(self.set_bruitage, +VOLUME_CHANGE)),
            load_button("moins", size=PM_BUTTON_SIZE, pos=(140, 280), func=partial(self.set_bruitage, -VOLUME_CHANGE)),

            load_button("sauver", size=MENU_BOUTTON_SIZE, pos=(420, 240), func=self.sauvgarder),
            load_button("charger", size=MENU_BOUTTON_SIZE, pos=(420, 160), func=self.charger_jeu)
            ]
    
        self.secret = False
        self.secret_2 = False

        self.joueur.inventaire = inventaire_joueur
        
        self.items = [] #ici, il va enregistrer tout les item d'une carte pour pouvoir les associer avec les autres
            #objets

        self.cle_id = [None,self.porte_1,self.porte_2, self.porte_3, self.porte_4, "quitter"]#ID 1: porte 1

        self.tampon = 0 #valeur tampon à utiliser avec modération (c'est qui modération ?)

        self.echap_menu = False #menu qui s'ouvre quand on clique sur echap

        #générique
        self.font = pygame.font.SysFont("monospace", 20)
        self.poscredit, self.listcredit = chargercredit()
        self.creditderoul = False
        self.generique = False

        self.credit_menu_elements = [
            (self.fond_plan_fond, (0, 0)),
            ]
        x = 150
        for i in range(len(self.listcredit)):
            self.credit_menu_elements.append(self.text_font("", pos=(300, x)))
            x+=50
        self.elements = self.credit_menu_elements
        
        self.sr420 = pygame.image.load("assets/fond/420.png")
        
        self.knockback = False
        
    def text_font(self, text: str, size: int = 1, color: tuple = (255, 255, 255), pos: tuple = (0, 0)):
        text = self.font.render(str(text), size, color)
        rect = text.get_rect()
        rect.center = pos
        return text, rect
    
    def credit(self):
        
        #panneau de la cryptanalyse
        
        self.elements = self.credit_menu_elements
        
        self.creditderoul = True

    def update_elements(self):
        for surface, rect in self.elements:
            self.screen.blit(surface, rect)
        
    def set_volume(self, vol: float):
        if son.volume + vol < 0 or son.volume + vol > 1:
            return

        self.son.volume = round(son.volume + vol, 1)
        pygame.mixer.music.set_volume(son.volume)

        # changer le niveau du son pour les son, pas que pour la musique
        self.option_titre[2] = self.police.render(self.get_volume(),True, (255,255,255))

    def set_bruitage(self, vol: float):
        if son.bruitage + vol < 0 or son.bruitage + vol > 1:
            return

        self.son.bruitage = round(son.bruitage + vol, 1)
        self.son.menu.set_volume(son.bruitage)

        # changer le niveau du son pour les son, pas que pour la musique
        self.option_titre[3] = self.police.render(self.get_bruitage(),True, (255,255,255))

    def save_config(self):
        # sauver la valeur
        self.son.data["volumeMusic"] = son.volume
        self.son.data["volumeEffect"] = son.bruitage
        json.dump(son.data, open("data/jeu.json", "w"))
        
    def actualiser(self):
        
        #système de detection des ennemis
        self.mobs.ojectif = self.joueur.pos[0]
        for i in range (len(self.mobs.pos_debut)):
            if self.mobs.statut[i] == 0 and self.joueur.pos[1] > self.mobs.pos[i][1] and self.joueur.pos[1] < self.mobs.pos[i][1]+47 and self.joueur.pos[0] > self.mobs.pos[i][0] and self.joueur.pos[0] < self.mobs.pos[i][0]+self.mobs.pivote_2[self.mobs.statut[i]]:
                self.mobs.etat[i] = True
                self.mobs.dernier_pos[0] = self.joueur.pos[0]
                
            elif self.mobs.statut[i] == 1 and self.joueur.pos[1] > self.mobs.pos[i][1] and self.joueur.pos[1] < self.mobs.pos[i][1]+47 and self.joueur.pos[0] > self.mobs.pos[i][0]-self.mobs.pivote_2[self.mobs.statut[i]] and self.joueur.pos[0] < self.mobs.pos[i][0]: 
                self.mobs.etat[i] = True
                self.mobs.dernier_pos[0] = self.joueur.pos[0]
                
            elif self.mobs.pos[i][0] == self.mobs.dernier_pos[0]:
                self.mobs.etat[i] = False

            if self.mobs.pos[i][0] < self.joueur.pos[0]+34 and self.mobs.pos[i][0]+47 > self.joueur.pos[0] and self.mobs.pos[i][1] < self.joueur.pos[1]+34 and self.mobs.pos[i][1]+47 > self.joueur.pos[1]:
                self.game_over = True
                
                

        #système de récupération des items
        for i, item in enumerate(self.nivactuel.pos_items):
            if item[4] == True:
                if item[2] ==  1 and item[0] < self.joueur.pos[0]+34 and item[0]+47 > self.joueur.pos[0] and item[1] < self.joueur.pos[1]+34 and item[1]+47 > self.joueur.pos[1]:
                    item[4] = False
                    self.placer_dans_inventaire(i)

                #grappin
                elif item[2] ==  4 and item[0] < self.joueur.pos[0]+34 and item[0]+47 > self.joueur.pos[0] and item[1] < self.joueur.pos[1]+34 and item[1]+47 > self.joueur.pos[1]:
                    item[4] = False
                    self.placer_dans_inventaire(i)
                    self.joueur.grappin_recu = True

                #hache
                elif item[2] ==  5 and item[0] < self.joueur.pos[0]+34 and item[0]+47 > self.joueur.pos[0] and item[1] < self.joueur.pos[1]+34 and item[1]+47 > self.joueur.pos[1]:
                    item[4] = False
                    self.placer_dans_inventaire(i)
                    self.joueur.hache_recu = True

                #générateur
                elif item[2] ==  6 and item[0]+100 > self.joueur.pos[0] and item[0] < self.joueur.pos[0] and item[1] < self.joueur.pos[1]+34 and item[1]+47 > self.joueur.pos[1]:
                    item[4] = False
                    self.nivactuel.eteindre -= 1

                #bouclier
                elif item[2] ==  10 and item[0]+100 > self.joueur.pos[0] and item[0] < self.joueur.pos[0] and item[1] < self.joueur.pos[1]+34 and item[1]+47 > self.joueur.pos[1]:
                    item[4] = False
                    print("ok")
                    self.nivactuel.bouclier = False

                #lock des portes
                elif item[2] ==  2 and item[0] < self.joueur.pos[0]+34 and item[0]+47 > self.joueur.pos[0] and item[1] < self.joueur.pos[1]+34 and item[1]+47 > self.joueur.pos[1]:
                    if item[3] in self.joueur.inventaire:
                        if self.cle_id[item[3]] == "quitter":
                            self.quitter(False)
                        else:
                            executer = self.cle_id[item[3]]
                            item[4] = False
                            self.retirer_de_inventaire(i, item)
                            
                            executer()
                #lumière
                
                elif item[2] ==  9 and self.nivactuel.eteindre != 0 and item[0] < self.joueur.pos[0]-30 and item[0]+47 > self.joueur.pos[0] and item[1] < self.joueur.pos[1]+34 and item[1]+400 > self.joueur.pos[1]:
                    self.game_over = True
                        
                            
        self.monde()
        self.posSouris = pygame.mouse.get_pos()

        self.screen.blit(self.joueur.player[self.joueur.animact][self.joueur.animp], (self.joueur.pos[0]-15,self.joueur.pos[1]-30))

        #tomber dans le vide
        if self.joueur.pos[1] > 410:
            self.game_over = True

        if self.joueur.pos[0] > 324 and self.joueur.pos[0] < 388 and self.joueur.pos[1] > 300 and self.joueur.pos[1] < 330 and self.niveau == 4:
            self.secret_2 = True
        else:
            self.secret_2 = False
            
        if self.niveau == 4 and self.bosse.vie != 0:#dernier niveau avec le bosse
                
            self.screen.blit(self.bosse.image[self.bosse.bosseanimact][self.bosse.bosseanim], (self.bosse.pos[0],self.bosse.pos[1]-2))
            for projectile in self.bosse.all_projectiles:
                projectile.move()

            self.bosse.all_projectiles.draw(self.screen)
            self.bosse_action()

            for sprite in self.bosse.all_projectiles:#si un bullets touche le joueur
                if sprite.rect.x > self.joueur.pos[0] and sprite.rect.x < self.joueur.pos[0]+64 and sprite.rect.y < self.joueur.pos[1]+32 and sprite.rect.y > self.joueur.pos[1]-32:
                    sprite.kill()
                    self.joueur.vie -= 1
                    if self.joueur.vie == 0:
                        self.game_over = True
                
        else:
            self.bosse.pos = [0,0]
        
        for i in range(len(self.mobs.pos_debut)):
            if self.mobs.pos[i][0] <= 0 or self.mobs.pos[i][0] >= 900:
                pass
            else:
                self.screen.blit(self.mobs.image_detection[i], (self.mobs.pos[i][0]+self.mobs.pivote[self.mobs.statut[i]], self.mobs.pos[i][1]))
                if self.mobs.mobanimact == 2 or self.mobs.mobanimact == 3:
                    self.screen.blit(self.mobs.image_mobs[i][self.mobs.mobanimact][self.mobs.mobanim], (self.mobs.pos[i][0], self.mobs.pos[i][1]-54))
                else:
                    self.screen.blit(self.mobs.image_mobs[i][self.mobs.mobanimact][self.mobs.mobanim], (self.mobs.pos[i][0], self.mobs.pos[i][1]-24))

        if self.bosse.vie == 0 and self.joueur.longniv == 1800 and self.generique == False:
            self.credit()
            self.update_elements()   
        
        self.fpsText = self.police.render(f"{int(self.clock.get_fps())} FPS",True,  (0,0,0))
        self.screen.blit(self.fpsText, [60, 100])

        #game over
        if self.game_over == True:
            i = 250
            while self.encours != True:
                self.screen.blit(self.game_over_fond, (0,0))
                self.fondu_entrer(i, self.texte_game_over, 450, 300)
                self.boucle_evenement()
                pygame.display.flip()
                i -= 1
                if i == 0:
                    i = 250
        
        pygame.display.flip()
        self.clock.tick(FPS)


    def bosse_action(self):
        self.screen.blit(self.bosse.image[self.bosse.bosseanimact][self.bosse.bosseanim], (self.bosse.rect[0],self.bosse.rect[1]-2))
        self.bosse.all_projectiles.update()
        self.bosse.all_projectiles.draw(self.screen)
        #faire la première annimation du bosse
        if self.joueur.longniv == 900:
            if self.bosse.pos[0] < 900 and self.bosse.longniv == 900:
                if self.texte_1 == False:
                    self.screen.blit(self.dialogue_bosse[0], (450,200))
                    
                if self.joueur.pos > [388,44]:
                    self.bosse.phase_0()
                    self.texte_1 = True

                    if self.texte_2 == False:
                        self.screen.blit(self.dialogue_bosse[1], (400,300))
                    if self.joueur.pos[0] > 700:
                        self.texte_2 = True
                
        if self.joueur.longniv == 900 and self.joueur.pos >= [802, 344]:
            
            self.bosse.direc[1] = False
            self.bosse.pos = [1350, 215]

        if self.joueur.longniv == 1800 and self.joueur.pos[0] > 250:
            
            self.combat = True
            
            
        if self.combat == True:
            vie_joueur = self.police.render(str(self.joueur.vie), True, (255,255,255))
            vie_bosse = self.police.render(str(self.bosse.vie), True, (255,255,255))
            self.screen.blit(vie_bosse, (556,220))
            self.screen.blit(vie_joueur, (self.joueur.pos[0]-20, self.joueur.pos[1]-42))
            self.bosse.main()
            
            

    def retirer_de_inventaire(self, i, item):
        trouver = False
        y = 0
        while trouver != True:
            if item[3] == self.joueur.inventaire[y]:
                self.joueur.inventaire[y] = 0
                trouver = True
            if y + 1 >= len(self.joueur.inventaire):
                trouver = True
            else:
                y+= 1

    def placer_dans_inventaire(self,i):
        y = 0#trouver une place libre dans l'inventaire
        trouver = False
        while trouver != True:
            if self.joueur.inventaire[y] == 0:
                self.joueur.inventaire[y] = self.nivactuel.pos_items[i][3]
                trouver = True
            y += 1
        trouver = False
                
    def porte_1(self):
        self.sauver_inventaire()
        self.monde()
                            
        pygame.display.flip()
        self.wait(1000)
        self.niveau += 1
        self.__init__(self.niveau, True, self.joueur.inventaire)
        self.nivactuel = self.niveau_2
        self.joueur.niveau = self.niveau_2

    def porte_2(self):
        self.sauver_inventaire()
        self.monde()
                            
        pygame.display.flip()
        self.wait(1000)
        self.niveau += 1
        self.__init__(self.niveau, True, self.joueur.inventaire)
        self.nivactuel = self.niveau_3
        self.joueur.niveau = self.niveau_3

    def porte_3(self):
        self.sauver_inventaire()
        self.monde()
                            
        pygame.display.flip()
        time.sleep(1)
        self.niveau += 1
        self.__init__(self.niveau, True, self.joueur.inventaire)
        self.nivactuel = self.niveau_4
        self.joueur.niveau = self.niveau_4

    def porte_4(self):
        self.sauver_inventaire()
        self.monde()
                            
        pygame.display.flip()
        self.wait(1000)
        self.niveau += 1
        self.__init__(self.niveau, True, self.joueur.inventaire)
        self.nivactuel = self.niveau_5
        self.joueur.niveau = self.niveau_5

    def porte_5(self):
        self.monde()
        self.wait(1000)
        self.joueur.inventaire = [0,0,0,0,0]

        self.blit(self.classe, (0,0))  
        pygame.display.flip()
        
            
    def monde(self):

        if self.encours:
            if self.niveau == 0:
                
                self.nivactuel = self.niveau_1
                self.__init__(0, True, self.joueur.inventaire)
                
            if self.niveau == 1:
            
                self.__init__(1, True, self.joueur.inventaire)
                self.nivactuel = self.niveau_2
                self.joueur.niveau = self.niveau_2

            if self.niveau == 2:
                
                self.__init__(2, True, self.joueur.inventaire)
                self.nivactuel = self.niveau_3
                self.joueur.niveau = self.niveau_3

            if self.niveau == 3:
                
                self.__init__(3, True, self.joueur.inventaire)
                self.nivactuel = self.niveau_4
                self.joueur.niveau = self.niveau_4

            if self.niveau == 4:
                
                self.__init__(4, True, self.joueur.inventaire)
                self.nivactuel = self.niveau_5
                self.joueur.niveau = self.niveau_5

            self.encours = False

        self.screen.blit(self.cache_fond_plan_fond, (0, 0))
        for i in range(len(self.nivactuel.tableau)):
            self.screen.blit(self.cache_fond_plan_1, (self.nivactuel.tableau_move_plan_1[i], 0))#faire bouger le plan 1
        
        if self.nivactuel.mur[round(self.joueur.pos[1]//20)][round((self.joueur.pos[0]-2+self.joueur.longniv)//36)] == 420:
            self.screen.blit(self.sr420, (0,0))
        
        for i in range(len(self.nivactuel.mur)):#poser les blocks
            for y in range(self.partieniv_2,len(self.nivactuel.mur[i])):
        
                
                if self.nivactuel.mur[i][y] == 1:#block
                    self.screen.blit(self.cube, (y*BLOCK_SIZE[0]-self.lieux, i*BLOCK_SIZE[1]))
                elif self.nivactuel.mur[i][y] == 2:#porte ouverte
                    self.screen.blit(self.porte, (y*BLOCK_SIZE[0]-self.lieux, i*BLOCK_SIZE[1]))
                elif self.nivactuel.mur[i][y] == 3:
                    self.screen.blit(self.support, (y*BLOCK_SIZE[0]-self.lieux, i*BLOCK_SIZE[1]))
                elif self.nivactuel.mur[i][y] == 4:
                    self.screen.blit(self.echelle, (y*BLOCK_SIZE[0]-self.lieux, i*BLOCK_SIZE[1]))
                elif self.nivactuel.mur[i][y] == 5:
                    self.screen.blit(self.pente, (y*BLOCK_SIZE[0]-self.lieux, i*BLOCK_SIZE[1]))
                elif self.nivactuel.mur[i][y] == 51:
                    self.screen.blit(self.pente_2, (y*BLOCK_SIZE[0]-self.lieux, i*BLOCK_SIZE[1]))
                elif self.nivactuel.mur[i][y] == 52:
                    self.screen.blit(self.pente_3, (y*BLOCK_SIZE[0]-self.lieux, i*BLOCK_SIZE[1]))
                elif self.nivactuel.mur[i][y] == 6:
                    self.screen.blit(self.cube, (y*BLOCK_SIZE[0]-self.lieux, i*BLOCK_SIZE[1]))
                elif self.nivactuel.mur[i][y] == 8:
                    self.screen.blit(self.cube_bloquer, (y*BLOCK_SIZE[0]-self.lieux, i*BLOCK_SIZE[1]))
                elif self.nivactuel.mur[i][y] == 9:
                    self.screen.blit(self.barille, (y*BLOCK_SIZE[0]-self.lieux, i*BLOCK_SIZE[1]))
                elif self.nivactuel.mur[i][y] == 10:
                    self.screen.blit(self.munition, (y*BLOCK_SIZE[0]-self.lieux, i*BLOCK_SIZE[1]))
                elif self.nivactuel.mur[i][y] == 105:
                    if self.joueur.boisbroken == False:
                        self.screen.blit(self.bois, (y*BLOCK_SIZE[0]-self.lieux, i*BLOCK_SIZE[1]))
                    else:
                        self.screen.blit(self.bois_broken, (y*BLOCK_SIZE[0]-self.lieux, i*BLOCK_SIZE[1]))
                if self.bosse.vie == 0 and self.nivactuel.mur[i][y] == 8 or self.nivactuel.bouclier == False and self.nivactuel.mur[i][y] == 8:
                    self.nivactuel.mur[i][y] = 0                    
        
        if self.joueur.direc[7] == True:     
            self.ligne = pygame.draw.line(self.screen,(255, 255, 100), (self.joueur.pos[0]+30, self.joueur.pos[1]-20), self.joueur.posSouris, width=3)
        

        for i, item in enumerate(self.nivactuel.pos_items):
            if item[4]:
                item_type = item[2]
                if item_type == 1:
                    self.screen.blit(self.cle, (item[0], item[1]))
                elif item_type == 2:
                    self.screen.blit(self.porte_ouverte, (item[0], item[1]))
                elif item_type == 3:
                    pass
                    self.screen.blit(self.porte_fermer, (item[0], item[1]))
                elif item_type == 4:
                    self.screen.blit(self.grappin, (item[0], item[1]))
                elif item_type == 5:
                    self.screen.blit(self.hache, (item[0], item[1]))
                elif item_type == 6:
                    self.screen.blit(self.generateur_on, (item[0], item[1]))
                elif item_type == 7:
                    self.screen.blit(self.generateur_off, (item[0], item[1]))
                elif item_type == 8:
                    self.screen.blit(self.lumiere, (item[0], item[1]))
                elif item_type == 9:
                    if self.nivactuel.eteindre == 0:
                        pass
                    else:
                        self.screen.blit(self.cache_flux_lumiere, (item[0], item[1]))
                elif item_type == 10:
                    self.screen.blit(self.bouclier_on, (item[0], item[1]))
                elif item_type == 11:
                    self.screen.blit(self.bouclier_off, (item[0], item[1]))
                elif item_type == 12:
                    self.screen.blit(self.banniere, (item[0], item[1]))

        if self.secret == True:
            self.screen.blit(self.secret_img, (0,0))
        if self.secret_2 == True:
            self.screen.blit(self.classe, (0,0))
       

    def attaque(self):
        if (self.joueur.pos[0]+64 > self.bosse.pos[0] and self.joueur.pos[0] < self.bosse.pos[0]+64) and self.joueur.direc[9] == False:
            self.bosse.vie -= 1
            self.bosse.cooldown_reload = 250 - self.bosse.vie*5
            self.knockback = True
            
    def kknockback(self):
        if self.knockback == True:
                
            if self.joueur.pos[0] >= 60:
                self.joueur.pos[0] -= 12
            else:
                self.knockback = False
                
            
    def avant(self):
                
        self.partieniv -=25
        self.partieniv_2 -= 25
        if self.tableau_inf+2 <= len(self.nivactuel.tableau):
            self.joueur.pos[0] += 12
            self.tableau_inf += 1
            while self.lieux != self.nivactuel.tableau[self.tableau_inf]:
                for i in range(len(self.nivactuel.tableau)):#faire bouger les arrière plan
                    self.nivactuel.tableau_move_plan_1[i] -= 15
                self.nivactuel.tableau_move_plan_fond -= 10
                self.cache_fond_plan_fond.blit(self.fond_plan_fond, [self.nivactuel.tableau_move_plan_fond, 0])
                self.lieux += 15
                self.joueur.pos[0] -= 15
                self.bosse.pos[0] -= 15
                for i in range(len(self.mobs.pos_debut)):
                    self.mobs.pos[i][0] -= 15
                    self.mobs.pos_debut[i][0] -= 15
                    self.mobs.pos_fin[i][0] -= 15
                for i in range(len(self.nivactuel.pos_items)):
                    self.nivactuel.pos_items[i][0] -= 15
                self.actualiser()

            self.bosse.longniv += 900
            self.mobs.longniv += 900
            self.joueur.longniv += 900
            self.joueur.boisbroken = False

        else:
            pass
        

    def arriere(self):
            
        if self.tableau_inf-1 >= 0:
            self.joueur.pos[0] -= 60
            self.tableau_inf -= 1
            while self.lieux != self.nivactuel.tableau[self.tableau_inf]:
                for i in range(len(self.nivactuel.tableau)):#faire bouger les arrière plan
                    self.nivactuel.tableau_move_plan_1[i] += 15
                self.nivactuel.tableau_move_plan_fond += 10
                self.cache_fond_plan_fond.blit(self.fond_plan_fond, [self.nivactuel.tableau_move_plan_fond, 0])
                self.lieux -= 15
                self.joueur.pos[0] += 15
                self.bosse.pos[0] += 15
                for i in range(len(self.mobs.pos_debut)):
                    self.mobs.pos[i][0] += 15
                    self.mobs.pos_debut[i][0] += 15
                    self.mobs.pos_fin[i][0] += 15
                for i in range(len(self.nivactuel.pos_items)):
                    self.nivactuel.pos_items[i][0] += 15
                self.actualiser()
            
            self.partieniv +=25
            self.partieniv_2 += 25

            self.bosse.longniv -= 900
            self.joueur.longniv -= 900
            self.mobs.longniv -= 900
            self.joueur.boisbroken = False

            
        else:
            pass

    def sauver_inventaire(self):#cela permet de recharger l'ancier inventaire après une mort
        with open("save/inv_tampon.txt", "w") as fichier:
            for stuff in self.joueur.inventaire:
                fichier.write(str(stuff) + "\n")
                
    def charger_inventaire(self):#litéralmement le contraire
        tampon = []
        with open("save/inv_tampon.txt", "r") as fichier:
            lignes = fichier.readlines()
            for ligne in lignes:
                element = ligne.strip()  # Supprimer les caractères de nouvelle ligne
                tampon.append(int(element))  # Convertir en entier et ajouter à la liste
        self.joueur.inventaire = tampon
    def wait(self, temps):
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(temps)
        
    def entrer(self):#annimation du joueur qui rentre dans le niveau
        self.sauver_inventaire()
        alpha = 0
        tampon = 255
        for i in range(100):
            self.screen.fill((0,0,0))
            alpha += 5
            self.fondu_entrer(alpha, self.chapitre[self.niveau], 300, 250)

            self.wait(10)
            pygame.display.flip()
            
        self.wait(2000)

        alpha = 255
        for i in range(100):#fondu du text
            self.screen.fill((0,0,0))
            self.monde()
            
            tampon -= 2.5
            self.monde() 
            s = pygame.Surface(SCREEN_SIZE)
            s.set_alpha(tampon)
            s.fill((0,0,0))
            self.screen.blit(s, (0,0))
               
            self.screen.blit(self.chapitre[self.niveau], (300, 250))
            self.wait(10)
            pygame.display.flip()

        alpha = 255
        for i in range(100):
            self.monde() 
            alpha -= 2.5
            self.fondu_sortie(alpha, self.chapitre[self.niveau], 300+i, 250)

            self.wait(10)
            pygame.display.flip()
            
        self.joueur.pos = [-70,286]
        while self.joueur.pos <= [60, 286]:
            
            self.mobs.grav()# la Gravité
            
            self.joueur.droite = True
            self.joueur.pos[0] += 2
            
            self.joueur.animation()
            self.actualiser()
        self.joueur.droite = False
            


    def fondu_entrer(self, alpha, text, x, y):
        text.set_alpha(alpha)
        self.screen.blit(text, (x, y))
            
            
    def fondu_sortie(self, alpha, text,x ,y):
        text.set_alpha(alpha)
        self.screen.blit(text, (x, y))

    ########################################################################### INTRO
    def intro(self):#crée un fondu quand on lance le jeu
        self.son.song_intro()
        tampon = 255
        pygame.display.flip()
        self.wait(2000)

        alpha = 0
        for i in range(100):#fondu du text
            self.screen.fill((0,0,0))
            alpha += 2.5
            self.fondu_entrer(alpha, self.nsi, 240, 180)
            self.wait(10)
            pygame.display.flip()
        self.wait(3000)
        for i in range(100):#fondu du text
            self.screen.fill((0,0,0))
            alpha -= 2.5
            self.fondu_sortie(alpha, self.nsi, 240, 180)
            self.wait(10)
            pygame.display.flip()

        self.wait(2000)
        alpha = 0   
        for i in range(50):#fondu du text
            self.screen.fill((0,0,0))
            alpha += 5
            self.fondu_entrer(alpha, self.generique_intro_1, 200, 120)
            self.fondu_entrer(alpha, self.generique_intro_2, 400, 160)
            self.fondu_entrer(alpha, self.generique_intro_3, 400, 190)
            self.fondu_entrer(alpha, self.generique_intro_4, 400, 220)

            self.wait(10)
            pygame.display.flip()

        self.wait(2000)
        alpha = 255
        for i in range(50):#fondu du text
            self.screen.fill((0,0,0))
            alpha -= 5
            self.fondu_sortie(alpha, self.generique_intro_1, 200, 120)
            self.fondu_sortie(alpha, self.generique_intro_2, 400, 160)
            self.fondu_sortie(alpha, self.generique_intro_3, 400, 190)
            self.fondu_sortie(alpha, self.generique_intro_4, 400, 220)

            self.wait(10)
            pygame.display.flip()
            
        self.wait(2000)

        alpha = 0
        for i in range(50):#fondu du text
            self.screen.fill((0,0,0))
            alpha += 5
            self.fondu_entrer(alpha, self.titre, 370, 180)
            self.wait(10)
            pygame.display.flip()
        self.wait(5000)
        for i in range(100):#fondu du text
            self.screen.fill((0,0,0))
            alpha -= 5
            self.fondu_sortie(alpha, self.titre, 370, 180)
            self.wait(10)
            pygame.display.flip()
            
        self.wait(2000)

    #############################################################################
    def charger_jeu(self):
        self.quitter(True)
        
    def sauvgarder(self):
        joueur = {
            "niveau": self.niveau,
            "inventaire":self.joueur.inventaire
            }
        sauver = json.dumps(joueur)
        fichier = open("save/slot_1.json", "w")
        fichier.write(sauver)
        fichier.close()

    def menu(self):
        self.buttons = self.option_bouttons
        self.screen.blit(self.menu_echap_fond, (125,0))
        self.screen.blit(self.titre, (175,50))
        
        for i in range(len(self.option_titre)):
            if i == 2 or i == 3:
                self.screen.blit(self.option_titre[i], (240, (i*100)-5))
            else:
                self.screen.blit(self.option_titre[i], (175, (i*100)+150))
            
        for button, button_pressed, button_rect, func in self.buttons:
            self.screen.blit(button, button_rect)
            
        pygame.display.flip()
        
    def check_buttons(self):
        for button, button_pressed, button_rect, func in self.buttons:
            self.screen.blit(button, button_rect)
            # verifier si la souris est sur un bouton (onHover)
            if button_rect.collidepoint(self.pos_souris):
                self.screen.blit(button_pressed, button_rect)
            
                self.son.menu.play()
                pygame.display.flip() # actualiser
                self.wait(100)
                func()
        
    def boucle_evenement(self):
        for event in pygame.event.get():
                    
                if event.type == pygame.QUIT:
                    
                    self.quitter(False)

                elif event.type==pygame.KEYDOWN:
                    
                    if event.key == pygame.K_q:
                        self.joueur.gauche = True
                        self.joueur.direc[0]=True
                        self.joueur.direc[1]=False

                    if event.key == pygame.K_d:
                        self.joueur.droite = True
                        self.joueur.direc[0]=False
                        self.joueur.direc[1]=True

                    if event.key == pygame.K_z: 
                        self.joueur.haut = True

                    if event.key == pygame.K_s:
                        self.joueur.bas = True
                        if self.joueur.direc[8] == True:                          
                            self.joueur.grap = False
                            self.joueur.direc[6] = False
                            self.joueur.direc[7] = False
                            self.joueur.animp = 0
                            self.animcp = 0

                    if event.key == pygame.K_a and self.joueur.pos[1] == 45 and (self.joueur.pos[0] >= 250 or self.joueur.pos[0] <= 300)  and self.niveau == 0:
                        self.secret = True
                    else:
                        self.secret = False

                    if event.key == pygame.K_a and self.joueur.pos[0] == 829 and self.joueur.pos[1] == 344 and self.niveau == 2 and self.joueur.longniv == 900:
                        self.son.song_2()
                        
                    if event.key == pygame.K_SPACE and self.game_over == True:
                        self.charger_inventaire()
                        self.encours = True

                    if event.key == pygame.K_ESCAPE:
                        self.echap_menu = not self.echap_menu
                        if self.echap_menu == True:
                            s = pygame.Surface(SCREEN_SIZE)
                            s.set_alpha(175)
                            s.fill((0,0,0))
                            self.screen.blit(s, (0,0))
                            self.menu()
                        else:
                            self.save_config()

                    if event.key == pygame.K_c:
                        print(self.joueur.pos)

                elif event.type == pygame.KEYUP:

                    if event.key == pygame.K_q:
                        self.joueur.gauche = False

                    if event.key == pygame.K_d:
                        self.joueur.droite = False

                    if event.key == pygame.K_z:
                        self.joueur.haut = False

                    if event.key == pygame.K_s:
                        self.joueur.bas = False

                if pygame.mouse.get_pressed()[0] and self.echap_menu == True:
                    # click droit donc on check si un bouton est cliquer
                    self.check_buttons()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 :#clique gauche
                        for i in range(len(self.joueur.inventaire)):
                            if self.joueur.inventaire[i] == 11:
                                if not self.nivactuel.mur[round((self.joueur.posSouris[1])//20)][round((self.joueur.posSouris[0]+self.joueur.longniv)//36)] == 3 or  self.joueur.pos[0] < self.joueur.posSouris[0]-50 or self.joueur.pos[0] > self.joueur.posSouris[0]+50:
                                    pass
                                else:
                                    if self.joueur.grap == False and not self.joueur.direc[2] == True:                          
                                        self.joueur.direc[6] = True
                                        self.joueur.direc[7] = False
                                        self.joueur.grap = True
                                        self.joueur.animp = 0
                                    else:
                                        self.joueur.grap = False
                                        self.joueur.direc[6] = False
                                        self.joueur.direc[7] = False
                                        self.joueur.animp = 0
                                        self.animcp = 0
                                break

                        if self.nivactuel.mur[round((self.joueur.posSouris[1])//20)][round((self.joueur.posSouris[0]+self.joueur.longniv)//36)] == 105 and (self.nivactuel.mur[round((self.joueur.pos[1])//20)][round((self.joueur.pos[0]+self.joueur.longniv+45)//36)] == 105 or self.nivactuel.mur[round((self.joueur.pos[1])//20)][round((self.joueur.pos[0]+self.joueur.longniv-10)//36)] == 105):
                            self.joueur.direc[9] = True
                            self.joueur.animp = 0
                            self.joueur.animcp = 0
                            self.joueur.boisbroken = True 
                    
                    
                    if (event.button == 3 and self.joueur.hache_recu == True) and not self.joueur.direc[9] == True and not self.joueur.grap == True:#clique droit

                            self.attaque()
                            self.joueur.direc[9] = True
                            self.joueur.animp = 0
                            self.joueur.animcp = 0
                             
    def quitter(self, load):
        #resultat = subprocess.Popen(["python3", "Confirmer.py"])
        #resultat.wait()
        #print(resultat)
        #if resultat == True:
        self.save_config()
        self.sauver_inventaire()
        self.ingame = False

        if load == True:
            fileObject = open("save/slot_1.json", "r")
            jsonContent = fileObject.read()
            obj_python = json.loads(jsonContent)

            self.__init__(obj_python["niveau"],True, obj_python["inventaire"])
    
        #else:
        #pass

    def new_game(self):
        self.intro()
        self.boucle_jeu()
    def boucle_jeu(self):
        self.son.song_game()
        while self.ingame:
            if self.creditderoul == True:
                
                ############################### défilement du générique
                taille = 80
                for i in range(1, len(self.credit_menu_elements)-1):
                    
                    if self.poscredit[i] >= 0 or self.poscredit[i] <= 400:
                        self.elements[i] = self.text_font(self.listcredit[i], taille,(255,255,255), pos=(300,self.poscredit[i]))
                    if self.poscredit[-1] >= 150:
                        self.poscredit[i] -= 1
                    else:
                        self.poscredit[i] -= 0.5

                        
                    if self.poscredit[-1] < -50:
                        
                        self.generique = True
                        self.creditderoul = False
                    taille = 20

                        
            self.pos_souris = pygame.mouse.get_pos()

            if self.echap_menu == True:
                    self.menu()
            
            if self.passer == True:#quand on passe un niveau, refaire l'animation d'entrer
                self.cache_fond_plan_1.fill((0, 0, 0, 0))
                self.cache_flux_lumiere.fill((0, 0, 0, 0))
                self.cache_fond_plan_fond.blit(self.fond_plan_fond, [self.nivactuel.tableau_move_plan_fond, 0])
                for i in range(len(self.nivactuel.tableau)):
                    self.cache_fond_plan_1.blit(self.fond_plan_1, [self.nivactuel.tableau_move_plan_1[i], 0])#faire bouger le plan 1
                #charger le fond lumineux
                self.cache_flux_lumiere.blit(self.flux_lumiere, [self.joueur.longniv, 1])
    
                self.entrer()
                self.passer = False
                

            if self.echap_menu != True or self.game_over == True:
                self.joueur.bouger()
                self.joueur.animation()
                self.mobs.bouger()
                self.mobs.animmob()
                self.bosse.animbosse()

                self.joueur.collisions()
    
                self.joueur.grav()# la Gravité
                self.mobs.grav()# la Gravité
                self.bosse.grav()
                self.kknockback()
            
                self.actualiser()
 
            if self.joueur.pos[0] >= 900:#faire un défilement de l'écran quand on arrive sur un autre tableau
                self.avant()
                        
            elif self.lieux >= 1 and self.joueur.pos[0] <= 0:
                self.arriere()
            
            self.boucle_evenement()
            
            
            for i in range(len(self.joueur.inventaire)):
                if self.joueur.inventaire[i] == 11:
                    self.joueur.grappin()###fonction grapin
                    self.joueur.collisiongrap()
                    break
                        

