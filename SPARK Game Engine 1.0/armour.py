from __future__ import annotations
from typing import Any


class Armour:
    """Base armour class storing name and protection value."""

    def __init__(self, name: str, protection: int) -> None:
        self.name: str = name
        self.protection: int = protection

    def __str__(self) -> str:
        return self.name     # Needed so print() shows the armour name instead of memory address


class Rags(Armour):
    """Basic starter armour with minimal protection."""
    def __init__(self, name: str = "Rags", protection: int = 1) -> None:
        super().__init__(name, protection)


class LeatherTunic(Armour):
    """Light armour offering slightly better protection."""
    def __init__(self, name: str = "Leather Tunic", protection: int = 2) -> None:
        super().__init__(name, protection)
