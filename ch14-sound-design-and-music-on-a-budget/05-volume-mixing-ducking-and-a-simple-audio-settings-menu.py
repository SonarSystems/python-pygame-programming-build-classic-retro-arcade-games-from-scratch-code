import pygame

class AudioSettings:
    def __init__(self):
        self.music_volume = 0.5
        self.effects_volume = 0.8

    def apply_music_volume(self):
        pygame.mixer.music.set_volume(self.music_volume)

    def play_effect(self, sound):
        sound.set_volume(self.effects_volume)
        sound.play()
