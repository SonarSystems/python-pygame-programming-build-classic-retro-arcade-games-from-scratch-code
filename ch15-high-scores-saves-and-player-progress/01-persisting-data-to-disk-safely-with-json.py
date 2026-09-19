import json
import os

SAVE_DIR = os.path.join(os.path.expanduser("~"), ".arcade_workshop")
SAVE_PATH = os.path.join(SAVE_DIR, "save.json")


def save_data(data):
    os.makedirs(SAVE_DIR, exist_ok=True)
    # Write to a temporary file first, then rename — this avoids leaving
    # a corrupted half-written save file if the game crashes or is force
    # closed mid-write.
    temp_path = SAVE_PATH + ".tmp"
    with open(temp_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    os.replace(temp_path, SAVE_PATH)


def load_data(default):
    if not os.path.exists(SAVE_PATH):
        return default
    try:
        with open(SAVE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        # A corrupted or unreadable save should never crash the game —
        # fall back to a fresh default instead.
        return default
