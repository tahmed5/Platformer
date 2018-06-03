import pygame as pg
from settings import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self,game):
        pg.sprite.Sprite.__init__(self)
        self.game = game 
        self.image = pg.Surface((30,40))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)
        self.pos = vec(width/2, height/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self,self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -jump
        
        
    def update(self):
        self.acc = vec(0,gravity)
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -player_acc

        if keys[pg.K_d]:
            self.acc.x = player_acc

        self.acc.x += self.vel.x * player_friction #friction
        #equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > width:
            self.pos.x = 0

        if self.pos.x < 0:
            self.pos.x = width

        self.rect.midbottom = self.pos
        
class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        
        
        
        
