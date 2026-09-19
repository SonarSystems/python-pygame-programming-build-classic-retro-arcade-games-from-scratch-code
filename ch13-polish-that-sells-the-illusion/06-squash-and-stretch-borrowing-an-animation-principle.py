class SquashStretch:
    def __init__(self):
        self.scale_x = 1.0
        self.scale_y = 1.0

    def apply_impact(self):
        self.scale_x, self.scale_y = 1.3, 0.7  # flatten on impact

    def apply_stretch(self, velocity, max_stretch=0.3):
        speed_fraction = min(1.0, velocity.length() / 500.0)
        stretch = 1.0 + speed_fraction * max_stretch
        direction_angle = velocity.angle_to(pygame.Vector2(1, 0))
        # In a full implementation, this angle would orient the stretch
        # along the direction of travel using a rotated scale transform.
        self.scale_x, self.scale_y = stretch, 1.0 / stretch

    def update(self, dt, recovery_speed=8.0):
        self.scale_x += (1.0 - self.scale_x) * min(1.0, recovery_speed * dt)
        self.scale_y += (1.0 - self.scale_y) * min(1.0, recovery_speed * dt)

    def draw(self, surface, image, rect):
        scaled_size = (int(rect.width * self.scale_x), int(rect.height * self.scale_y))
        scaled_image = pygame.transform.scale(image, scaled_size)
        scaled_rect = scaled_image.get_rect(center=rect.center)
        surface.blit(scaled_image, scaled_rect)
