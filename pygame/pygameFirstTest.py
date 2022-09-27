from dis import dis
import pygame
from sys import exit

width = 800
height = 400

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64,64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
test_font2 = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
cheat_mode = False
start_time = 0
score = 0

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# score_surf = test_font.render('My game', False, (64,64, 64))
# score_rect = score_surf.get_rect(center = (400, 50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (600,300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand_scaled = pygame.transform.scale(player_stand, (200, 400))
player_stand_rect = player_stand.get_rect(center = (200, 100))

game_name = test_font.render('Pixel Runner', False, (111, 196, 169))
game_name_scaled = pygame.transform.scale(game_name, (300, 200))
game_name_rect = game_name.get_rect(center = (500, 80))

game_name2 = test_font2.render('Pixel Runner', False, (0, 170, 0))
game_name_scaled2 = pygame.transform.scale(game_name2, (310,220))
game_name_rect2 = game_name2.get_rect(center = (495, 70))

game_message = test_font.render('Press space to run', False, (111, 196, 196))
game_message_rect = game_message.get_rect(center = (550, 250))

game_message2 = test_font2.render('Press space to run', False, (0, 170, 0))
game_message_rect2 = game_message2.get_rect(center = (548, 248))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:            ### event TYPE
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:         ### event KEY
                    player_gravity = -20
                if event.key == pygame.K_F10:
                    cheat_mode = True
                    print('Cheat mode - ENGAGE')
                if event.key == pygame.K_F9:
                    cheat_mode = False
                    print('Cheat mode - dis-engage')
        else:
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_F5 or event.key == pygame.K_SPACE):
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)

        if event.type == pygame.KEYUP:            ### event TYPE
            pass
    
    if game_active == True:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        # screen.blit(score_surf, score_rect)
        score = display_score()

        snail_rect.x -=4
        if snail_rect.right <= 0:
            snail_rect.left = 800

        if cheat_mode == True:
            if snail_rect.right == 196:
                player_gravity = -20

        screen.blit(snail_surface, snail_rect)

        # PLAYER
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand_scaled, player_stand_rect)
        screen.blit(ground_surface, (0,300))
        score_message = test_font.render(f'Your score: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (400, 370))

        if score == 0:
            # screen.blit(game_message, game_message_rect)
            screen.blit(score_message, score_message_rect)
            pass
        else:
            screen.blit(score_message, score_message_rect)
            
        pygame.draw.line(screen, 'red', (0,0), (width, height), 10)
        pygame.draw.line(screen, 'red', (width,0), (0, height), 10)
        screen.blit(game_name_scaled2, game_name_rect2) # title 1
        screen.blit(game_name_scaled, game_name_rect)   # title 2
        screen.blit(game_message2, game_message_rect2)
        screen.blit(game_message, game_message_rect)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print('jump')
    # if player_rect.colliderect(snail_rect):
    #     print('collision')



    pygame.display.update()
    clock.tick(60)  # computer will crash without this here slowing everything down.

