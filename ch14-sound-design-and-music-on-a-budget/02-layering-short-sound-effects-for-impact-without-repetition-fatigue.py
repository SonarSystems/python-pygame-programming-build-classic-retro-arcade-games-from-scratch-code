import random


class SoundVariations:
    def __init__(self, sounds):
        self.sounds = sounds

    def play(self):
        random.choice(self.sounds).play()


hit_variations = SoundVariations([
    generate_tone(300, 0.08),
    generate_tone(320, 0.08),
    generate_tone(280, 0.09),
])
