import pygame, math, time, os
from pygame.locals import *


# CONSTANTES
ANCHO = 640
ALTO = 480
# CONSTANTES

# PROGRAMA PRINCIPAL

pygame.init()
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("TESTS")
print "Hola"
print "Adios"

while True:
    pygame.display.flip()
