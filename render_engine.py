# coding:utf-8

from Juego.menu import *
from util import load_image
from game_engine import *

class MovingEntity:
    def __init__(self, coords, img):
        """
        MovingEntity define todo tipo de entidad (jugador, policías) que se pueda mover y realizar acciones.
        
        Tiene tres características fundamentales: posición, velocidad y aceleración.
        
        En sí no representa nada en el juego, pero una clase heredada de esta sí.
        """
        self.coords = coords
        self.velocity = [0.0,0.0]
        self.acceleration = [0.0,0.0]
        self.pintable = img
        
    def simulate_pos(self):
        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]
        self.coords[0] += self.velocity[0]
        self.coords[1] += self.velocity[1]
        
    def update_pos(self, newpos):
        self.coords = newpos
        
    def update_acceleration(self, newacc):
        self.acceleration = newacc
        
    def update_velocity(self, newv):
        self.velocity = newv
    
    def get_pintable(self):
        return self.pintable
    
class Player(MovingEntity):
    def __init__(self, initialcoords, initialimg, initialhealth, name, score):
        super(Player, self).__init__(initialcoords, initialimg)
        self.health = initialhealth
        self.name = name
        self.score = score
    
        
class Game:
    def __init__(self):
        """
        Instanciar esta clase sólo UNA VEZ, al principio del programa.
        """
        self.estado = "INICIO" # Estados posibles: INICIO, ERROR, MENU, PARTIDA, OPCIONES
        self.seleccionado = 0
        self.character = {}
        self.character["Still_front"] = load_image("images/still1-new.png", True)
        self.character["Still_back"] = load_image("images/still2-new.png", True)
        self.character["Walking_still"] = load_image("images/2.png", True)
        self.character["Walking_1"] = load_image("images/1.png", True)
        self.character["Walking_2"] = load_image("images/3.png", True)
        self.suelo = load_image("images/suelo.png")
        self.game_background = load_image("images/background3.png")
        
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

def get_objects(juego, seleccion, logo):
    if juego.estado == "INICIO": return [] # TODO: Print loading
    elif juego.estado == "MENU":
        return pintar_menu(juego.config, juego.get_menu_selected(), seleccion, logo)
    elif juego.estado == "ERROR":
        return [] # TODO: BSoD
    elif juego.estado == "OPCIONES":
        return pintar_opciones(juego.config, seleccion)
    elif juego.estado == "PARTIDA":
        return paint_game(juego)
    else: return []
