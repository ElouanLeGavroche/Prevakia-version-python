__all__ = ['main']

import pygame
import pygame_menu
import json
from pygame_menu.examples import create_example_window

from typing import Optional

from Main import Main
from src import son

FPS = 30
WINDOW_SIZE = (900, 400)


sound: Optional['pygame_menu.sound.Sound'] = None
surface: Optional['pygame.Surface'] = None
main_menu: Optional['pygame_menu.Menu'] = None

# charger l'image
background_image = pygame_menu.BaseImage(image_path=r'assets/fond/fond_menu.png',)

#musique volume
def ambiant(value, level):
    son.menu.play()
    son.bruitage = 0
    son.bruitage = round(son.bruitage + level, 1)
    son.menu.set_volume(son.bruitage)

    son.data["volumeEffect"] = level
    json.dump(son.data, open("data/jeu.json", "w"))
    
def music(value, level):
    son.menu.play()
    son.volume = 0
    son.volume = round(son.volume + level, 1)
    pygame.mixer.music.set_volume(son.volume)
        
    son.data["volumeMusic"] = level
    json.dump(son.data, open("data/jeu.json", "w"))

#load save
def LOAD():
    son.menu.play()
    fileObject = open("save/slot_1.json", "r")
    jsonContent = fileObject.read()
    obj_python = json.loads(jsonContent)
    
    jeu = Main(obj_python["niveau"],True, obj_python["inventaire"])
    jeu = Main(4, True, [11,0,0,0,0])
    jeu.boucle_jeu()

#commence nouvelle partie
def START():
    son.menu.play()
    jeu = Main(0, True, [0,0,0,0,0])
    jeu.new_game()

#fond d'ecran menu
def main_background() -> None:

    background_image.draw(surface)

#programe menu
def main(test: bool = False) -> None:

    global main_menu
    global sound
    global surface

    #fenetre
    surface = create_example_window('Prevakia', WINDOW_SIZE)
    clock = pygame.time.Clock()

    #menu theme/couleur
    main_menu_theme = pygame_menu.themes.THEME_DARK.copy()
    main_menu_theme.set_background_color_opacity(0.7)  # 50% transparent


    main_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.7,
        onclose=pygame_menu.events.EXIT,
        theme=main_menu_theme,
        title='Prevakia',
        width=WINDOW_SIZE[0] * 0.8
    )

    theme_bg_image = main_menu_theme.copy()
    theme_bg_image.background_color = pygame_menu.BaseImage(
        image_path=pygame_menu.baseimage.IMAGE_EXAMPLE_CARBON_FIBER #<---------- a changer
    )

    theme_bg_image.title_font_size = 25
    option = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.7,
        onclose=pygame_menu.events.EXIT,
        theme=theme_bg_image,
        title='Options',
        width=WINDOW_SIZE[0] * 0.8
    )
    option.add.selector('Musique', [("0", 0), ("1", 0.1), ("2", 0.2), ("3", 0.3), ("4", 0.4), ("5", 0.5), ("6", 0.6), ("7", 0.7), ("8", 0.8), ("9", 0.9), ("10", 1)], onchange=music)
    option.add.selector('Bruitage', [("0", 0), ("1", 0.1), ("2", 0.2), ("3", 0.3), ("4", 0.4), ("5", 0.5), ("6", 0.6), ("7", 0.7), ("8", 0.8), ("9", 0.9), ("10", 1)], onchange=ambiant)
    option.add.button('Retour', pygame_menu.events.BACK)
#
    start = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.7,
        onclose=pygame_menu.events.EXIT,
        theme=theme_bg_image,
        title='Lancer',
        width=WINDOW_SIZE[0] * 0.8,
    )
    start.add.button('Charger', LOAD)
    start.add.button('Nouvelle Partie', START)


    button_image = pygame_menu.BaseImage(pygame_menu.baseimage.IMAGE_EXAMPLE_CARBON_FIBER)

    main_menu.add.button('Jouer', start)
    main_menu.add.button('Option', option)
    main_menu.add.button('Quitter', pygame_menu.events.EXIT)


    #boucle
    while True:

        #FPS
        clock.tick(FPS)

        #menu principale boucle
        
        #jsp on ma dit de faire sa mais c'est pour l'afichage je crois enfin bref pas grave
        pygame.display.flip()
        main_menu.mainloop(surface, main_background, disable_loop=test, fps_limit=FPS)

        if test:
            break


if __name__ == '__main__':
    main()
