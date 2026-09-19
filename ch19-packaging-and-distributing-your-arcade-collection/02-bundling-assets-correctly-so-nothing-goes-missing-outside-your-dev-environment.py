import os
import sys


def resource_path(relative_path):
    """Get an absolute path to a bundled resource, working both when run
    normally and when packaged by PyInstaller."""
    if hasattr(sys, "_MEIPASS"):
        # PyInstaller extracts bundled files to a temporary folder at
        # runtime and stores its path in sys._MEIPASS.
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)
