# Without Vector2 — considerably more error-prone:
thrust_x = math.cos(math.radians(angle - 90))
thrust_y = math.sin(math.radians(angle - 90))
velocity_x += thrust_x * THRUST_ACCELERATION * dt
velocity_y += thrust_y * THRUST_ACCELERATION * dt
speed = math.sqrt(velocity_x ** 2 + velocity_y ** 2)
if speed > MAX_SPEED:
    velocity_x = (velocity_x / speed) * MAX_SPEED
    velocity_y = (velocity_y / speed) * MAX_SPEED
