class PausedScene(Scene):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.font = pygame.font.Font(None, 48)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.app.states.transition_to("playing")

    def draw(self, surface):
        # Draw the frozen playing-scene frame underneath, then dim it,
        # so the player can still see the game state they paused on.
        self.app.scenes["playing"].draw(surface)
        overlay = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 140))
        surface.blit(overlay, (0, 0))
        text = self.font.render("PAUSED", True, (240, 240, 240))
        surface.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
