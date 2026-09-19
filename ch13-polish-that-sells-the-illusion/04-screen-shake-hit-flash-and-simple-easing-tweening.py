def ease_out_quad(t):
    return 1 - (1 - t) ** 2


class TweenedValue:
    def __init__(self, initial):
        self.current = float(initial)
        self.target = float(initial)
        self.start = float(initial)
        self.duration = 0.3
        self.elapsed = 0.0

    def set_target(self, value):
        self.start = self.current
        self.target = float(value)
        self.elapsed = 0.0

    def update(self, dt):
        if self.elapsed >= self.duration:
            self.current = self.target
            return
        self.elapsed += dt
        t = min(1.0, self.elapsed / self.duration)
        self.current = self.start + (self.target - self.start) * ease_out_quad(t)
