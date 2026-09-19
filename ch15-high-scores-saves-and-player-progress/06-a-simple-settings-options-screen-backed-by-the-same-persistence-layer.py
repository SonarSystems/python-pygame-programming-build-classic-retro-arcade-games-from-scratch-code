def save_settings(audio_settings, wrap_walls_enabled):
    all_data = load_data(default={})
    all_data["settings"] = {
        "music_volume": audio_settings.music_volume,
        "effects_volume": audio_settings.effects_volume,
        "wrap_walls": wrap_walls_enabled,
    }
    save_data(all_data)


def load_settings():
    all_data = load_data(default={})
    return all_data.get("settings", {
        "music_volume": 0.5,
        "effects_volume": 0.8,
        "wrap_walls": False,
    })
