import pygame
from pygame.locals import *


# CONSTANTES
ANCHO = 640
ALTO = 480
# CONSTANTES

# PROGRAMA PRINCIPAL

pygame.init()
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("TESTING PURPOSES")


while True:
    pygame.display.flip()