class AnticipatedAction:
    def __init__(self, wind_up_duration=0.08):
        self.wind_up_duration = wind_up_duration
        self.timer = 0.0
        self.winding_up = False

    def start(self):
        self.winding_up = True
        self.timer = self.wind_up_duration

    def update(self, dt):
        if self.winding_up:
            self.timer -= dt
            if self.timer <= 0:
                self.winding_up = False
                return True  # fire the actual action now
        return False

    @property
    def wind_up_offset(self):
        if not self.winding_up:
            return 0.0
        # A small negative offset that grows as the wind-up completes,
        # then snaps forward the instant the real action fires.
        progress = 1.0 - (self.timer / self.wind_up_duration)
        return -6.0 * (1.0 - progress)
