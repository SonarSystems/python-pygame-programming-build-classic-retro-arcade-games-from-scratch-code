import random

STARTING_LIVES = 3

def handle_ball_lost(self):
    self.lives -= 1
    if self.lives <= 0:
        self.app.states.transition_to("game_over")
    else:
        self.ball.reset(direction=random.choice([-1, 1]))
        self.paddle.reset_position()
