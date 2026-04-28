from __future__ import annotations
from typing import List
import animations


def intro() -> None:
    print("                          The Spoon Quest                        ")
    print("                Prepare to enter the Dungeon of Doom  !! ")
    input("                      press enter to continue")
    animations.intro_animation()
