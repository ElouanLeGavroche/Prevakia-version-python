import pygame
pygame.init()

def charger_icon():
    icon = pygame.image.load("assets/icon/Icon_2.png")
    return icon

class Quitter():
    def __init__(self):
        self.exit = False
        pygame.display.set_caption("Quitter")
        pygame.display.set_icon(charger_icon())
        self.conf = pygame.display.set_mode((680, 100))

        self.police = pygame.font.SysFont("monospace" ,30)
        self.titre = self.police.render("Voulez vous vraiment quitter ?",True,  (255,255,255))

    def text(self):
        while self.exit == False:
            self.conf.blit(self.titre, (70, 0))
            pygame.display.flip()
            self.conf.fill((0,0,0))
            

            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    self.exit = True
                    return True
def main():
    jeu = Quitter()
    jeu.text()
    pygame.quit()
    
if __name__ == '__main__':
    main()
