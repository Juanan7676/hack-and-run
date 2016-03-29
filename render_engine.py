# coding:utf-8
import util
from util import load_image
from Juego.menu import pintar_menu

class Game:
    def __init__(self):
        """
        Instanciar esta clase sólo UNA VEZ, al principio del programa.
        """
        self.estado = "INICIO" # Estados posibles: INICIO, ERROR, MENU, PARTIDA
    def complete_init(self, config):
        """
        Llamar cuando se ha completado el arranque y empezar a renderizar el menú.
        """
        self.config = config
        self.estado = "MENU"


def get_objects(juego):
    if juego.estado == "INICIO": return [] # TODO: Print loading
    elif juego.estado == "MENU":
        return pintar_menu(juego.config)
    else: return []