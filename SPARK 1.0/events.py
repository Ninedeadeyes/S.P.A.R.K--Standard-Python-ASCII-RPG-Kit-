from __future__ import annotations
from typing import Any, List
import random
import msvcrt
import battle
import weapon
import armour
import enemy
import sys
import animations


nothing_list: List[str] = [
    "You look for deadly traps but find none",
    "You find nothing of interest here, maybe next time",
    "Wait..You hear something..It must be your imagination",
    "You find nothing of interest here"
]


# ---------------------------------------------------------------------------
# Progress events
# ---------------------------------------------------------------------------

def win() -> None:
    """Trigger the win animation and end the game."""
    animations.win_animation()
    print("You win!")
    print("GAME OVER")
    input("Press enter to exit")
    sys.exit()


def death(Player: Any) -> None:
    """End the game if the player's health reaches zero."""
    if Player.health <= 0:
        print("Wounds upon wounds, you fall to your death")
        print("GAME OVER")
        input("Press enter to exit")
        sys.exit()


def check_level_up(Player: Any) -> None:
    """Check if the player levels up and apply stat increases."""
    if Player.exp > 15 * Player.level:
        Player.level += 1
        Player.exp = 0
        print(f"You have gained a level. You are now level {Player.level}")
        print("What would you like to increase Power(P) or Health(H)?")

        while True:
            level_up_choice = msvcrt.getch()

            if level_up_choice in {b'p', b'P'}:
                power_increase = random.randint(2, 4)
                Player.full_power += power_increase
                Player.power = Player.full_power
                Player.health = Player.full_health
                print(f"Your power has increased by {power_increase}")
                print(f"Your power is now {Player.power}.")
                break
            
            if level_up_choice in {b'h', b'H'}:
                health_increase = random.randint(20, 30)
                Player.full_health += health_increase
                Player.health = Player.full_health
                print(f"Your health has increased by {health_increase}")
                print(f"Your health is now {Player.health}.")
                break

        Player.exp = 0


# ---------------------------------------------------------------------------
# Random events
# ---------------------------------------------------------------------------

def random_event(Player: Any) -> None:
    """Trigger a random event: nothing, battle, or loot."""
    r = random.random()
    
    if r < 0.92:
        nothing_happened()

    elif r < 0.96:
        random_battle(Player)
                    
    else:
        loot(Player)


def random_battle(Player: Any) -> None:
    """Start a random battle with one of three enemy types."""
    r = random.random()

    if r < 0.50:
        battle.fight(Player, enemy.Ratling())

    elif r < 0.75:
        battle.fight(Player, enemy.BogImp())

    else:
        battle.fight(Player, enemy.Hobgoblin())


def nothing_happened() -> None:
    """Print a random 'nothing happened' message."""
    noEvent = random.choice(nothing_list)
    print(noEvent)


def loot(Player: Any) -> None:
    """Give the player a random amount of gold."""
    gold_pickup = random.randint(1, 12)

    Player.gold += gold_pickup

    if gold_pickup == 1:
        print(f"You find a {gold_pickup} gold coin on the floor")
    else:
        print(f"You find {gold_pickup} gold coins on the floor")


# ---------------------------------------------------------------------------
# Quest events
# ---------------------------------------------------------------------------

def spoon_found(Player: Any) -> bool:
    """Handle the event where the player finds a spoon."""
    print("You find a spoon on the floor. Do you pick it up (Y or N)?")

    while True:
        decision = msvcrt.getch()

        if decision in {b'y', b'Y'}:
            print("You pick up the spoon")
            Player.got_spoon_for_quest = True
            Player.inventory.append("Spoon")
            return True
            
        if decision in {b'n', b'N'}:
            print("You decide to leave it")
            return False


def goblin_spoon_quest(Player: Any) -> None:
    """Handle the goblin's spoon quest dialogue and rewards."""
    if not Player.got_spoon_for_quest and not Player.spoon_quest:
        print("Goblin: Have you seen my spoon?")
    
    elif Player.got_spoon_for_quest and not Player.spoon_quest:
        print("Goblin: You have found my spoon, thank you!!")
        print("Goblin: For your troubles, here is a Sword and a Leather Tunic")
        Player.inventory.remove("Spoon")
        Player.inventory.append(weapon.Sword())
        Player.inventory.append(armour.LeatherTunic())
        Player.spoon_quest = True

    else:
        print("Goblin: Spoon, spoon I love my spoon la la la laaaaaa")
        print("Goblin: Are you still here?")
        print("Goblin: You've beaten the game, go home and be a family person")
        input("Goblin: Here is a little victory dance to send you off (Press Enter)")
        win()
