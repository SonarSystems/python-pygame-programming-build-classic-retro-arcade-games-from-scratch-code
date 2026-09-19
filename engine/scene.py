"""Base class for a game screen — a menu, a playing state, a game-over
screen. GameLoop calls handle_event/update/draw on whatever scene is
currently active."""
import pygame


class Scene:
    def __init__(self):
        self.sprites = pygame.sprite.Group()

    def handle_event(self, event):
        """Override to respond to a single Pygame event."""
        pass

    def update(self, dt):
        self.sprites.update(dt)

    def draw(self, surface):
        surface.fill((20, 20, 30))
        self.sprites.draw(surface)
