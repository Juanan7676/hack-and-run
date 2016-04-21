import pygame, time
from pygame.locals import K_UP, K_DOWN

def controls(game):
    while game.estado != "ERROR":
        pygame.time.wait(100)
        pressed = pygame.key.get_pressed()
        if game.estado == "MENU":
            if pressed[K_UP] and game.get_menu_selected() > 1: 
                game.set_menu_selected(game.get_menu_selected() - 1)
            elif pressed[K_DOWN] and game.get_menu_selected() < 3: 
                game.set_menu_selected(game.get_menu_selected() + 1)