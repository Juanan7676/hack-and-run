# coding:utf-8

from Juego.menu import *

class Game:
    def __init__(self):
        """
        Instanciar esta clase sólo UNA VEZ, al principio del programa.
        """
        self.estado = "INICIO" # Estados posibles: INICIO, ERROR, MENU, PARTIDA, OPCIONES
        self.seleccionado = 0
    def complete_init(self, config):
        """
        Llamar cuando se ha completado el arranque y empezar a renderizar el menú.
        """
        self.config = config
        self.estado = "MENU"
    def set_menu_selected(self, selection):
        if self.estado != "MENU": return False
        else: self.seleccionado = selection
    def get_menu_selected(self):
        return self.seleccionado

def get_objects(juego, seleccion):
    if juego.estado == "INICIO": return [] # TODO: Print loading
    elif juego.estado == "MENU":
        return pintar_menu(juego.config, juego.get_menu_selected(), seleccion)
    elif juego.estado == "ERROR":
        return [] # TODO: BSoD
    elif juego.estado == "OPCIONES":
        return pintar_opciones(juego.config, seleccion)
    else: return []
