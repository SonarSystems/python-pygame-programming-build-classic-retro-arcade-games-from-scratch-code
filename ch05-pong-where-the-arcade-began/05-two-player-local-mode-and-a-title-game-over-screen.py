class MenuScene(Scene):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.font = pygame.font.Font(None, 40)
        self.small_font = pygame.font.Font(None, 26)

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return
        if event.key == pygame.K_1:
            self.app.two_player = False
            self.app.states.transition_to("playing")
        elif event.key == pygame.K_2:
            self.app.two_player = True
            self.app.states.transition_to("playing")

    def draw(self, surface):
        surface.fill((20, 20, 30))
        title = self.font.render("PONG", True, (240, 240, 240))
        surface.blit(title, title.get_rect(center=(WIDTH // 2, 200)))
        opt1 = self.small_font.render("Press 1 for One Player (vs CPU)", True, (200, 200, 200))
        opt2 = self.small_font.render("Press 2 for Two Player", True, (200, 200, 200))
        surface.blit(opt1, opt1.get_rect(center=(WIDTH // 2, 320)))
        surface.blit(opt2, opt2.get_rect(center=(WIDTH // 2, 356)))


class GameOverScene(Scene):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.font = pygame.font.Font(None, 48)
        self.small_font = pygame.font.Font(None, 26)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.app.states.transition_to("menu")

    def draw(self, surface):
        surface.fill((20, 20, 30))
        playing = self.app.scenes["playing"]
        winner = "Left Player" if playing.left_score > playing.right_score else "Right Player"
        text = self.font.render(f"{winner} Wins!", True, (240, 200, 40))
        surface.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20)))
        prompt = self.small_font.render("Press Enter for Menu", True, (200, 200, 200))
        surface.blit(prompt, prompt.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30)))
