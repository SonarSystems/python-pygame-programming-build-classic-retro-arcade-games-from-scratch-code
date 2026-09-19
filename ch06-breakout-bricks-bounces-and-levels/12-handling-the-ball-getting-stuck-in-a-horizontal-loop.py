MIN_VERTICAL_RATIO = 0.15  # vertical speed must be at least this fraction of total speed

def prevent_horizontal_stall(ball):
    if abs(ball.velocity.y) < ball.speed * MIN_VERTICAL_RATIO:
        sign = 1 if ball.velocity.y >= 0 else -1
        ball.velocity.y = sign * ball.speed * MIN_VERTICAL_RATIO
        ball.velocity = ball.velocity.normalize() * ball.speed
