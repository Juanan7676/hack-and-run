# coding:utf-8
import math
from Juego.menu import *
from game_engine import *


def generate_map(juego):
    obj = []
    # Phase 1: floor
    for k in range(-1000, 1000):
        for j in range(0,2):
            obj.append(MovingEntity([k, j - 1.83], Pintable(juego.suelo, juego.suelo.get_rect())))
    for k in range(-1000,1000,10):
            obj.append(MovingEntity([k,0], Pintable(juego.farola, juego.farola.get_rect())))
    return obj

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
        
    def simulate_pos(self, deltat, juego):
        self.velocity[0] += self.acceleration[0] * deltat
        self.velocity[1] += self.acceleration[1] * deltat
        self.coords[0] += self.velocity[0] * deltat
        self.coords[1] += self.velocity[1] * deltat
        if self.coords[1] < 0.0: 
            self.acceleration[1] = 0.0
            self.coords[1] = 0.0
        self.pintable.rect.bottom = -self.coords[1] * 30 + juego.config.getWindowALTO() - 20
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
        MovingEntity.__init__(self, initialcoords, initialimg)
        self.health = initialhealth
        self.name = name
        self.score = score
        self.status = "STILL"
        self.timeelapsed = 0 # Variable para guardar tiempos al andar
    def perform_jump(self):
        if self.coords[1] > 0.0: return
        self.velocity = [self.velocity[0], 5.0]
        self.acceleration = [self.acceleration[0], -9.8]
        
    def walk(self, deltat, direction, juego):
        """
        Direccion: FALSE Izquierda, TRUE Derecha
        """
        self.timeelapsed += deltat
        if self.timeelapsed >= 100:
            self.timeelapsed = 0
            if direction:
                if self.status == "STILL" or self.status == "R_3":
                    self.status = "R_0"
                    self.pintable = Pintable(juego.character["Walking_still"], juego.player.get_pintable().rect)
                elif self.status == "R_0":
                    self.status = "R_1"
                    self.pintable = Pintable(juego.character["Walking_1"], juego.player.get_pintable().rect)
                elif self.status == "R_1":
                    self.status = "R_2"
                    self.pintable = Pintable(juego.character["Walking_still"], juego.player.get_pintable().rect)
                elif self.status == "R_2":
                    self.status = "R_3"
                    self.pintable = Pintable(juego.character["Walking_2"], juego.player.get_pintable().rect)
            else:
                if self.status == "STILL" or self.status == "R_3":
                    self.status = "R_0"
                    self.pintable = Pintable(juego.character["Walking_still_L"], juego.player.get_pintable().rect)
                elif self.status == "R_0":
                    self.status = "R_1"
                    self.pintable = Pintable(juego.character["Walking_1_L"], juego.player.get_pintable().rect)
                elif self.status == "R_1":
                    self.status = "R_2"
                    self.pintable = Pintable(juego.character["Walking_still_L"], juego.player.get_pintable().rect)
                elif self.status == "R_2":
                    self.status = "R_3"
                    self.pintable = Pintable(juego.character["Walking_2_L"], juego.player.get_pintable().rect)
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
        self.character["Walking_still"] = load_image("images/walking-D-3.png", True)
        self.character["Walking_1"] = load_image("images/walking-D-1.png", True)
        self.character["Walking_2"] = load_image("images/walking-D-2.png", True)
        self.character["Walking_still_L"] = load_image("images/walking-I-3.png", True)
        self.character["Walking_1_L"] = load_image("images/walking-I-1.png", True)
        self.character["Walking_2_L"] = load_image("images/walking-I-2.png", True)
        self.suelo = load_image("images/suelo.png")
        self.game_background = load_image("images/background3.png")
        self.player = Player([0.0,0.0], Pintable(self.character["Still_front"], self.character["Still_front"].get_rect()), 100.0, "Juanan76", 0)
        self.farola = load_image("images/farola2.png", True)
        self.entities = generate_map(self)
        #self.entities.append(MovingEntity([-10.0,0], Pintable(self.farola, self.farola.get_rect())))
        #self.entities.append(MovingEntity([-20.0,0], Pintable(self.farola, self.farola.get_rect())))

    def complete_init(self, config):
        """
        Llamar cuando se ha completado el arranque y empezar a renderizar el menú.
        """
        self.config = config
        self.estado = "MENU"
        self.player.get_pintable().rect.centerx = self.config.getWindowANCHO() / 2
        self.player.get_pintable().rect.bottom = self.config.getWindowALTO() - 25

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
