MAX_PARTICLES = 400

def burst(self, pos, color, count=12, **kwargs):
    if len(self.particles) + count > MAX_PARTICLES:
        # Drop the oldest particles first, freeing room for the new burst.
        overflow = len(self.particles) + count - MAX_PARTICLES
        self.particles = self.particles[overflow:]
    # ... existing burst logic ...
