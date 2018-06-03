import pygame as pg
from settings import *
from spritesf import *
from os import path
import random

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((width,height))
        pg.display.set_caption("Platformer")
        self.fps = pg.time.Clock()
        self.running = True
        self.game_font = pg.font.match_font(game_font)
        self.load_data()

    def load_data(self):

        with open(hs_file, 'w') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0 

    def new(self):
        self.score = 0
        self.sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.sprites.add(self.player)

        for platform in PLATFORM_LIST:
            p = Platform(*platform)
            self.sprites.add(p)
            self.platforms.add(p)
            
        
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.fps.tick(60)
            self.events()
            self.update()
            self.draw()
        

    def update(self):
        self.sprites.update()
        if self.player.vel.y > 0:          
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top  + 1
                self.player.vel.y = 0

        if self.player.rect.top <= height/4:
            self.player.pos.y += abs(self.player.vel.y)
            for platform in self.platforms:
                platform.rect.y += abs(self.player.vel.y)
                if platform.rect.top >= height:
                    platform.kill()
                    self.score += 10

        while len(self.platforms) < 5:
            w = random.randint(50,100)
            p = Platform(random.randrange(0,width - w), random.randrange(-75, - 30),w, 20)
            self.platforms.add(p)
            self.sprites.add(p)

        if self.player.rect.bottom > height:
            for sprite in self.sprites:
                sprite.rect.y -= max(self.player.vel.y , 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
                    
        if len(self.platforms) == 0:
            self.playing = False
            


    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
                
    def draw(self):
        self.screen.fill(black)
        self.sprites.draw(self.screen)
        self.draw_text(str(self.score) , 22, white, width/2, 15)
        pg.display.flip()

    def start_screen(self):
        self.screen.fill(black)
        self.draw_text('Good Nice Game', 48, white , width/2, height/4)
        self.draw_text("Arrows to move, Space to Jump", 22, white, width/2 , height/2)
        self.draw_text("Press a key to play", 22, white, width/2 , height *3/4)
        self.draw_text("High Score: " + str(self.highscore), 22, white, width/2 , 15) 
        pg.display.flip()
        self.wait_for_key()

    def end_screen(self):
        if not self.running:
            return
            
        
        self.screen.fill(black)
        self.draw_text('Game Over', 48, white , width/2, height/4)
        self.draw_text("Score:" + str(self.score) , 22, white, width/2 , height/2)
        self.draw_text("Press a key to play again", 22, white, width/2 , height *3/4)
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text("NEW HIGH SCORE: " + str(self.highscore), 22, white, width/2 , height/2 + 40)
            with open(hs_file, 'w') as f:
                f.write(str(self.score))

        else:
            self.draw_text("High Score: " + str(self.highscore), 22, white, width/2 , height/2 + 40)             
            
        pg.display.flip()
        self.wait_for_key()

    def draw_text(self, text, size, colour, x,y):
        font = pg.font.Font(self.game_font, size)
        text_surface = font.render(text, True, colour)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.fps.tick(60)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False

                if event.type == pg.KEYUP:
                    waiting = False
    

g = Game()
g.start_screen()

while g.running:
    g.new()
    g.end_screen()
    
pg.quit()
