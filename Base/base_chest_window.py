import pygame
from Base import draw_chest_window


FPS = 60
clock = pygame.time.Clock()


def base_chest_window():
    clock.tick(FPS)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_chest_window()


