import pygame

from engine.entity import Entity

GRAVITY = 1450.0  # pixels per second^2
JUMP_VELOCITY = -560.0
MOVE_SPEED = 240.0


class Player(Entity):
    def __init__(self, x, y, assets):
        image = assets.placeholder_image((28, 40), (220, 120, 60))
        super().__init__(image, x, y)
        self.on_ground = False
        self.coyote_timer = 0.0
        self.coyote_duration = 0.1  # seconds of "still allowed to jump" after leaving a ledge

    def update(self, dt, solids):
        keys = pygame.key.get_pressed()
        self.velocity.x = 0
        if keys[pygame.K_LEFT]:
            self.velocity.x = -MOVE_SPEED
        elif keys[pygame.K_RIGHT]:
            self.velocity.x = MOVE_SPEED

        self.velocity.y += GRAVITY * dt

        if self.on_ground:
            self.coyote_timer = self.coyote_duration
        else:
            self.coyote_timer = max(0.0, self.coyote_timer - dt)

        self._move_and_collide(dt, solids)

    def try_jump(self):
        if self.on_ground or self.coyote_timer > 0:
            self.velocity.y = JUMP_VELOCITY
            self.coyote_timer = 0.0
