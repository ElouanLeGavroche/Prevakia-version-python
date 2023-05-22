import pygame
import random

from projectile import Projectile
from Joueur import Joueur

from Niveau_5 import Niveau_5

class Bosse(pygame.sprite.Sprite):
    def __init__(self, niveau):
        super(). __init__()

        self.image = [
            
            [pygame.image.load("assets/joueur/bosse/bosse_g.png"),
             pygame.image.load("assets/joueur/bosse/bosse_g.png"),
             pygame.image.load("assets/joueur/bosse/bosse_g.png"),
             pygame.image.load("assets/joueur/bosse/bosse_g2.png"),
             pygame.image.load("assets/joueur/bosse/bosse_g2.png"),
             pygame.image.load("assets/joueur/bosse/bosse_g.png"),],
            
            [pygame.image.load("assets/joueur/bosse/bosse_d.png"),
             pygame.image.load("assets/joueur/bosse/bosse_d1.png"),
             pygame.image.load("assets/joueur/bosse/bosse_d.png"),
             pygame.image.load("assets/joueur/bosse/bosse_d.png"),
             pygame.image.load("assets/joueur/bosse/bosse_d2.png"),
             pygame.image.load("assets/joueur/bosse/bosse_d.png"),],
            
            [pygame.image.load("assets/joueur/bosse/bosse_g.png"),
             pygame.image.load("assets/joueur/bosse/bosse_gt.png"),
             pygame.image.load("assets/joueur/bosse/bosse_g.png"),
             pygame.image.load("assets/joueur/bosse/bosse_gt.png"),
             pygame.image.load("assets/joueur/bosse/bosse_g.png"),
             pygame.image.load("assets/joueur/bosse/bosse_g.png"),],
            
            [pygame.image.load("assets/joueur/bosse/bosse_gt2.png"),
             pygame.image.load("assets/joueur/bosse/bosse_gt2.png"),
             pygame.image.load("assets/joueur/bosse/bosse_gt3.png"),
             pygame.image.load("assets/joueur/bosse/bosse_gt3.png"),
             pygame.image.load("assets/joueur/bosse/bosse_gt3.png"),
             pygame.image.load("assets/joueur/bosse/bosse_gt2.png"),]
                      
                      
                      ]
        
        self.rect = self.image[0][0].get_rect()

        self.pos = [1400,250]

        self.joueur = Joueur(4)
        
        self.rect.x = 1400
        self.rect.y = 250

        self.vie = 6
        
        self.last = pygame.time.get_ticks()
        
        self.cooldown_projectile = 400  # Durée du cooldown en millisecondes
        self.last_projectile_time = 0  # Temps du dernier tir de projectile

        self.cooldown_reload = 250
        self.last_reload_time = 0
        
        self.phase_1_go = False
        self.phase_2_go = True
        self.shoot = 0
        
        self.vitesse = 1

        self.longniv= 0
        self.niveau = niveau
        
        self.rotation = False

        self.projectile = Projectile(self)
        self.all_projectiles = pygame.sprite.Group()
        
        self.direc = [
            
            True, #idle 
            False,  #phase_0
            False, #phase_1
            False #phase_2
            
            ]
        
        self.bosseanim = 0
        
        self.bosseanicp = 0
        
        self.bosseanimact = 0

    def main(self):
        
        self.direc[0] = True
        
        if self.phase_2_go == True:
            self.phase_2()
        elif self.phase_1_go == True:
            self.phase_1()
        
    def phase_0(self):
        if self.pos[0] <= 1200:
            self.pos[0] += 4
            self.direc[1] = True

            
    def phase_1(self):
        
        if self.shoot != 0:
            self.direc[2] = True
            self.direc[3] = False
            now = pygame.time.get_ticks()
            # Vérifiez si le cooldown du projectile est écoulé
            if now - self.last_projectile_time >= self.cooldown_projectile:
                self.last_projectile_time = now  # Mettez à jour le temps du dernier tir
                self.rect.x, self.rect.y = self.pos[0], self.pos[1]
                self.all_projectiles.add(Projectile(self))
                self.shoot -= 1

                
        elif self.shoot == 0:  # Vérifiez si self.shoot a atteint 0
            self.phase_1_go = False
            self.phase_2_go = True            
            
        
    def phase_2(self):
        
        if self.shoot != 16-self.vie:
            self.direc[3] = True
            self.direc[2] = False
            now = pygame.time.get_ticks()
            if now - self.last_reload_time >= self.cooldown_reload:
                self.last_reload_time = now 
                
                self.shoot +=1
        else:
            self.phase_1_go = True
            self.phase_2_go = False 


    def grav(self):
        
        if self.pos[1] < 350:
            self.col5 = self.niveau.mur[round((self.pos[1]-2)//19.3)][round((self.pos[0]+self.longniv)//36)] #collisions g haut
            self.col6 = self.niveau.mur[round((self.pos[1]+64)//19.3)][round((self.pos[0]+self.longniv)//36)] #collisions g bas
            self.col7 = self.niveau.mur[round((self.pos[1]-2)//19.3)][round((self.pos[0]-2+self.longniv)//36+1)] #collisions d haut
            self.col8 = self.niveau.mur[round((self.pos[1]+64)//19.3)][round((self.pos[0]-2+self.longniv)//36+1)] #collisions d bas

            if self.col6==1 or self.col8==1 or self.col8==5 or self.col6==5 or self.col5==4 or self.col7==4 or self.col6==6 or self.col8==6:
                pass
            else:
                self.pos[1] += self.vitesse+3
        else:
            self.pos[1] += self.vitesse


        if self.niveau.mur[round((self.pos[1]+40)//20)][round((self.pos[0]-2+self.longniv+47)//36)] == 5:
            self.pos[1] -= self.vitesse +10
        if self.niveau.mur[round((self.pos[1]+42)//20)][round((self.pos[0]-2+self.longniv+47)//36)] == 1:
            self.pos[1] -= 10

    def animbosse(self):
        
        if self.direc[0] == True:
            self.bosseanimact= 0
        if self.direc[1] == True:
            self.bosseanimact = 1
        if self.direc[2] == True:
            self.bosseanimact = 2
        if self.direc[3] == True:
            self.bosseanimact = 3
         
        
        if self.bosseanicp >= 12:
            if self.bosseanim <= 4:        
                self.bosseanim += 1
                self.bosseanicp = 0
            else:
                self.bosseanim = 0
        else:
            self.bosseanicp +=1
