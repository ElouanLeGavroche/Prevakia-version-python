import pygame


class Joueur():
    def __init__(self, niveau):
        
        
        self.player = [
                        
                       #idle droite animation debut 0
                       [pygame.image.load("assets/joueur/idle/idle1.png"),
                        pygame.image.load("assets/joueur/idle/idle2.png"),
                        pygame.image.load("assets/joueur/idle/idle1.png"),
                        pygame.image.load("assets/joueur/idle/idle1.png")],
                       
                       #idle gauche animation debut 1
                       [pygame.image.load("assets/joueur/idle/idle3.png"),
                        pygame.image.load("assets/joueur/idle/idle4.png"),
                        pygame.image.load("assets/joueur/idle/idle4.png"),
                        pygame.image.load("assets/joueur/idle/idle3.png")],
                       
                       #droite animation debut 2
                       [pygame.image.load("assets/joueur/droite/droite2.png"),
                        pygame.image.load("assets/joueur/droite/droite3.png"),
                        pygame.image.load("assets/joueur/droite/droite2.png"),
                        pygame.image.load("assets/joueur/droite/droite1.png")],
                       
                       #gauche animation debut 3
                       [pygame.image.load("assets/joueur/gauche/gauche2.png"),
                        pygame.image.load("assets/joueur/gauche/gauche3.png"),
                        pygame.image.load("assets/joueur/gauche/gauche2.png"),
                        pygame.image.load("assets/joueur/gauche/gauche1.png")],
                       
                       #grav droite 4
                       [pygame.image.load("assets/joueur/grav/grav.png"),
                        pygame.image.load("assets/joueur/grav/grav.png"),
                        pygame.image.load("assets/joueur/grav/grav.png"),
                        pygame.image.load("assets/joueur/grav/grav.png")],
                       
                       #grav gauche 5
                       [pygame.image.load("assets/joueur/grav/grav2.png"),
                        pygame.image.load("assets/joueur/grav/grav2.png"),
                        pygame.image.load("assets/joueur/grav/grav2.png"),
                        pygame.image.load("assets/joueur/grav/grav2.png")],
                       
                       #idle echelle 6
                       [pygame.image.load("assets/joueur/echelle/echelle1.png"),
                        pygame.image.load("assets/joueur/echelle/echelle1.png"),
                        pygame.image.load("assets/joueur/echelle/echelle1.png"),
                        pygame.image.load("assets/joueur/echelle/echelle1.png")],
                       
                       #echelle 7
                       [pygame.image.load("assets/joueur/echelle/echelle1.png"),
                        pygame.image.load("assets/joueur/echelle/echelle1.png"),
                        pygame.image.load("assets/joueur/echelle/echelle2.png"),
                        pygame.image.load("assets/joueur/echelle/echelle2.png")],
                       
                       #grap debut 8
                       [pygame.image.load("assets/joueur/grap/grap.png"),
                        pygame.image.load("assets/joueur/grap/grap.png"),
                        pygame.image.load("assets/joueur/grap/grap2.png"),
                        pygame.image.load("assets/joueur/grap/grap3.png")],
                       
                       #grap idle 9
                       [pygame.image.load("assets/joueur/grap/grap3.png"),
                        pygame.image.load("assets/joueur/grap/grap3.png"),
                        pygame.image.load("assets/joueur/grap/grap3.png"),
                        pygame.image.load("assets/joueur/grap/grap3.png")],
                       
                       #grap bouge droite 10
                       [pygame.image.load("assets/joueur/grap/pend1.png"),
                        pygame.image.load("assets/joueur/grap/pend1.png"),
                        pygame.image.load("assets/joueur/grap/pend2.png"),
                        pygame.image.load("assets/joueur/grap/pend3.png"),
                        pygame.image.load("assets/joueur/grap/pend3.png"),
                        pygame.image.load("assets/joueur/grap/pend2.png")],
                       
                       #grap bouge gauche 11
                       [pygame.image.load("assets/joueur/grap/pend21.png"),
                        pygame.image.load("assets/joueur/grap/pend21.png"),
                        pygame.image.load("assets/joueur/grap/pend22.png"),
                        pygame.image.load("assets/joueur/grap/pend23.png"),
                        pygame.image.load("assets/joueur/grap/pend23.png"),
                        pygame.image.load("assets/joueur/grap/pend22.png")],
                       
                       #idle pend 12
                       [pygame.image.load("assets/joueur/grap/pend1.png"),
                        pygame.image.load("assets/joueur/grap/pend1.png"),
                        pygame.image.load("assets/joueur/grap/pend1.png"),
                        pygame.image.load("assets/joueur/grap/pend1.png"),
                        pygame.image.load("assets/joueur/grap/pend1.png"),
                        pygame.image.load("assets/joueur/grap/pend1.png")],
                        #13
                       [pygame.image.load("assets/joueur/grap/pend21.png"),
                        pygame.image.load("assets/joueur/grap/pend21.png"),
                        pygame.image.load("assets/joueur/grap/pend21.png"),
                        pygame.image.load("assets/joueur/grap/pend21.png"),
                        pygame.image.load("assets/joueur/grap/pend21.png"),
                        pygame.image.load("assets/joueur/grap/pend21.png")],
                       #14
                       [pygame.image.load("assets/joueur/idle/idle1.png"),
                        pygame.image.load("assets/joueur/grap/grap2.png"),
                        pygame.image.load("assets/joueur/grap/grap2.png"),
                        pygame.image.load("assets/joueur/grap/grap.png"),
                        pygame.image.load("assets/joueur/grap/grap.png"),
                        pygame.image.load("assets/joueur/grap/grap.png"),
                        pygame.image.load("assets/joueur/idle/idle1.png")],
                        
                        #15
                        [pygame.image.load("assets/joueur/idle/idle3.png"),
                        pygame.image.load("assets/joueur/grap/grapg2.png"),
                        pygame.image.load("assets/joueur/grap/grapg2.png"),
                        pygame.image.load("assets/joueur/grap/grapg.png"),
                        pygame.image.load("assets/joueur/grap/grapg.png"),
                        pygame.image.load("assets/joueur/grap/grapg.png"),
                        pygame.image.load("assets/joueur/idle/idle3.png")]
                        ]
        
        
        self.direc = [False, #gauche 0
                      True,  #droite 1
                      False, #grav 2
                      False, #landing 3
                      True,  #sur sol 4
                      False, #echelle 5
                      False, #debut grap 6
                      False, #pendant grap 7
                      False,  #fin grap 8
                      False  #atak 9
                      ]
        
                
        self.animcp = 0 #compteur animation 12 fps
        self.animact = 0#l'animation choisie         self.pos = [-100,286]

        self.vie = 3
        self.vitesse = 2
        
        self.pos = [-70,286]
        self.rect = self.player[3][0].get_rect()
        self.rect.x, self.rect.y = self.pos[0], self.pos[1]
        
        self.gauche = False
        self.droite = False
        self.haut = False
        self.bas = False
        
        self.grap = False

        self.grappin_recu = False
        self.hache_recu = False
        
        self.niveau = niveau
            
        self.longniv=0

        self.inventaire = [0,0,0,0,0]
        
        self.animp = 0
        
        self.cp = 0 #temp avant reset

        self.posSouris = [0,0]
        
        self.boisbroken = False 
        
        
    def collisions(self):
          
        self.col2 = self.niveau.mur[round((self.pos[1]+32)//20)][round((self.pos[0]-2+self.longniv)//36)] #collisions gauche b
        
        self.col8 = self.niveau.mur[round((self.pos[1]+37)//20)][round((self.pos[0]-2+self.longniv)//36+1)] #collisions d bas
        
        self.col1 = self.niveau.mur[round(self.pos[1]//20)][round((self.pos[0]-2+self.longniv)//36)] #collisions gauche h
        
        self.col7 = self.niveau.mur[round((self.pos[1]-2)//20)][round((self.pos[0]-2+self.longniv)//36+1)] #collisions d haut
        
        self.col4 = self.niveau.mur[round((self.pos[1]+32)//20)][round((self.pos[0]+self.longniv)//36+1)] #collisions droite b
        
        self.col6 = self.niveau.mur[round((self.pos[1]+37)//20)][round((self.pos[0]+self.longniv)//36)] #collisions g bas
        
        self.col3 = self.niveau.mur[round(self.pos[1]//20)][round((self.pos[0]+self.longniv)//36+1)] #collisions droite h
        
        self.col5 = self.niveau.mur[round((self.pos[1]-2)//20)][round((self.pos[0]+self.longniv)//36)] #collisions g haut
        
    
    def grav(self):
        
        
        if self.col6==1 or self.col8==1 or self.col8==5 or self.col6==5 or self.col5==4 or self.col7==4 or self.col6==4 or self.col8==4 or self.col6==6 or self.col8==6 or self.col6==7 or self.col8==7 or self.grap == True:
            
            self.direc[2] = False
            if self.direc[4] == False:
                self.direc[3] = True
            self.direc[4] = True
            if self.grap == False:
                self.direc[7] = False
            if self.niveau.mur[round((self.pos[1]+34)//20)][round((self.pos[0]+self.longniv)//36)]==1 or self.niveau.mur[round((self.pos[1]+34)//20)][round((self.pos[0]+self.longniv+34)//36)]==1 or self.niveau.mur[round((self.pos[1]+34)//20)][round((self.pos[0]+self.longniv)//36)]==6:      
                self.pos[1] -= self.vitesse - 1
                if self.col1 == 1 or self.col3 == 1:
                    self.pos[1] += self.vitesse - 1
            
            if self.col5==4 or self.col7==4 or self.col6==4 or self.col8==4:
                self.direc[5] = True
            else:
                self.direc[5] = False
                
        else:
            self.direc[2] = True
            self.direc[4] = False
            self.direc[5] = False
            self.pos[1] += self.vitesse + 4
                
        
    def grappin(self):
        
        self.posSouris = pygame.mouse.get_pos()
        
        
        if self.direc[6]==False:
            if self.direc[8] == True:
                pass
            else:
                if self.grap==False or not self.niveau.mur[round((self.posSouris[1])//20)][round((self.posSouris[0]+self.longniv)//36)] == 3 or self.pos[0] < self.posSouris[0]-50 or self.pos[0] > self.posSouris[0]+50:
                    self.grap=False
                else:
                    if self.pos[0]+30< (self.posSouris[0]-10):
                        if self.col1==1 or self.col2==1 or self.col3==1:
                            pass
                        else:
                            self.pos[0] += self.vitesse+7
                            
                    elif self.pos[0]+30> (self.posSouris[0]+10):
                        if self.col3==1 or self.col4==1 or self.col1==1:
                            pass
                        else:
                            self.pos[0] -= self.vitesse+7
                    else:
                        pass
                        
                    if self.pos[1]< (self.posSouris[1]-20):
                        if self.col8==1 or self.col6==1:
                            pass
                        else:
                            self.pos[1] += self.vitesse+7
                            
                    elif self.pos[1]> (self.posSouris[1]+10):
                        if self.col5==1 or self.col7==1:
                            pass
                        else:
                            self.pos[1] -= self.vitesse+7
                    else:
                        pass
            
    def collisiongrap(self):
        if self.niveau.mur[round((self.pos[1]-27)//20)][round((self.pos[0]+self.longniv+30)//36)] == 3:
            self.direc[6] = False
            self.direc[7] = False
            self.direc[8] = True
        if not self.niveau.mur[round((self.pos[1]-27)//20)][round((self.pos[0]+self.longniv+30)//36)] == 3 and self.direc[8] == True:
            self.direc[8] = False
            self.animp = 0

    def bouger(self):
        
        if self.direc[9] == True:
            pass
        else:
            if self.gauche == False or self.col1==1 or self.col2==1 or self.col1==8 or self.col2==8 or (self.grap==True and self.direc[8] == False) or ((self.col1==105 or self.col2==105) and self.boisbroken == False):
                pass
            else:
                if self.direc[8] == True:
                    self.pos[0] -= self.vitesse-1
                else:
                    self.pos[0] -= self.vitesse
                    if self.col6==5 or self.col8==5 or self.col4==5:
                        self.pos[1] += self.vitesse-1
             
            if self.droite == False or self.col3==1 or self.col4==1 or self.col3==8 or self.col4==8 or (self.grap==True and self.direc[8] == False) or ((self.col3==105 or self.col4==105) and self.boisbroken == False):
                pass
            else:
                if self.direc[8] == True:
                    self.pos[0] += self.vitesse-1
                else:
                    self.pos[0] += self.vitesse
                    if self.col6==5 or self.col8==5 or self.col4==5:
                        self.pos[1] -= self.vitesse-1
                    if self.col6==7 or self.col8==7 or self.col4==7:
                        self.pos[1] += self.vitesse

                
            if self.haut == False or self.col5==1 or self.col7==1 or self.col5==8 or self.col7==8 or self.grap==True:
                pass
            else:
                if self.col5==4 or self.col7==4:
                    self.pos[1] -= self.vitesse+1
                
            if self.bas == False or self.col6==1 or self.col8==1 or self.col6==8 or self.col8==8 or self.grap==True:
                pass
            else:
                if self.col6==4 or self.col8==4:
                    self.pos[1] += self.vitesse+1
            return self.pos[1]
    
    def animation(self):
                   
        if self.direc[1]==True:
            self.animact = 0
        if self.direc[0]==True:
            self.animact = 1
        if self.droite==True:
            self.animact = 2
        if self.gauche==True:
            self.animact = 3
        if self.direc[2]==True:
            if self.direc[1]==True:
                self.animact = 4
            if self.direc[0]==True:
                self.animact = 5
        if self.direc[5]==True and not self.niveau.mur[round((self.pos[1]+40)//20)][round((self.pos[0]+self.longniv)//36)]==1:
            self.animact = 6
        if (self.haut==True or self.bas==True) and self.direc[5]==True:
            self.animact = 7
        if self.direc[6] == True:
            self.animact = 8
        if self.direc[7] == True:
            self.animact = 9
        if self.direc[8] == True and self.direc[1]==True:
            self.animact = 12
        if self.direc[8] == True and self.direc[0]==True:
            self.animact = 13
        if self.direc[8] == True and self.droite==True:
            self.animact = 10
        if self.direc[8] == True and self.gauche==True:
            self.animact = 11
        if self.direc[9] == True and self.direc[1]==True:
            self.animact = 14
        if self.direc[9] == True and self.direc[0]==True:
            self.animact = 15
        
        #landing
        if self.direc[3] == True and not self.direc[9] == True:
            if self.animcp <= 24:
                self.animcp +=1
                self.animp = 0
                
                if self.direc[1]==True:
                    self.animact = 2
                if self.direc[0]==True:
                    self.animact = 3
            else:
                self.animcp = 0
                self.direc[3] = False              
        #normal
        else:
            if self.animcp >= 12:
                
                if self.direc[9] == True:
                    if self.animp <= 5:        
                        self.animp += 1
                        self.animcp = 0
                    else:
                        self.animp = 0
                        self.direc[9] = False
                        
                elif self.direc[8] == True:
                    if self.animp <= 4:        
                        self.animp += 1
                        self.animcp = 0
                    else:
                        self.animp = 0         
                           
                else:
                    if self.animp <= 2:        
                        self.animp += 1
                        self.animcp = 0
                    else:
                        self.animp = 0
                        if self.direc[6] == True:
                            self.direc[6] = False
                            self.direc[7] = True
                            self.animp = 3
                            
            else:
                if self.direc[6] == True:
                    self.animcp += 4
                elif self.direc[5] == True and not self.niveau.mur[round((self.pos[1]+40)//20)][round((self.pos[0]+self.longniv)//36)]==1:
                    self.animcp += 3
                elif self.direc[9] == True:
                    self.animcp += 6
                else:
                    self.animcp += 1
                        
