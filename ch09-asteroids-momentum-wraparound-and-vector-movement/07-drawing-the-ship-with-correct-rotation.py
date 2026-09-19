import pygame

def draw(self, surface):
    rotated_image = pygame.transform.rotate(self.image, -self.angle)
    rotated_rect = rotated_image.get_rect(center=self.rect.center)
    surface.blit(rotated_image, rotated_rect)
