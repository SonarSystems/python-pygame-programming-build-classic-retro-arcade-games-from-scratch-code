def elastic_collision_2d(pos_a, vel_a, mass_a, pos_b, vel_b, mass_b):
    """Returns the new velocities for both objects after an elastic
    collision, using the standard 2D elastic collision formula."""
    normal = (pygame.Vector2(pos_b) - pygame.Vector2(pos_a))
    if normal.length_squared() == 0:
        return vel_a, vel_b
    normal = normal.normalize()

    relative_velocity = vel_a - vel_b
    velocity_along_normal = relative_velocity.dot(normal)

    if velocity_along_normal > 0:
        return vel_a, vel_b  # already moving apart, no response needed

    impulse_scalar = -(2 * velocity_along_normal) / (1 / mass_a + 1 / mass_b)
    impulse = normal * impulse_scalar

    new_vel_a = vel_a + impulse / mass_a
    new_vel_b = vel_b - impulse / mass_b
    return new_vel_a, new_vel_b
