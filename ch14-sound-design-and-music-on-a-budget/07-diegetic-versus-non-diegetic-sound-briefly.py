def spatialized_play(sound, source_x, screen_width, base_volume=0.8):
    center = screen_width / 2
    pan = (source_x - center) / center  # -1.0 (far left) to 1.0 (far right)
    pan = max(-1.0, min(1.0, pan))
    left_volume = base_volume * (1.0 - max(0, pan))
    right_volume = base_volume * (1.0 + min(0, pan))
    channel = sound.play()
    if channel is not None:
        channel.set_volume(left_volume, right_volume)
