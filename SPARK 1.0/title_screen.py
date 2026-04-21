from __future__ import annotations
from typing import Any
import animations


def intro() -> None:
    """Display the game title screen and play the intro animation."""
    print("                          The Spoon Quest                        ")
    print("                Prepare to enter the Dungeon of Doom  !! ")
    
    input("                      press enter to continue")
    
    animations.intro_animation()

    

