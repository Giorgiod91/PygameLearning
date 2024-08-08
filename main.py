import pygame
import sys
from player import Player
from boss import DungeonBoss

# pygame setup
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dungeon Boss Guides")
clock = pygame.time.Clock()
running = True
player = Player(screen_width // 2, screen_height // 2, 50, 50, 5)
boss = DungeonBoss(screen_width // 4, screen_height // 4, 60, 60, 3)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
     # Handle player movement
    player.handle_movement()
    # Handle player ability
    player.useDef_Cd()

    # Draw the player
    player.draw(screen)

    boss.automated_movement()
    boss.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()