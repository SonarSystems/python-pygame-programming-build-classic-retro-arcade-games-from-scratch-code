def draw_debug_rects(surface, sprite_group, color=(255, 0, 255)):
    for sprite in sprite_group:
        pygame.draw.rect(surface, color, sprite.rect, width=1)
