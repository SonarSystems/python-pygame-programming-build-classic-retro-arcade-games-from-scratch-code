"""A reusable, frame-rate-independent game loop.

Any game built in this book supplies a `Scene`-like object with
`handle_event(event)`, `update(dt)`, and `draw(surface)` methods, and
GameLoop takes care of the event queue, delta time, and frame capping.
"""
import sys

import pygame


class GameLoop:
    def __init__(self, width, height, title, fps=60):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.running = False
        self.scene = None

    def set_scene(self, scene):
        self.scene = scene

    def run(self):
        self.running = True
        while self.running:
            dt = self.clock.tick(self.fps) / 1000.0
            dt = min(dt, 0.05)  # clamp so a stutter can't cause a huge jump

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif self.scene is not None:
                    self.scene.handle_event(event)

            if self.scene is not None:
                self.scene.update(dt)
                self.scene.draw(self.screen)

            pygame.display.flip()

        pygame.quit()
        sys.exit()
