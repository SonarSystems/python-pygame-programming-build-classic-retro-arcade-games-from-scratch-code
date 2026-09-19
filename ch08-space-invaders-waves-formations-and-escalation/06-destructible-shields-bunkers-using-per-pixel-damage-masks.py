import pygame

def resolve_shield_hits(bullet_group, shield_blocks):
    for bullet in list(bullet_group):
        hit_blocks = pygame.sprite.spritecollide(bullet, shield_blocks, dokill=True)
        if hit_blocks:
            bullet.kill()
