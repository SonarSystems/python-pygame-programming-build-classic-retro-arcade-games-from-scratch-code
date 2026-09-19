class AudioEvents:
    def __init__(self, asset_manager, audio_settings):
        self.assets = asset_manager
        self.settings = audio_settings
        self.event_sounds = {}

    def register(self, event_name, sound_path):
        self.event_sounds[event_name] = self.assets.sound(sound_path)

    def play(self, event_name):
        sound = self.event_sounds.get(event_name)
        if sound is not None:
            sound.set_volume(self.settings.effects_volume)
            sound.play()
