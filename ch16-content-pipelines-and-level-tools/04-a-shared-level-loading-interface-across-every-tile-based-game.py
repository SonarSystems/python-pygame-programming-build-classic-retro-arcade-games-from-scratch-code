def load_level_file(path):
    """Returns (rows, metadata) — the same shape every game's own
    build_level()-style function already expects as its `rows` input,
    now sourced from a file the editor produced instead of a hardcoded
    list literal."""
    with open(path, "r", encoding="utf-8") as f:
        payload = json.load(f)
    return payload["rows"], payload.get("metadata", {})
