import pygame, sys
from settings import *
from level import Level
from tiles import Tile
#importing pygame and other files into the main python file here

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_maps[0], screen)
#creating a screen with a set width and height (of desired pixels), stored as the above variables in a different file 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('blue')
    level.run()
    pygame.display.update()
    clock.tick(60)


#this runs the actual game, running a for loop inside of a while loop
