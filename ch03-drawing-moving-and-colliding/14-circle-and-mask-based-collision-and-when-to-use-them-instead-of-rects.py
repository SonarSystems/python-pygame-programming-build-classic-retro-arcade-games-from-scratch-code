def masks_collide(sprite_a, sprite_b):
    mask_a = pygame.mask.from_surface(sprite_a.image)
    mask_b = pygame.mask.from_surface(sprite_b.image)
    offset = (sprite_b.rect.x - sprite_a.rect.x, sprite_b.rect.y - sprite_a.rect.y)
    return mask_a.overlap(mask_b, offset) is not None
