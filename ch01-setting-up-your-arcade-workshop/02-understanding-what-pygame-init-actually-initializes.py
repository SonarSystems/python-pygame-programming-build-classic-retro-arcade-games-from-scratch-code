import pygame

successes, failures = pygame.init()
if failures > 0:
    print(f"Warning: {failures} Pygame subsystem(s) failed to initialize")
