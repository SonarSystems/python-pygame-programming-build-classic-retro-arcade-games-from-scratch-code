import pygame

class ArcadeCollectionMenu(Scene):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.font = pygame.font.Font(None, 36)
        self.games = [
            ("Pong", "games.pong.main", "launch_pong"),
            ("Breakout", "games.breakout.main", "launch_breakout"),
            ("Snake", "games.snake.main", "launch_snake"),
            # ... one entry per game ...
        ]
        self.selected_index = 0

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return
        if event.key == pygame.K_DOWN:
            self.selected_index = (self.selected_index + 1) % len(self.games)
        elif event.key == pygame.K_UP:
            self.selected_index = (self.selected_index - 1) % len(self.games)
        elif event.key == pygame.K_RETURN:
            import importlib
            name, module_path, launch_func = self.games[self.selected_index]
            module = importlib.import_module(module_path)
            getattr(module, launch_func)(self.app)

    def draw(self, surface):
        surface.fill((15, 15, 20))
        title = self.font.render("Arcade Collection", True, (240, 200, 40))
        surface.blit(title, (60, 40))
        for i, (name, _, _) in enumerate(self.games):
            color = (240, 240, 240) if i == self.selected_index else (140, 140, 140)
            text = self.font.render(name, True, color)
            surface.blit(text, (80, 120 + i * 44))
