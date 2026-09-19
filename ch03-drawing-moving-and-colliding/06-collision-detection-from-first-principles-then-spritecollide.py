hit_bricks = pygame.sprite.spritecollide(ball, brick_group, dokill=True)
for brick in hit_bricks:
    score += 10
