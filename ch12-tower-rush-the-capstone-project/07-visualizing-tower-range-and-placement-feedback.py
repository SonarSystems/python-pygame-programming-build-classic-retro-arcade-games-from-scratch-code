def draw_range_preview(surface, position, tower_range, valid):
    overlay = pygame.Surface((tower_range * 2, tower_range * 2), pygame.SRCALPHA)
    color = (80, 200, 120, 60) if valid else (200, 70, 70, 60)
    pygame.draw.circle(overlay, color, (tower_range, tower_range), tower_range)
    pygame.draw.circle(overlay, color[:3] + (140,), (tower_range, tower_range),
                       tower_range, width=2)
    surface.blit(overlay, (position[0] - tower_range, position[1] - tower_range))
