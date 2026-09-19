class AnimatedSprite:
    def __init__(self, frames, frame_duration=0.08):
        self.frames = frames  # a list of Surface objects
        self.frame_duration = frame_duration
        self.current_frame = 0
        self.timer = 0.0

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.frame_duration:
            self.timer -= self.frame_duration
            self.current_frame = (self.current_frame + 1) % len(self.frames)

    @property
    def image(self):
        return self.frames[self.current_frame]
