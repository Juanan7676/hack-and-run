import pygame, math, time, os
from pygame.locals import *


# CONSTANTES
ANCHO = 640
ALTO = 480
# CONSTANTES

# PROGRAMA PRINCIPAL
def main():
    pygame.init()
    pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("TESTS")

    while True:
        pygame.display.flip()

if __name__ == '__main__':
    main()