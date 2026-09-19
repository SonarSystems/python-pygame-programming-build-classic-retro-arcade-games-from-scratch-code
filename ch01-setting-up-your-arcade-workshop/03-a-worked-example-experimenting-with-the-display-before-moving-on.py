import time

import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Experimenting")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((20, 20, 30))

    # Try changing these values and observing what happens:
    pygame.draw.circle(screen, (240, 200, 40), (400, 300), 50)
    pygame.draw.rect(screen, (80, 200, 120), (100, 100, 120, 60))
    pygame.draw.line(screen, (200, 80, 80), (0, 0), (800, 600), 3)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
