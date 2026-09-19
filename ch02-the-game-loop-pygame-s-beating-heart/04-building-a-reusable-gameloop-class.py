class BlinkingSquareScene:
    def __init__(self):
        self.x = 100.0
        self.speed = 200.0  # pixels per second

    def handle_event(self, event):
        pass

    def update(self, dt):
        self.x += self.speed * dt
        if self.x > 700:
            self.x = 100.0

    def draw(self, surface):
        surface.fill((20, 20, 30))
        pygame.draw.rect(surface, (240, 200, 40), (self.x, 280, 40, 40))


if __name__ == "__main__":
    from engine.game_loop import GameLoop

    loop = GameLoop(800, 600, "Delta Time Demo")
    loop.set_scene(BlinkingSquareScene())
    loop.run()
