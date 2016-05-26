import sys, pygame, thread, math, random
from pygame.locals import * 
from pygame import time as pytime
from threading import Thread
from util import Pintable
# Constantes
ANCHO = 640
ALTO = 480
# Clases
# ---------------------------------------------------------------------

class Pong_context():
    def __init__(self, juego):
        self.bola = Bola()
        self.pala1 = Pala(28)
        self.pala2 = Pala(juego.config.getWindowANCHO() - 28)
        self.marcador = [0 , 0]
        self.deltat = 0
        self.obj = []
    def update_deltat(self, deltat):
        self.deltat = deltat

class Bola(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/ball.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO / 2
        self.rect.centery = ALTO / 2
        self.speed = [2, 2]
        
    def actualizar(self, time, pala1, pala2, marcador):
        self.rect.centerx += self.speed[0] * time
        self.rect.centery += self.speed[1] * time
        if self.rect.left <= 0:
            random.random()
            for k in range(0, random.randint(1,2)):
                self.speed[0] = -self.speed[0]
            for k in range(0, random.randint(1,2)):
                self.speed[1] = -self.speed[1]
            self.rect.centerx = ANCHO / 2
            self.rect.centery = ALTO / 2
            marcador[1] += 1
            return True
        elif self.rect.right >= ANCHO:
            random.random()
            for k in range(0, random.randint(1,2)):
                self.speed[0] = -self.speed[0]
            for k in range(0, random.randint(1,2)):
                self.speed[1] = -self.speed[1]
            self.rect.centerx = ANCHO / 2
            self.rect.centery = ALTO / 2
            marcador[0] += 1
            return True
        elif check_collision(self,pala1):
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
            return False
        elif check_collision(self,pala2,"d"):
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
            return False
        elif self.rect.top <= 0 or self.rect.bottom >= ALTO:
            self.speed[1] = -self.speed[1]
            self.rect.centery += math.ceil(self.speed[1] * time)
            return False
            
class Pala(pygame.sprite.Sprite):
    
    def __init__(self,posx):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/pala.png", False)
        self.rect = self.image.get_rect()
        self.rect.centerx = posx
        self.rect.centery = ALTO / 2
        
    def move(self, keys, second = False):
        if keys[K_w] and self.rect.top > 0 and not second:
            self.rect.centery -= 3
        elif keys[K_s] and self.rect.bottom < ALTO and not second:
            self.rect.centery += 3
        elif keys[K_UP] and self.rect.top > 0 and second:
            self.rect.centery -= 3
        elif keys[K_DOWN] and self.rect.bottom < ALTO and second:
            self.rect.centery += 3
        
# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------
def load_image(filename, transparent=False):
    try: image = pygame.image.load(filename)
    except pygame.error, message:
        raise SystemExit, message
    image = image.convert()
    if transparent:
        color = image.get_at((0,0))
        image.set_colorkey(color, RLEACCEL)
    return image


#def get_fps(frames, antes, despues):

def update_ball(bola, pala1, pala2, marcador, deltat):
    if bola.actualizar(deltat / 1000, pala1, pala2, marcador):
        pala1.rect.centery = ALTO / 2
        pala2.rect.centery = ALTO / 2
    keys = pygame.key.get_pressed()
    pala1.move(keys)
    pala2.move(keys,True)
    thread.exit()
        
def check_collision(bola, pala, direccion = "i"):
    bYt = bola.rect.top
    bYb = bola.rect.bottom
    pYt = pala.rect.top
    pYb = pala.rect.bottom
    if direccion == "i":
        bX = bola.rect.left
        pX = pala.rect.right
        return (bX < pX) and (bYt <= pYb and bYb >= pYt)
    elif direccion == "d":
        bX = bola.rect.right
        pX = pala.rect.left
        return (bX > pX) and (bYt <= pYb and bYb >= pYt)
    else: raise Exception("check_collision solo puede aceptar de direcciones \"i\" o \"d\"!")
# ---------------------------------------------------------------------

def start_pong(context):
    context.obj = []
    background_image = load_image('images/fondo_pong.png')
    context.obj.append(Pintable(background_image, background_image.get_rect()))
    update_ball(context.bola, context.pala1, context.pala2, context.marcador, context.deltat)
    fuente = pygame.font.SysFont("calibri", 40)
    context.obj.append(Pintable(context.bola.image, context.bola.rect))
    context.obj.append(Pintable(context.pala1.image, context.pala1.rect))
    context.obj.append(Pintable(context.pala2.image, context.pala2.rect))
    marcador1 = fuente.render(str(context.marcador[0]), 1, (255,255,255))
    marcador2 = fuente.render(str(context.marcador[1]), 1, (255,255,255))
    marcador1r = marcador1.get_rect()
    marcador2r = marcador2.get_rect()
    marcador1r.centerx = ANCHO / 2 - 30
    marcador2r.centerx = ANCHO / 2 + 10
    marcador1r.centery = marcador2r.centery = 20
    context.obj.append(marcador1, marcador1r)
    context.obj.append(marcador2, marcador2r)
    return True
