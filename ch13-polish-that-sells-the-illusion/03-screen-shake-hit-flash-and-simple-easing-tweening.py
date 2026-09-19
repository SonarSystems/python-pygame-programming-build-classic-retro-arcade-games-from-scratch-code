import pygame

def apply_hit_flash(sprite, duration=0.08):
    sprite.flash_timer = duration


def draw_with_flash(sprite, surface):
    if getattr(sprite, "flash_timer", 0) > 0:
        flash_image = sprite.image.copy()
        flash_image.fill((255, 255, 255, 255), special_flags=pygame.BLEND_RGBA_MULT)
        surface.blit(flash_image, sprite.rect)
    else:
        surface.blit(sprite.image, sprite.rect)
