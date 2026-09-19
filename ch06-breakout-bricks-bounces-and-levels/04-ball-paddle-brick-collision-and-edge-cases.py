hits = pygame.sprite.spritecollide(self.ball, self.bricks, dokill=False)
if hits:
    brick = hits[0]
    resolve_brick_collision(self.ball, brick)
    self.score += brick.points
    self.hit_sound.play()
    brick.kill()
