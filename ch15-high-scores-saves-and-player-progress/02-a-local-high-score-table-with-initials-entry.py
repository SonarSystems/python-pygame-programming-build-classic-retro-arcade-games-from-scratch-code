MAX_HIGH_SCORES = 10


class HighScoreTable:
    def __init__(self, game_id):
        self.game_id = game_id
        all_data = load_data(default={})
        self.entries = all_data.get(game_id, [])

    def qualifies(self, score):
        if len(self.entries) < MAX_HIGH_SCORES:
            return True
        return score > min(e["score"] for e in self.entries)

    def add_entry(self, initials, score):
        self.entries.append({"initials": initials, "score": score})
        self.entries.sort(key=lambda e: e["score"], reverse=True)
        self.entries = self.entries[:MAX_HIGH_SCORES]
        self._save()

    def _save(self):
        all_data = load_data(default={})
        all_data[self.game_id] = self.entries
        save_data(all_data)
