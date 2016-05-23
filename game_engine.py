import pygame
from util import Pintable
from input_thread import controls
from pygame.locals import K_RIGHT, K_LEFT, K_UP
def paint_game(juego):
    # 1: Character
    obj = []
    backpintable = Pintable(juego.game_background, juego.game_background.get_rect())
    obj.append(backpintable)
    suelop = Pintable(juego.suelo, juego.suelo.get_rect())
    suelop.rect.bottom = juego.config.getWindowALTO()
    suelop.rect.centerx = juego.config.getWindowANCHO() / 2
    #for k in range(0, 20):
    #    for j in range(0,2):
    #        tmpx = Pintable(juego.suelo, juego.suelo.get_rect())
    #        tmpx.rect.bottom = juego.config.getWindowALTO() - 32 * j
    #        tmpx.rect.left = 32 * k
    #        obj.append(tmpx)
    for entity in juego.entities:
        tmp = entity.pintable
        coords = entity.coords
        centercoords = juego.player.coords
        diff = [coords[0] - centercoords[0], coords[1] - centercoords[1]]
        tmp.rect.centerx = juego.player.pintable.rect.centerx + diff[0] * 30
        tmp.rect.bottom = juego.config.getWindowALTO() - entity.coords[1] * 30 - 55
        obj.append(tmp)
    obj.append(juego.player.get_pintable())
    return obj

def game_loop(juego):
    while True:
        pygame.time.delay(25)
        if juego.estado != "PARTIDA": continue
        print juego.player.coords
        deltat = 25
        controles = controls(juego)
        if controles[K_RIGHT]:
            juego.player.update_velocity([3.0, juego.player.velocity[1]])
            juego.player.walk(deltat, True, juego)
        elif controles[K_LEFT]:
            juego.player.update_velocity([-3.0, juego.player.velocity[1]])
            juego.player.walk(deltat, False, juego)
        elif controles[K_UP] and juego.player.coords[1] == 0.0:
            juego.player.perform_jump()
        else:
            if juego.player.coords[1] == 0.0: juego.player.update_velocity([0.0, 0.0])
            juego.player.pintable = Pintable(juego.character["Still_front"], juego.player.get_pintable().rect)
        juego.player.simulate_pos(float(deltat) / 1000.0, juego)
        