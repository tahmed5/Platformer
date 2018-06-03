# game options
fps = 30
width = 480
height = 600
game_font = 'verdana'
hs_file = "highscore.txt"

#platforms
# x y w h 
PLATFORM_LIST = [(0, height - 40, width, 40),
                 ( width / 2 - 50, height * 3/4, 100, 20 ),
                 (125, height - 350, 100, 20 ),
                 (350, 200, 100, 20),
                 (175, 100, 100, 20),
                 ]

#player properties
player_acc = 0.5
player_friction = -0.12
gravity = 0.5
jump = 20

#colours
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
