import pygame

class SecondPlayerPaddle(Paddle):
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.velocity.y = -PADDLE_SPEED
        elif keys[pygame.K_DOWN]:
            self.velocity.y = PADDLE_SPEED
        else:
            self.velocity.y = 0
        super().update(dt)
        self.clamp_to_screen()
