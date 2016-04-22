import pygame
from pygame.locals import RLEACCEL

class Pintable():
    def __init__(self, surf, rect):
        self.assoc = surf
        self.rect = rect
    def set_rect(self, rect):
        self.rect = rect
    def get_rect(self):
        return self.rect
    def get_assoc(self):
        return self.assoc

def load_image(filename, transparent=False):
    try: image = pygame.image.load(filename)
    except pygame.error, message:
        raise SystemExit, message
    image = image.convert()
    if transparent:
        color = image.get_at((0,0))
        image.set_colorkey(color, RLEACCEL)
    return image
