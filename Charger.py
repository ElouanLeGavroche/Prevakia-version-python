import pygame

PATH_BLOCK = "assets/blocks/"      
def charger_block():
    cube = pygame.image.load(f"{PATH_BLOCK}cube.png")
    pente = pygame.image.load(f"{PATH_BLOCK}pente.png")
    pente_2 = pygame.image.load(f"{PATH_BLOCK}pente_2.png")
    pente_3 = pygame.image.load(f"{PATH_BLOCK}pente_3.png")
    porte = pygame.image.load(f"{PATH_BLOCK}porte.png")
    support = pygame.image.load(f"{PATH_BLOCK}support.png")
    echelle = pygame.image.load(f"{PATH_BLOCK}echelle.png")
    munition = pygame.image.load(f"{PATH_BLOCK}munition.png")
    cube_bloquer = pygame.image.load(f"{PATH_BLOCK}cube_bloquer.png")
    barille = pygame.image.load(f"{PATH_BLOCK}barille_centre.png")
    bois = pygame.image.load(f"{PATH_BLOCK}bois.png")
    bois_broken = pygame.image.load(f"{PATH_BLOCK}bois_broken.png")

    return cube , pente, porte, support, echelle, munition, cube_bloquer, barille, pente_2, pente_3, bois, bois_broken

def charger_fond():

    fond_plan_fond = pygame.image.load("assets/fond/fond_opti.png").convert_alpha()
    fond_plan_fond = pygame.transform.scale(fond_plan_fond, (2700, 400))

    fond_plan_1 = pygame.image.load("assets/fond/fond_plan_1.png").convert_alpha()
    fond_plan_1 = pygame.transform.scale(fond_plan_1, (900,400))

    cache_fond_plan_1 = pygame.Surface((900,400)).convert_alpha()
    cache_fond_plan_fond = pygame.Surface((900, 400)).convert_alpha()        

    game_over = pygame.image.load("assets/fond/game_over.png")

    secret = pygame.image.load("assets/test/Edenchoque.jpg")

    menu_echap_fond = pygame.image.load("assets/fond/menu_echap_fond.png")

    classe = pygame.image.load("assets/fond/classe.png")

    return fond_plan_fond, fond_plan_1, game_over, secret, cache_fond_plan_fond, cache_fond_plan_1, menu_echap_fond, classe

def charger_item():

    cle = pygame.image.load("assets/items/cle.png")

    porte_fermer = pygame.image.load("assets/items/porte_fermer.png")

    porte_ouverte = pygame.image.load("assets/items/porte_ouverte.png")

    grappin = pygame.image.load("assets/items/grappin.png")

    hache = pygame.image.load("assets/items/hache.png")

    generateur_on = pygame.image.load("assets/items/generateur_on.png")

    generateur_off = pygame.image.load("assets/items/generateur_off.png")

    bouclier_on = pygame.image.load("assets/items/bouclier_on.png")

    bouclier_off = pygame.image.load("assets/items/bouclier_off.png")

    lumiere = pygame.image.load("assets/items/lumiere.png")

    banniere =pygame.image.load("assets/items/prevakia.png")

    flux_lumiere = pygame.image.load("assets/items/flux_lumiere.png").convert_alpha()
    flux_lumiere = pygame.transform.scale(flux_lumiere, (438, 400))
    cache_flux_lumiere = pygame.Surface((438,400)).convert_alpha()

    return cle, porte_ouverte, porte_fermer, grappin, hache, generateur_on, generateur_off, lumiere, flux_lumiere, cache_flux_lumiere, bouclier_on, bouclier_off, banniere




