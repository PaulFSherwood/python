#!/usr/bin/python

import sys, pygame, glob
from pygame import *

pygame.init()

size = width, height = 500, 500

# initialise
screen = pygame.display.set_mode(size)
mario = pygame.image.load("mario.png")
gauge = pygame.image.load("gauge.png")
needle_rot = pygame.image.load("needle.png")

class needle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.ani_speed_init = 10
        self.ani_speed = self.ani_speed_init
        self.ani = glob.glob("images/needle*.png")
        self.ani.sort()
        self.ani_pos = 0
        self.ani_max = len(self.ani) - 1
        self.img = pygame.image.load(self.ani[0])
        self.update(0)
    def update (self, pos):
        if pos != 0:
            self.ani_speed-=1
            self.x+=pos
            if self.ani_speed == 0:
                self.img = pygame.image.load(self.ani[self.ani_pos])
                self.ani_speed = self.ani_speed_init
                if self.ani_pos == self.ani_max:
                    self.ani_pos = 0
                else:
                    self.ani_pos += 1

        screen.blit(self.img, (0, 0))

# needle1 = needle()
pos = 0

angle = 0


clock = pygame.time.Clock()
# 120  168  192

x = 0
y = 0

# keys
up    = False
down  = False
left  = False
right = False

running = True
# loop
while running:
    for event in pygame.event.get():

        # events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_UP:
                up = True
            if event.key == pygame.K_DOWN:
                down = True
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_DOWN:
                down = False
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False

        if event.type == pygame.QUIT:sys.exit()


    clock.tick(60)

    # render
    # clear the screen
    screen.fill((0, 0, 0))
    # screen.blit(mario, (x, y))
    # pygame.display.flip()
    screen.blit(gauge, (50, 50))

    # rotate image
    image_rotate = pygame.transform.rotate(needle_rot, angle)

    # needle1.update(pos)
    screen.blit(image_rotate, (50, 50))

    pygame.display.update()

    # logic
    if up == True:
        y = y - 1
    elif down == True:
        y = y + 1
    elif left == True:
        x = x - 1
        pos - 1
        angle -= 1
    elif right == True:
        x = x + 1
        pos = 1
        angle += 1

    # collision
    if x > 575:
        x = 575
    if y > 360:
        y = 360
    if x < 0:
        x = 0
    if y < 0:
        y = 0

