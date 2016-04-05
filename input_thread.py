import pygame
from pygame.locals import K_UP, K_DOWN

current_selection = 0

def controls(game):
    while game.estado != "ERROR":
        pygame.time.delay(1)
        pressed = pygame.key.get_pressed()
        if game.estado == "MENU":
            global current_selection
            if pressed[K_UP] and current_selection > 1: current_selection -= 1
            elif pressed[K_DOWN] and current_selection < 3: current_selection += 1