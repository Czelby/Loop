import pygame
import os


FPS = 6

WIDTH = 1600
HEIGHT = 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))


img_background = pygame.image.load(os.path.join("Base", "Assets", "Base_Background_updated.png"))
img_player = pygame.image.load(os.path.join("Base", "Assets", "player_model.png"))
img_chest_open = pygame.image.load(os.path.join("Base", "Assets", "Base_chest_open.png"))


def draw_base_window(player):
    WINDOW.blit(img_background, (0, 0))
    WINDOW.blit(img_player, (player.x, player.y))
    pygame.display.update()


def draw_chest_window():
    WINDOW.blit(img_chest_open, (0, 0))
    pygame.display.update()
