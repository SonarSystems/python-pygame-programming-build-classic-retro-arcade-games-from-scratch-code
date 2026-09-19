def resolve_brick_collision(ball, brick):
    # Compare how far the ball's center has penetrated each axis to
    # decide whether this was primarily a horizontal or vertical hit.
    dx = ball.rect.centerx - brick.rect.centerx
    dy = ball.rect.centery - brick.rect.centery
    overlap_x = (ball.rect.width + brick.rect.width) / 2 - abs(dx)
    overlap_y = (ball.rect.height + brick.rect.height) / 2 - abs(dy)

    if overlap_x < overlap_y:
        ball.velocity.x *= -1
    else:
        ball.velocity.y *= -1
