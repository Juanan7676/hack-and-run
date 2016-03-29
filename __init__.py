import pygame, math, time, os, config, menu, util, render_engine, sys
from pygame.locals import *
from config import *
from menu import *
from util import *
from render_engine import *
# CONSTANTES
ANCHO = None
ALTO = None
# CONSTANTES

# PROGRAMA PRINCIPAL
def main():
    JUEGO = Game()
    configuracion = load_config("config.cfg")
    ANCHO = configuracion.getWindowANCHO()
    ALTO = configuracion.getWindowALTO()
    screen = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("TESTS")
    fuente = pygame.font.SysFont("Calibri",15)
    JUEGO.complete_init(configuracion)
    ticked = 0
    ticks_before = pygame.time.get_ticks()
    ticks_after = pygame.time.get_ticks()
    fps = 60
    while True:
        screen.fill((0,0,0))
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        for obj in get_objects(JUEGO):
            screen.blit(obj.get_assoc() , obj.get_rect())
        if configuracion.getShowFPS():
            if (ticks_after - ticks_before > 1000):
                fps = ticked / ((ticks_after - ticks_before) / 1000)
                ticked = 0
                ticks_before = pygame.time.get_ticks()
            label = fuente.render("FPS: " + str(fps) ,1,(255,255,255))
            screen.blit(label,(ANCHO - 60, 20))
        pygame.display.flip()
        ticks_after = pygame.time.get_ticks()
        ticked += 1
if __name__ == '__main__':
    pygame.init()
    main()
