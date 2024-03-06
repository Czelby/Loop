import pygame


PLAYER_WIDTH = 52
PLAYER_HEIGHT = 49
PLAYER_VEL = 5


def player_model(window):
    model = pygame.Rect(750, 650, PLAYER_WIDTH, PLAYER_HEIGHT)
    return model
