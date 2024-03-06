import pygame
from Base import draw_base_window, chest_base
from Player import player_model, player_movement


FPS = 60
WIDTH = 1600
HEIGHT = 800

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def base_home_window():
    player = player_model(WINDOW)
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        player_movement(player)     # handles player input for movement
        draw_base_window(player)    # creates the window for game
        item = chest_base()         # defines chest as an clickable object
        pos = pygame.mouse.get_pos()
        if pygame.MOUSEBUTTONUP:
            if item.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    return 1        # initiates opening chest in base
