import pygame

class ScoreDisplay:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)  # created once

    def draw(self, surface, score, position):
        text_surface = self.font.render(f"Score: {score}", True, (240, 240, 240))
        surface.blit(text_surface, position)
