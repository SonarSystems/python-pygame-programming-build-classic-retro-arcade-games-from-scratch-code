def save_platformer_progress(level_index, checkpoint_position, collected_items):
    all_data = load_data(default={})
    all_data["platformer_progress"] = {
        "level_index": level_index,
        "checkpoint_position": list(checkpoint_position),
        "collected_items": list(collected_items),
    }
    save_data(all_data)


def load_platformer_progress():
    all_data = load_data(default={})
    return all_data.get("platformer_progress")
