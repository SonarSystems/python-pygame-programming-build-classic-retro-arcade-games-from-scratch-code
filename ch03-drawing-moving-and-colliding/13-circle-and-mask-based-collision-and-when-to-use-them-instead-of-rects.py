def circles_collide(pos_a, radius_a, pos_b, radius_b):
    distance_squared = (pos_a[0] - pos_b[0]) ** 2 + (pos_a[1] - pos_b[1]) ** 2
    radius_sum = radius_a + radius_b
    return distance_squared < radius_sum ** 2
