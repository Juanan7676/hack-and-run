import pygame
from util import Pintable#, load_image

def pintar_menu(config, seleccionado, seleccion, logo):
    obj = []
    pintable4 = Pintable(seleccion, seleccion.get_rect())
    fuente = pygame.font.SysFont("Calibri", 40)
    ancho = config.getWindowANCHO()
    alto = config.getWindowALTO()
    label1 = fuente.render("Jugar" ,1,(255,255,255))
    label1_rect = label1.get_rect()
    label1_rect.centerx = ancho / 2
    label1_rect.centery = alto / 2 - 20
    pintable1 = Pintable(label1, label1_rect)
    label2 = fuente.render("Opciones",1,(255,255,255))
    label2_rect = label2.get_rect()
    label2_rect.centerx = ancho / 2
    label2_rect.centery = alto / 2 + 50
    pintable2 = Pintable(label2, label2_rect)
    label3 = fuente.render("Salir",1,(255,255,255))
    label3_rect = label3.get_rect()
    label3_rect.centerx = ancho / 2
    label3_rect.centery = alto / 2 + 110
    pintable3 = Pintable(label3, label3_rect)
    pintable5 = Pintable(logo, logo.get_rect())
    pintable5.rect.centerx = config.getWindowANCHO() / 2
    pintable5.rect.centery = 40
    obj.append(pintable1)
    obj.append(pintable2)
    obj.append(pintable3)
    obj.append(pintable5)
    if seleccionado != 0:
        pintable4.rect.centery = obj[seleccionado - 1].rect.centery
        pintable4.rect.right = obj[seleccionado - 1].rect.left - 5
        obj.append(pintable4)
    return obj

def pintar_opciones(config, seleccionado):
    objetos = []
    #seleccion = load_image("images/flecha.png",True)
    
    return objetos
