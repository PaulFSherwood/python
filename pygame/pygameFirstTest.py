from dis import dis
import pygame
from random import randint, choice
from sys import exit



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('audio/audio_jump.mp3')
        self.jump_sound.set_volume(0.2)
    
    def player_intput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()
    
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_intput()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        
        if type == 'fly':
            fly_1 = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
            fly_2 = pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210
        else:
            snail_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
            self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

width = 800
height = 400

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64,64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

# def obstacle_movement(obstacle_list):
#     if obstacle_list:
#         for obstacle_rect in obstacle_list:
#             obstacle_rect.x -= 5

#             if obstacle_rect.bottom == 300:
#                 screen.blit(snail_surface, obstacle_rect)
#             else:
#                 screen.blit(fly_surface, obstacle_rect)

#         obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

#         return obstacle_list
#     else: return []

# def collisions(player, obstacles):
#     if obstacles:
#         for obstacles_rect in obstacles:
#             if player.colliderect(obstacles_rect):
#                 return False
#     return True

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, True):
        # obstacle_group.empty()
        return False
    return True

# def player_animation():
#     global player_surf, player_index
#     # play walking animation if the player is on the floor
#     # play jump aniimation if the player is off of the floor
#     if player_rect.bottom < 300:
#         player_surf = player_jump
#     else:
#         player_index += 0.1
#         if player_index >= len(player_walk):
#             player_index = 0
#         player_surf = player_walk[int(player_index)]


pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
test_font2 = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

# GROUPS
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

game_sound = pygame.mixer.Sound('audio/music.wav')
game_sound.set_volume(0.1)

# score_surf = test_font.render('My game', False, (64,64, 64))
# score_rect = score_surf.get_rect(center = (400, 50))

# Obstacles
# snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
# snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
# snail_frames = [snail_frame_1, snail_frame_2]
# snail_frame_index = 0
# snail_surface = snail_frames[snail_frame_index]

# fly_frame_1 = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
# fly_frame_2 = pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()
# fly_frames = [fly_frame_1, fly_frame_2]
# fly_frame_index = 0
# fly_surface = fly_frames[fly_frame_index]

# obstacle_rect_list = []

# player_walk_1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
# player_walk_2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
# player_walk = [player_walk_1, player_walk_2]
# player_index = 0
# player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()

# player_surf = player_walk[player_index]
# player_rect = player_surf.get_rect(midbottom = (80, 300))
# player_gravity = 0
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


# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1800)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            game_sound.play(loops = -1)
            # if event.type == pygame.MOUSEBUTTONDOWN:
                # if player_rect.collidepoint(event.pos):
                    # player_gravity = -20
            if event.type == pygame.KEYDOWN:            ### event TYPE
                if event.key == pygame.K_SPACE: # and player_rect.bottom >= 300:         ### event KEY
                    player_gravity = -20
                # if event.key == pygame.K_F10:
                #     cheat_mode = True
                #     print('Cheat mode - ENGAGE')
                # if event.key == pygame.K_F9:
                #     cheat_mode = False
                #     print('Cheat mode - dis-engage')
        else:
            game_sound.fadeout(250)
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_F5 or event.key == pygame.K_SPACE):
                game_active = True
                # snail_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)

        if event.type == pygame.KEYUP:            ### event TYPE
            pass
        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))

                # if randint(0, 2):
                #     obstacle_rect_list.append(snail_surface.get_rect(bottomright = (randint(900, 1100),150)))
                # else:
                #     obstacle_rect_list.append(fly_surface.get_rect(bottomright = (randint(900, 1100),300)))
            # if event.type == snail_animation_timer:
            #     if snail_frame_index == 0: snail_frame_index = 1
            #     else: snail_frame_index = 0
            #     snail_surface = snail_frames[snail_frame_index]

            # if event.type == fly_animation_timer:
            #     if fly_frame_index == 0: fly_frame_index = 1
            #     else: fly_frame_index = 0
            #     fly_surface = fly_frames[fly_frame_index]

    if game_active == True:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        # screen.blit(score_surf, score_rect)
        score = display_score()

        # snail_rect.x -=4
        # if snail_rect.right <= 0:
        #     snail_rect.left = 800
        # screen.blit(snail_surface, snail_rect)

        # PLAYER
        # player_gravity += 1
        # player_rect.y += player_gravity
        # if player_rect.bottom >= 300: player_rect.bottom = 300
        # player_animation()
        # screen.blit(player_surf, player_rect)
        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        # Obstacle movement
        # obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        # print(len(obstacle_rect_list))

        # collision
        game_active = collision_sprite()
        # game_active = collisions(player_rect, obstacle_rect_list)
        # if snail_rect.colliderect(player_rect):
        #     game_active = False
    else:
        # reset entities and player
        # obstacle_rect_list.clear()
        # player_rect.midbottom = (80, 300)
        player_gravity = 0

        screen.fill((94, 129, 162))
        screen.blit(player_stand_scaled, player_stand_rect)
        screen.blit(ground_surface, (0,300))
        score_message = test_font.render(f'Your score: {score}', False, (111, 196, 169))
        score_message2 = test_font2.render(f'Your score: {score}', False, (0, 170, 0))
        score_message_rect = score_message.get_rect(center = (400, 370))
        score_message_rect2 = score_message2.get_rect(center = (402, 372))

        if score == 0:
            # screen.blit(game_message, game_message_rect)
            screen.blit(score_message, score_message_rect)
            screen.blit(score_message2, score_message_rect2)
            pass
        else:
            screen.blit(score_message, score_message_rect)
            screen.blit(score_message2, score_message_rect2)
            
        # pygame.draw.line(screen, 'red', (0,0), (width, height), 10)
        # pygame.draw.line(screen, 'red', (width,0), (0, height), 10)
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
