import pygame
import time

clock = pygame.time.Clock()

running = True
while running:
    dt_ms = clock.tick(60)
    dt = dt_ms / 1000.0  # convert milliseconds to seconds

    # ... process input ...

    ball_x += ball_speed_pixels_per_second * dt

    # ... render ...
