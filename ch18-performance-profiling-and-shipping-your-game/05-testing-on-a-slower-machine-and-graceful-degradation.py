class QualitySettings:
    def __init__(self, level="high"):
        self.level = level

    @property
    def max_particles(self):
        return {"low": 80, "medium": 200, "high": 400}[self.level]

    @property
    def screen_shake_enabled(self):
        return self.level != "low"
