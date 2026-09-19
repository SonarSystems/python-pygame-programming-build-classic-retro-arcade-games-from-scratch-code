def on_wave_cleared(self):
    if self.lives_lost_this_wave == 0:
        self.score += 500
        self.show_bonus_message("Flawless Wave! +500")
    self.lives_lost_this_wave = 0
    self.wave_number += 1
    # ... existing wave-rebuild logic ...
