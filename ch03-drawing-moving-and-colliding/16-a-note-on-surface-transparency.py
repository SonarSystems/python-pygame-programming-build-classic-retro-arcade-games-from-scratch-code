import pygame

surface = pygame.Surface((width, height), pygame.SRCALPHA)
surface.fill((0, 0, 0, 0))  # fully transparent
pygame.draw.circle(surface, (240, 80, 80, 200), (width // 2, height // 2), 20)
