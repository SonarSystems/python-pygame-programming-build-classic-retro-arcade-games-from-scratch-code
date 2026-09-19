import pygame

from engine.scene import Scene

WIN_SCORE = 11


class PlayingScene(Scene):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.assets = app.assets
        self.left_score = 0
        self.right_score = 0
        self.font = pygame.font.Font(None, 64)

        self.ball = Ball(self.assets)
        self.left_paddle = PlayerPaddle(30, HEIGHT // 2, self.assets)
        self.right_paddle = AIPaddle(WIDTH - 30, HEIGHT // 2, self.assets, self.ball)
        self.sprites.add(self.ball, self.left_paddle, self.right_paddle)

    def update(self, dt):
        super().update(dt)

        if self.ball.rect.colliderect(self.left_paddle.rect) and self.ball.velocity.x < 0:
            self.ball.bounce_off_paddle(self.left_paddle.rect)
        elif self.ball.rect.colliderect(self.right_paddle.rect) and self.ball.velocity.x > 0:
            self.ball.bounce_off_paddle(self.right_paddle.rect)

        if self.ball.rect.right < 0:
            self.right_score += 1
            self.ball.reset(direction=1)
        elif self.ball.rect.left > WIDTH:
            self.left_score += 1
            self.ball.reset(direction=-1)

        if self.left_score >= WIN_SCORE or self.right_score >= WIN_SCORE:
            self.app.states.transition_to("game_over")

    def draw(self, surface):
        super().draw(surface)
        left_text = self.font.render(str(self.left_score), True, (240, 240, 240))
        right_text = self.font.render(str(self.right_score), True, (240, 240, 240))
        surface.blit(left_text, (WIDTH // 4, 20))
        surface.blit(right_text, (WIDTH * 3 // 4, 20))
        pygame.draw.aaline(surface, (90, 90, 90), (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
