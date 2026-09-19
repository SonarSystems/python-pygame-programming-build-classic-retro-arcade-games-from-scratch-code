def apply_powerup(scene, kind):
    if kind == "widen":
        scene.paddle.grow(1.6, duration=8.0)
    elif kind == "slow":
        for ball in scene.balls:
            ball.speed_multiplier = 0.6
        scene.slow_timer = 6.0
    elif kind == "multiball":
        scene.spawn_extra_ball()
