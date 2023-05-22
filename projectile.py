import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, bosse):
        super().__init__()
        self.image = pygame.image.load("assets/projectile/balles.png")
        self.rect = self.image.get_rect()
        self.bosse = bosse
        self.vitesse = 8
        self.pos =[0,0]       
        self.pos[0] -= self.vitesse

        self.rect.x = bosse.rect.x
        self.rect.y = bosse.rect.y+30

    def move(self):
        self.rect.x -= self.vitesse
        if self.rect.x < 0:
            self.remove()

    def remove(self):
        self.bosse.all_projectiles.remove(self)
     
