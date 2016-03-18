<<<<<<< HEAD
import pygame, math, time, os
=======
import pygame, math, time, os
>>>>>>> add-imports
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

while True:
    pygame.display.flip()
