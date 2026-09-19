class TickTimer:
    def __init__(self, interval_seconds):
        self.interval = interval_seconds
        self.accumulated = 0.0

    def update(self, dt):
        self.accumulated += dt
        if self.accumulated >= self.interval:
            self.accumulated -= self.interval
            return True
        return False
