def draw_fps_counter(surface, clock, font):
    fps_text = font.render(f"{clock.get_fps():.0f} FPS", True, (200, 200, 200))
    surface.blit(fps_text, (10, 10))
