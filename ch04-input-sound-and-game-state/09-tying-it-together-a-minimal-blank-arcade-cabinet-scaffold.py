import pygame

from engine.game_loop import GameLoop
from engine.scene import Scene
from engine.state_machine import StateMachine

WIDTH, HEIGHT = 800, 600


class MenuScene(Scene):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.font = pygame.font.Font(None, 48)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.app.states.transition_to("playing")

    def draw(self, surface):
        surface.fill((20, 20, 30))
        text = self.font.render("Press Enter to Start", True, (240, 240, 240))
        surface.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))


class PlayingScene(Scene):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.font = pygame.font.Font(None, 32)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.app.states.transition_to("menu")

    def draw(self, surface):
        surface.fill((30, 45, 30))
        text = self.font.render("Playing! (Esc to return to menu)", True, (240, 240, 240))
        surface.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))


class GameApp:
    def __init__(self, loop):
        self.loop = loop
        self.states = StateMachine("menu")
        self.scenes = {
            "menu": MenuScene(self),
            "playing": PlayingScene(self),
        }
        self.states.on_change(self._on_state_change)
        self.loop.set_scene(self.scenes["menu"])

    def _on_state_change(self, old_state, new_state):
        self.loop.set_scene(self.scenes[new_state])


if __name__ == "__main__":
    loop = GameLoop(WIDTH, HEIGHT, "Arcade Cabinet Scaffold")
    app = GameApp(loop)
    loop.run()
