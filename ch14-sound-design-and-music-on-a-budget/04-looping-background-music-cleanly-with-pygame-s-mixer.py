import pygame
import time

def crossfade_to(new_track_path, fade_ms=800):
    pygame.mixer.music.fadeout(fade_ms)
    pygame.time.set_timer(pygame.USEREVENT + 1, fade_ms, loops=1)
    # on receiving that USEREVENT, load and play(loops=-1) the new track
