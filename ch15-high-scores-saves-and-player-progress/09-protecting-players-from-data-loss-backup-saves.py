import os
import json

def save_data_with_backup(data):
    if os.path.exists(SAVE_PATH):
        backup_path = SAVE_PATH + ".bak"
        try:
            os.replace(SAVE_PATH, backup_path)
        except OSError:
            pass  # backup is best-effort, never block the actual save
    save_data(data)


def load_data_with_fallback(default):
    try:
        return load_data(default=None) or default
    except Exception:
        backup_path = SAVE_PATH + ".bak"
        if os.path.exists(backup_path):
            try:
                with open(backup_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except (json.JSONDecodeError, OSError):
                pass
        return default
