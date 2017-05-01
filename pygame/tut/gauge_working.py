#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
011-rotozoom.py
moving, rotating and zooming a pygame surface
url: http://thepythongamebook.com/en:part2:pygame:step011
author: horst.jens@spielend-programmieren.at
licence: gpl, see http://www.gnu.org/licenses/gpl.html

loading the background image and snake.gif from a subfolder called 'data'
The subfolder must be inside the same folder as the program itself. 
The snake surface can be moved with the cursor keys, 
rotated with a and d key and and zoomed with w and s key.
"""
import pygame
import os

try:
    # load from subfolder 'data'
    # background = pygame.image.load(os.path.join("images","background640x480_a.jpg"))
    background = pygame.image.load(os.path.join("images","gauge.png"))
    # snake = pygame.image.load(os.path.join("images","snake.gif"))
    snake = pygame.image.load(os.path.join("images","needle.png"))
except:
    raise UserWarning, "Unable to find the images in the folder 'data' :-( "
#finally:
pygame.init()
screen=pygame.display.set_mode((600,600)) # try out larger values and see what happens !
# snake = snake.convert_alpha()           # png image has transparent color 
background = background.convert()         # jpg can not have transparency
snake_original = snake.copy()             # store a unmodified copy of the snake surface
snakex, snakey = 150, 165                 # start position of snake surface
dx, dy  = 0, 0                            # snake speed in pixel per second !
speed = 60                                # in pixel / second
angle = 0                                 # current orientation of snake
zoom = 1.0                                # current zoom factor
zoomspeed = 0.01                   
turnspeed = 180                           # in Grad (360) per second
screen.blit(background, (0,0))            # blit background on screen (overwriting all)
screen.blit(snake, (snakex, snakey))      # blit the snake shape 
clock = pygame.time.Clock()               # create pygame clock object 
mainloop = True
FPS = 60                                  # desired max. framerate in frames per second. 
while mainloop:
    milliseconds = clock.tick(FPS)        # milliseconds passed since last frame
    seconds = milliseconds / 1000.0       # seconds passed since last frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False              # pygame window closed by user
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False          # user pressed ESC
    pygame.display.set_caption("press cursor keys and a d - fps:"
        "%.2f angle %.2f" % (clock.get_fps(), angle))
                                          # only blit the part of the background where the snake was (cleanrect)
                                          # try:
                                          # if the subsurface is outside the screen pygame would raise an error
                                          # this can happen when using rotozoom, therfore check inside try..except
                                          # dirtyrect = background.subsurface((round(snakex,0), 
                                          # round(snakey,0), snake.get_width(), snake.get_height()))
                                          
                                          # screen.blit(dirtyrect, (round(snakex,0), round(snakey,0))) 
                                          # except:
                                          # print "autch!"
    snakerect = pygame.Rect(round(snakex,0), 
                round(snakey,0), snake.get_width(), snake.get_height())
    dirty = background.subsurface(snakerect.clip(screen.get_rect()))
    dirtyrect = dirty.get_rect()
    screen.blit(dirty, (round(snakex), round(snakey)))
        
    #screen.blit(background,(0,0)) # blit the whole background (slow but secure)
    #raise UserWarning, "subsurface out of screen?"
    # move snake with cursor keys
    pressedkeys = pygame.key.get_pressed()
    dx, dy  = 0, 0   # no cursor key, no movement
    
    #calculate new center of snake 
    snakex += dx * seconds # time based movement
    snakey += dy * seconds
    # rotate snake with a and d key
    turnfactor = 0  # neither a nor d, no turning
    if pressedkeys[pygame.K_a]:
        if angle >= 28.7:
            turnfactor = 0
        else:
            turnfactor += 1 # counter-clockwise
    if pressedkeys[pygame.K_d]:
        if angle <= -208:
            turnfactor = 0
        else:
            turnfactor -= 1 # clock-wise

    if turnfactor != 0:
        angle += turnfactor * turnspeed * seconds # time-based turning
        # the surface shrinks and zooms and moves by rotating
        oldrect = snake.get_rect() # store current surface rect
        snake = pygame.transform.rotozoom(snake_original, angle, zoom)
        newrect = snake.get_rect() # store new surface rect
        # put new surface rect center on same spot as old surface rect center
        snakex += oldrect.centerx - newrect.centerx
        snakey += oldrect.centery - newrect.centery

    # paint the snake    
    screen.blit(snake, (round(snakex,0), round(snakey,0)))

    pygame.display.flip()          # flip the screen 30 times a second                # flip the screen 30 (or FPS) times a second
