CURRENT_SAVE_VERSION = 2


def migrate_save(data):
    version = data.get("version", 1)

    if version < 2:
        # Version 2 introduced a "collected_items" list; older saves
        # simply don't have one yet, so default it in rather than crash.
        data.setdefault("collected_items", [])
        data["version"] = 2

    return data


def load_data_migrated(default):
    data = load_data(default)
    return migrate_save(data)
