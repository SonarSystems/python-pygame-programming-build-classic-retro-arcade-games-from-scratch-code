def update(self, dt):
    super().update(dt)
    # ... collision handling for player/enemy bullets against each other's targets ...

    if len(self.formation.enemies) == 0:
        self.wave_number += 1
        self.formation = Formation(self.assets)
        self.formation.speed = 40.0 + (self.wave_number - 1) * 12.0
        self.rebuild_shields()

    lowest_enemy = max((e.rect.bottom for e in self.formation.enemies), default=0)
    if lowest_enemy >= self.player.rect.top:
        self.app.states.transition_to("game_over")
