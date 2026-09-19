def draw_snake(surface, snake, assets):
    for i, (col, row) in enumerate(snake.body):
        x, y = col * GRID_SIZE, row * GRID_SIZE
        rect = pygame.Rect(x, y, GRID_SIZE - 2, GRID_SIZE - 2)
        if i == 0:
            pygame.draw.rect(surface, (240, 220, 60), rect)
            eye_offset = pygame.Vector2(snake.direction) * (GRID_SIZE // 4)
            eye_pos = (rect.centerx + eye_offset.x, rect.centery + eye_offset.y)
            pygame.draw.circle(surface, (20, 20, 30), eye_pos, 3)
        else:
            # Slightly darken each successive segment toward the tail,
            # giving the snake a subtle gradient rather than a flat block.
            fade = max(0.4, 1.0 - (i / len(snake.body)) * 0.5)
            color = (int(90 * fade), int(200 * fade), int(90 * fade))
            pygame.draw.rect(surface, color, rect)
