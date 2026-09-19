def _move_and_collide(self, dt, solids):
    self.rect.x += self.velocity.x * dt
    for solid in solids:
        if self.rect.colliderect(solid.rect):
            if self.velocity.x > 0:
                self.rect.right = solid.rect.left
            elif self.velocity.x < 0:
                self.rect.left = solid.rect.right

    self.rect.y += self.velocity.y * dt
    self.on_ground = False
    for solid in solids:
        if self.rect.colliderect(solid.rect):
            if self.velocity.y > 0:
                self.rect.bottom = solid.rect.top
                self.velocity.y = 0
                self.on_ground = True
            elif self.velocity.y < 0:
                self.rect.top = solid.rect.bottom
                self.velocity.y = 0
