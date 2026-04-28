from __future__ import annotations
import platform


def play_background_music(file_path: str) -> None:
    """Play looping background music on Windows using winsound.
    
    On non‑Windows systems, this function does nothing.
    """
    if platform.system() == "Windows":  # Only play music on Windows
        try:
            import winsound  # Imported here to avoid crashing Mac/Linux
            winsound.PlaySound(file_path, winsound.SND_ASYNC | winsound.SND_LOOP)
        except Exception as e:
            print(f"Windows sound error: {e}")
    else:
        # Not on Windows? Do nothing.
        pass
