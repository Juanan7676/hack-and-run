import pygame, math, time, os, config, menu, util, render_engine, sys, threading, input_thread
from pygame.locals import *
from config import *
from menu import *
from util import *
from render_engine import *
from threading import Thread
from input_thread import *
# CONSTANTES
ANCHO = None
ALTO = None
# CONSTANTES

# PROGRAMA PRINCIPAL

def main():
    configuracion = load_config("config.cfg")
    ANCHO = configuracion.getWindowANCHO()
    ALTO = configuracion.getWindowALTO()
    screen = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("TESTS")
    JUEGO = Game()
    fuente = pygame.font.SysFont("Calibri",15)
    JUEGO.complete_init(configuracion)
    ticked = 0
    ticks_before = pygame.time.get_ticks()
    ticks_after = pygame.time.get_ticks()
    fps = 60
    xdd = Thread(target = controls, args= (JUEGO, ))
    xdd.daemon = True
    logo = load_image("images/logo.png", True)
    #xdd.start()
    fondo = load_image("images/background.jpg")
    seleccion = load_image("images/flecha.png",True)
    while True:
        
        if JUEGO.estado == "MENU": screen.blit(fondo, (-55,0))
        else: screen.fill((0,0,0))
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                JUEGO.estado = "ERROR"
                sys.exit(0)
            elif eventos.type == KEYDOWN and JUEGO.estado != "PARTIDA":
                controls(JUEGO)
        if JUEGO.estado == "ERROR": sys.exit(0)
        if JUEGO.estado == "PARTIDA": controls(JUEGO)
        for obj in get_objects(JUEGO, seleccion, logo):
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
