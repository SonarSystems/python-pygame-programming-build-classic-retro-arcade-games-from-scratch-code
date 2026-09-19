import os

def validate_level_file(path, required_start_char="P"):
    rows, metadata = load_level_file(path)
    problems = []

    widths = {len(row) for row in rows}
    if len(widths) > 1:
        problems.append(f"Inconsistent row widths: {widths}")

    if required_start_char and not any(required_start_char in row for row in rows):
        problems.append(f"No '{required_start_char}' (player start) found")

    if "name" not in metadata:
        problems.append("Missing 'name' in metadata")

    return problems


def validate_all_levels(levels_dir):
    any_problems = False
    for filename in sorted(os.listdir(levels_dir)):
        if not filename.endswith(".json"):
            continue
        path = os.path.join(levels_dir, filename)
        problems = validate_level_file(path)
        if problems:
            any_problems = True
            print(f"{filename}:")
            for problem in problems:
                print(f"  - {problem}")
    if not any_problems:
        print("All levels valid.")
