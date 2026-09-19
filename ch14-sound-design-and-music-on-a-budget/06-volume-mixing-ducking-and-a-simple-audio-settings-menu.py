import pygame
import time

def duck_music(audio_settings, duration=0.6):
    original = audio_settings.music_volume
    pygame.mixer.music.set_volume(original * 0.3)
    pygame.time.set_timer(pygame.USEREVENT + 2, int(duration * 1000), loops=1)
    # on receiving that USEREVENT, restore pygame.mixer.music.set_volume(original)
