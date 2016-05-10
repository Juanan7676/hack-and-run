import pygame
from pygame.locals import K_UP, K_DOWN, K_RETURN

def controls(game):
    pressed = pygame.key.get_pressed()
    if game.estado == "MENU":
        if pressed[K_UP] and game.get_menu_selected() > 1: 
            game.set_menu_selected(game.get_menu_selected() - 1)
        elif pressed[K_DOWN] and game.get_menu_selected() < 3: 
            game.set_menu_selected(game.get_menu_selected() + 1)
        elif pressed[K_RETURN] and game.get_menu_selected() != 0:
            if game.get_menu_selected() == 3: game.estado = "ERROR"
            elif game.get_menu_selected() == 2: game.estado = "OPTIONS"
            elif game.get_menu_selected() == 1: game.estado = "PARTIDA"
