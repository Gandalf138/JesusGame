from pathlib import Path
import sys

def resource_path(relative_path: str) -> str:
    """Path helper for pyinstaller --onefile strangeness"""
    try:
        base_path = Path(sys._MEIPASS) # pyinstaller stores path in _MEIPASS
    except AttributeError:
        base_path = Path().absolute()

    return str(base_path / relative_path) # back to a string for pygame compatibility
