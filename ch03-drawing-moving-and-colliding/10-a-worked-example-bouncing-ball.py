import pygame

from engine.game_loop import GameLoop
from engine.entity import Entity
from engine.scene import Scene

WIDTH, HEIGHT = 800, 600


class Ball(Entity):
    def __init__(self):
        image = pygame.Surface((20, 20))
        image.fill((240, 200, 40))
        super().__init__(image, WIDTH // 2, HEIGHT // 2)
        self.velocity = pygame.Vector2(220, 160)

    def update(self, dt):
        super().update(dt)
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.velocity.x *= -1
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.velocity.y *= -1
        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))


class BouncingBallScene(Scene):
    def __init__(self):
        super().__init__()
        self.sprites.add(Ball())


if __name__ == "__main__":
    loop = GameLoop(WIDTH, HEIGHT, "Bouncing Ball")
    loop.set_scene(BouncingBallScene())
    loop.run()
