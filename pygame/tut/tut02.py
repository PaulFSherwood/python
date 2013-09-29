#!/usr/bin/python

import sys, pygame

pygame.init()

size = width, height = 315, 315

# screen surface
screen = pygame.display.set_mode(size)

######################################

running = True
# create variable for degrees for roation
degree = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.QUIT:sys.exit()

    # clear the screen
    screen.fill((40, 40, 40))

    surf = pygame.Surface((100, 100))
    surf.fill((255,255,255))
    
    # load image
    gauge = pygame.image.load("gauge.png")

    # create the needle surface
    needle = pygame.image.load("needle.png")

    rect_needle = needle.get_rect()

    pygame.draw.rect(surf, (100, 0, 0), rect_needle)
    # static image placement
    where = 0, 0
    
    # push static image to screen
    screen.blit(gauge, (0, 0))

    # draw 
    # blittedRect = screen.blit(screen, where)

    # oldCenter = blittedRect.center
    
    # rotate_needle = pygame.transform.rotate(needle, degree)
    
    # rotRect = rotate_needle.get_rect()
    
    # screen.blit(rotate_needle, rotRect)

    #change the degree of rotation
    degree += 5
    if degree > 360:
        degree = 0

    pygame.display.flip()
    
    pygame.time.wait(60)
