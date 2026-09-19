STARTING_LIVES = 20
TOTAL_WAVES = 10


class PlayingScene(Scene):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.map = TowerMap()
        self.economy = Economy(STARTING_GOLD)
        self.lives = STARTING_LIVES
        self.wave_number = 0
        self.enemies = []
        self.towers = []
        self.projectiles = []
        self.wave_in_progress = False

    def start_next_wave(self):
        self.wave_number += 1
        self.pending_enemies = build_wave(self.wave_number, self.map.path, self.app.assets)
        self.wave_timer = 0.0
        self.wave_in_progress = True

    def update(self, dt):
        self.wave_timer = getattr(self, "wave_timer", 0.0) + dt
        ready = [e for e in self.pending_enemies if e.spawn_delay <= self.wave_timer]
        for enemy in ready:
            self.enemies.append(enemy)
            self.pending_enemies.remove(enemy)

        for enemy in list(self.enemies):
            enemy.update(dt)
            if enemy.reached_end():
                self.lives -= 1
                self.enemies.remove(enemy)
            elif enemy.health <= 0:
                self.economy.earn(enemy.reward)
                self.enemies.remove(enemy)

        for tower in self.towers:
            tower.update(dt, self.enemies, self.projectiles, self.app.assets)

        for projectile in list(self.projectiles):
            result = projectile.update(dt)
            if result in ("hit", "expired"):
                self.projectiles.remove(projectile)

        if self.lives <= 0:
            self.app.states.transition_to("game_over")
        elif self.wave_in_progress and not self.enemies and not self.pending_enemies:
            self.wave_in_progress = False
            if self.wave_number >= TOTAL_WAVES:
                self.app.states.transition_to("victory")
