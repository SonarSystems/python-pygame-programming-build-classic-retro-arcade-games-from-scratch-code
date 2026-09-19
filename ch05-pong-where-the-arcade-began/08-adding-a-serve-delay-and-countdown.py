SERVE_DELAY = 1.2


class PlayingScene(Scene):
    def __init__(self, app):
        # ... existing __init__ body ...
        self.serve_timer = SERVE_DELAY
        self.awaiting_serve = True

    def update(self, dt):
        if self.awaiting_serve:
            self.serve_timer -= dt
            if self.serve_timer <= 0:
                self.awaiting_serve = False
            return  # freeze gameplay during the countdown

        super().update(dt)
        # ... existing collision and scoring logic ...

    def start_serve_countdown(self, direction):
        self.ball.reset(direction=direction)
        self.serve_timer = SERVE_DELAY
        self.awaiting_serve = True

    def draw(self, surface):
        super().draw(surface)
        # ... existing score drawing ...
        if self.awaiting_serve:
            countdown_text = self.font.render(str(int(self.serve_timer) + 1),
                                               True, (240, 240, 240))
            surface.blit(countdown_text,
                        countdown_text.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
