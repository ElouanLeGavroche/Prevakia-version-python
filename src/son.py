import pygame
import json

# INITIALISATION DES SON
pygame.mixer.init()
data = json.load(open("data/jeu.json"))

# INITIALISATION DES SON
menu = pygame.mixer.Sound("assets/sons/click_sound.mp3")

def song_intro():
    pygame.mixer.music.load("assets/sons/music_intro.wav")
    pygame.mixer.music.play(1)
    foret = pygame.mixer.Sound('assets/sons/bruit_fond.wav')

    foret.set_volume(bruitage)
    foret.play()
    
    return foret
    
def song_game():
    pygame.mixer.music.load("assets/sons/ost.mp3")
    pygame.mixer.music.play(-1)

def song_2():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("assets/sons/hey.mp3")
    pygame.mixer.music.play(-1)


volume = data["volumeMusic"]
pygame.mixer.music.set_volume(volume)

bruitage = data["volumeEffect"]


menu.set_volume(bruitage)
