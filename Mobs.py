import pygame

from Niveau_1 import Niveau_1
from Niveau_2 import Niveau_2
from Niveau_3 import Niveau_3
from Niveau_4 import Niveau_4
from Niveau_5 import Niveau_5

from Joueur import Joueur

class Mobs():
    def __init__(self, lvl):

        self.image = [
            
                    
                    [pygame.image.load("assets/joueur/mob/mobs_1.png"),
                     pygame.image.load("assets/joueur/mob/mobs_2.png"),
                     pygame.image.load("assets/joueur/mob/mobs_2.png"),
                     pygame.image.load("assets/joueur/mob/mobs_1.png")],
                    
                    [pygame.image.load("assets/joueur/mob/mobs_5.png"),
                     pygame.image.load("assets/joueur/mob/mobs_6.png"),
                     pygame.image.load("assets/joueur/mob/mobs_5.png"),
                     pygame.image.load("assets/joueur/mob/mobs_5.png")],
                    
                    [pygame.image.load("assets/joueur/mob/mobs_3.png"),
                     pygame.image.load("assets/joueur/mob/mobs_3.png"),
                     pygame.image.load("assets/joueur/mob/mobs_3.png"),
                     pygame.image.load("assets/joueur/mob/mobs_3.png")],
                    
                    [pygame.image.load("assets/joueur/mob/mobs_4.png"),
                     pygame.image.load("assets/joueur/mob/mobs_4.png"),
                     pygame.image.load("assets/joueur/mob/mobs_4.png"),
                     pygame.image.load("assets/joueur/mob/mobs_4.png")]
                    
                      ]
        
        self.detection = pygame.image.load("assets/joueur/detection.png")
        self.vitesse = 1
        
        self.longniv= 0
        
        self.mobanim = 0
        
        self.mobanicp = 0
        
        self.mobanimact = 0
        
        self.mobcp = 0
    
        self.pos_debut, self.pos_fin, self.pos, self.retour, self.image_mobs = self.pos_lvl(lvl)
        

    def etat_passive(self, i):
        self.mobcp = 0
        
        if self.pos_fin[i][0]-1 >= self.pos[i][0] and self.retour[i] == 0:
            self.pos[i][0] += self.vitesse
            self.mobanimact = 0
            
        if self.pos_fin[i][0] <= self.pos[i][0]:
                
                
            self.image_detection[i] = pygame.transform.flip(self.image_detection[i], True, False)
            self.retour[i] = 1
            self.statut[i] = 1                    
            
        if self.pos_debut[i][0]+1 <= self.pos[i][0] and self.retour[i] == 1:
            self.retour[i] = 1
            self.pos[i][0] -= self.vitesse
            self.mobanimact = 1
            
        if self.pos_debut[i][0] >= self.pos[i][0]:
              
                
            self.image_detection[i] = pygame.transform.flip(self.image_detection[i], True, False)
            self.retour[i] = 0
            self.statut[i] = 0
            
    def etat_agressive(self, i):
        
        if self.pos[i][0]+6 > self.dernier_pos[0] and self.pos[i][0]-6 < self.dernier_pos[0]:
            self.pos[i][0] = self.dernier_pos[0]
        else:
            if not self.pos[i][0] == self.dernier_pos[0]:
                if self.pos[i][0] < self.dernier_pos[0]:
                    if self.statut[i] == 1:
                        self.rotation_b(i)
                        
                    if self.mobcp == 40:
                        self.pos[i][0] += self.vitesse+8
                    else:
                        self.mobcp +=1
                    
                    self.mobanimact = 2
                    
                elif self.pos[i][0] > self.dernier_pos[0]:
                    if self.statut[i] == 0:
                        self.rotation_a(i)
                    
                    if self.mobcp == 40:
                        self.pos[i][0] -= self.vitesse+8
                    else:
                        self.mobcp +=1
                    self.mobanimact = 3
            
        
            
        
    def rotation_a(self, i):
        self.retour[i] = 1
        self.image_detection[i] = pygame.transform.flip(self.image_detection[i], True, False)
        self.statut[i] = 1
        
    def rotation_b(self, i):
        self.retour[i] = 0
        self.image_detection[i] = pygame.transform.flip(self.image_detection[i], True, False)
        self.statut[i] = 0
        
        
    def pos_lvl(self, lvl):
        level_configs = {
            0: {
                'niveau': Niveau_1(),
                'retour': [0, 0, 0],
                'pos_debut': [[500, 200], [950, 200]],
                'pos_fin': [[700, 200], [1100, 200]],
                'pos': [[500, 200], [950, 200]],
                'etat': [False, False],
                'image_mobs': [self.image, self.image],
                'image_detection': [self.detection, self.detection],
                'pivote': [45, -95],
                'statut': [0, 0],
                'pivote_2': [140, 130],
                'dernier_pos': [0, 0]
            },
            1: {
                'niveau': Niveau_2(),
                'retour': [],

                'pos_debut': [],
                'pos_fin': [],
                'pos': [],
                'etat': [],
                'image_mobs': [],
                'image_detection': [],
                'pivote': [],
                'statut': [],
                'pivote_2': [],
                'dernier_pos': []
            },
            2: {
                'niveau': Niveau_3(),
                'retour': [0,0],

                'pos_debut': [[2044, 60]],
                'pos_fin': [[2610, 60]],
                'pos': [[2044, 60]],
                'etat': [False],
                'image_mobs': [self.image],
                'image_detection': [self.detection],
                'pivote': [45,-95],
                'statut': [0],
                'pivote_2': [140,130],
                'dernier_pos': [0]
            },
            3: {
                'niveau': Niveau_4(),
                'retour': [0,0,0,0],

                'pos_debut': [[300, 320],[1200, 100],[2250, 320],[3000, 320]],
                'pos_fin': [[500, 320],[1400, 100],[2450, 320],[3200, 320]],
                'pos': [[300, 320],[1200, 100],[2250, 320],[3000, 320]],
                'etat': [False,False,False,False],
                'image_mobs': [self.image,self.image,self.image,self.image],
                'image_detection': [self.detection,self.detection,self.detection,self.detection],
                'pivote': [45, -95],
                'statut': [0,0,0,0],
                'pivote_2': [140, 130],
                'dernier_pos': [0,0,0,0]
            },

            4: {
                'niveau': Niveau_5(),
                'retour': [0],
                'pos_debut': [[2000, 10]],
                'pos_fin': [[2710, 10]],
                'pos': [[2000, 10]],
                'etat': [False],
                'image_mobs': [self.image],
                'image_detection': [self.detection],
                'pivote': [45, -95],
                'statut': [0],
                'pivote_2': [140, 130],
                'dernier_pos': [0]
            }
        }

        if lvl in level_configs:
            config = level_configs[lvl]
            self.niveau = config['niveau']
            self.retour = config['retour']
            self.pos_debut = config['pos_debut']
            self.pos_fin = config['pos_fin']
            self.pos = config['pos']
            self.etat = config['etat']
            self.image_mobs = config['image_mobs']
            self.image_detection = config['image_detection']
            self.pivote = config['pivote']
            self.statut = config['statut']
            self.pivote_2 = config['pivote_2']
            self.dernier_pos = config['dernier_pos']
        else:
            # Gérer le cas où le niveau n'est pas défini dans le dictionnaire
            pass

        return self.pos_debut, self.pos_fin, self.pos, self.retour, self.image_mobs


    def bouger(self):
        for i in range(len(self.pos_debut)):
            if self.pos[i][0] <= 0 or self.pos[i][0] >= 1000:
                pass
            else:
                if self.etat[i] == False:
                    self.etat_passive(i)
                else:
                    self.etat_agressive(i)
 
    

    def grav(self):
        for i in range(len(self.pos_debut)):
            if self.pos[i][1] < 350:
                self.col5 = self.niveau.mur[round((self.pos[i][1]-2)//19.3)][round((self.pos[i][0]+self.longniv)//36)] #collisions g haut
                self.col6 = self.niveau.mur[round((self.pos[i][1]+37)//19.3)][round((self.pos[i][0]+self.longniv)//36)] #collisions g bas
                self.col7 = self.niveau.mur[round((self.pos[i][1]-2)//19.3)][round((self.pos[i][0]-2+self.longniv)//36+1)] #collisions d haut
                self.col8 = self.niveau.mur[round((self.pos[i][1]+37)//19.3)][round((self.pos[i][0]-2+self.longniv)//36+1)] #collisions d bas

                if self.col6==1 or self.col8==1 or self.col8==5 or self.col6==5 or self.col6==6 or self.col8==6:
                    pass
                else:
                    self.pos[i][1] += self.vitesse
            else:
                self.pos[i][1] += self.vitesse
                
                
            if self.niveau.mur[round((self.pos[i][1]+40)//20)][round((self.pos[i][0]-2+self.longniv+47)//36)] == 5:
                self.pos[i][1] -= self.vitesse +10
            if self.niveau.mur[round((self.pos[i][1]+42)//20)][round((self.pos[i][0]-2+self.longniv+47)//36)] == 1:
                self.pos[i][1] -= 1

    def animmob(self):
        
        
        if self.mobanicp >= 12:
            if self.mobanim <= 2:        
                self.mobanim += 1
                self.mobanicp = 0
            else:
                self.mobanim = 0
        else:
            self.mobanicp +=1
    
