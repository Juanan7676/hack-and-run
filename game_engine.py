from util import Pintable



def paint_game(juego):
    # 1: Character
    obj = []
    backpintable = Pintable(juego.game_background, juego.game_background.get_rect())
    obj.append(backpintable)
    pintable1 = Pintable(juego.character["Still_front"], juego.character["Still_front"].get_rect())
    pintable1.rect.centery = juego.config.getWindowALTO() - 75
    pintable1.rect.centerx = juego.config.getWindowANCHO() / 2
    suelop = Pintable(juego.suelo, juego.suelo.get_rect())
    suelop.rect.bottom = juego.config.getWindowALTO()
    suelop.rect.centerx = juego.config.getWindowANCHO() / 2
    for k in range(0, 20):
        for j in range(0,2):
            tmpx = Pintable(juego.suelo, juego.suelo.get_rect())
            tmpx.rect.bottom = juego.config.getWindowALTO() - 32 * j
            tmpx.rect.left = 32 * k
            obj.append(tmpx)
    obj.append(pintable1)
    return obj