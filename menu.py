import util, pygame
from util import Pintable


def pintar_menu(config):
    
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
    return [pintable1,pintable2,pintable3]
