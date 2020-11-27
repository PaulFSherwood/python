#!/usr/bin/python

import sys, pygame

pygame.init()

size = width, height = 600, 400

screen = pygame.display.set_mode(size)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.QUIT:sys.exit()
