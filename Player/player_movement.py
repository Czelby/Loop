import pygame


PLAYER_VEL = 5


def player_movement(player):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.y -= PLAYER_VEL
    if keys[pygame.K_s]:
        player.y += PLAYER_VEL
    if keys[pygame.K_a]:
        player.x -= PLAYER_VEL
    if keys[pygame.K_d]:
        player.x += PLAYER_VEL
