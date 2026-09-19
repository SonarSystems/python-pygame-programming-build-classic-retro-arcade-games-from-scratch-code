import pygame

from engine.game_loop import GameLoop


class FrameRateTestScene:
    """Runs the exact same delta-time movement logic at two different
    frame rate caps in two separate short runs, and prints the final
    position reached in each — if frame-rate independence is working
    correctly, both numbers should be very close to identical despite
    completing wildly different numbers of frames."""

    def __init__(self, target_fps, run_duration=2.0):
        self.target_fps = target_fps
        self.run_duration = run_duration
        self.elapsed = 0.0
        self.x = 0.0
        self.speed = 200.0  # pixels per second
        self.frame_count = 0

    def handle_event(self, event):
        pass

    def update(self, dt):
        self.x += self.speed * dt
        self.elapsed += dt
        self.frame_count += 1
        if self.elapsed >= self.run_duration:
            print(f"At {self.target_fps} FPS target: "
                  f"{self.frame_count} frames, final x = {self.x:.1f}")

    def draw(self, surface):
        surface.fill((20, 20, 30))


if __name__ == "__main__":
    for fps in (30, 144):
        loop = GameLoop(400, 300, f"FPS Test ({fps})", fps=fps)
        loop.set_scene(FrameRateTestScene(fps))
        # In a real run you'd let this play interactively; for this
        # diagnostic, imagine running each for exactly two seconds and
        # comparing the two printed final positions.
