class LifetimeStats:
    def __init__(self, game_id):
        self.game_id = game_id
        all_data = load_data(default={})
        self.stats = all_data.get(f"{game_id}_stats", {
            "games_played": 0,
            "total_score": 0,
            "best_wave": 0,
            "total_playtime_seconds": 0.0,
        })

    def record_game(self, score, wave_reached, playtime_seconds):
        self.stats["games_played"] += 1
        self.stats["total_score"] += score
        self.stats["best_wave"] = max(self.stats["best_wave"], wave_reached)
        self.stats["total_playtime_seconds"] += playtime_seconds
        self._save()

    def _save(self):
        all_data = load_data(default={})
        all_data[f"{self.game_id}_stats"] = self.stats
        save_data(all_data)

    @property
    def average_score(self):
        if self.stats["games_played"] == 0:
            return 0
        return self.stats["total_score"] / self.stats["games_played"]
