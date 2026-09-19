def update(self, dt):
    super().update(dt)
    # ... collision handling above ...
    if len(self.bricks) == 0:
        self.level_index += 1
        if self.level_index < len(LEVELS):
            self.load_level(LEVELS[self.level_index])
        else:
            self.app.states.transition_to("victory")
