class InputBinding:
    def __init__(self, up, down, left=None, right=None, action=None):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.action = action


PLAYER_ONE_BINDING = InputBinding(up=pygame.K_w, down=pygame.K_s,
                                   action=pygame.K_SPACE)
PLAYER_TWO_BINDING = InputBinding(up=pygame.K_UP, down=pygame.K_DOWN,
                                   action=pygame.K_RETURN)


class ConfigurablePaddle(Entity):
    def __init__(self, x, y, binding, assets):
        image = assets.placeholder_image((14, 90), (230, 230, 230))
        super().__init__(image, x, y)
        self.binding = binding

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[self.binding.up]:
            self.velocity.y = -PADDLE_SPEED
        elif keys[self.binding.down]:
            self.velocity.y = PADDLE_SPEED
        else:
            self.velocity.y = 0
        super().update(dt)
