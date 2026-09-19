import pygame

def update_jump_cut(self, keys):
    jump_held = keys[pygame.K_SPACE] or keys[pygame.K_UP]
    if not jump_held and self.velocity.y < 0:
        # Cut the upward velocity short if the key was released mid-rise.
        self.velocity.y *= 0.5
