class GameApp:
    def __init__(self, loop):
        self.loop = loop
        self.states = StateMachine("menu")
        self.scenes = {
            "menu": MenuScene(self),
            "playing": PlayingScene(self),
            "game_over": GameOverScene(self),
        }
        self.states.on_change(self._on_state_change)
        self.loop.set_scene(self.scenes["menu"])

    def _on_state_change(self, old_state, new_state):
        self.loop.set_scene(self.scenes[new_state])
