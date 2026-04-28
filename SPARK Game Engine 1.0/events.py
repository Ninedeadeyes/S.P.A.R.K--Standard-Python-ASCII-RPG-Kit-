from __future__ import annotations
from typing import List, TYPE_CHECKING
import random
import msvcrt
import battle
import weapon
import armour
import enemy
import sys
import animations

if TYPE_CHECKING:
    from player import Player

nothing_list: List[str] = [
    "You look for deadly traps but find none",
    "You find nothing of interest here, maybe next time",
    "Wait..You hear something..It must be your imagination",
    "You find nothing of interest here"
]

def win() -> None:
    """Trigger the win animation and end the game."""
    animations.win_animation()
    print("You win!")
    print("GAME OVER")
    input("Press enter to exit")
    sys.exit()

def death(player: Player) -> None:
    """End the game if the player's health reaches zero."""
    if player.health <= 0:
        print("Wounds upon wounds, you fall to your death")
        print("GAME OVER")
        input("Press enter to exit")
        sys.exit()

def check_level_up(player: Player) -> None:
    """Check if the player levels up and apply stat increases."""
    if player.exp > 15 * player.level:
        player.level += 1
        player.exp = 0
        print(f"You have gained a level. You are now level {player.level}")
        print("What would you like to increase Power(P) or Health(H)?")

        while True:
            level_up_choice = msvcrt.getch()

            if level_up_choice in {b'p', b'P'}:
                power_increase = random.randint(2, 4)
                player.full_power += power_increase
                player.power = player.full_power
                player.health = player.full_health
                print(f"Your power has increased by {power_increase}")
                print(f"Your power is now {player.power}.")
                break
            
            if level_up_choice in {b'h', b'H'}:
                health_increase = random.randint(20, 30)
                player.full_health += health_increase
                player.health = player.full_health
                print(f"Your health has increased by {health_increase}")
                print(f"Your health is now {player.health}.")
                break

        player.exp = 0

def random_event(player: Player) -> None:
    """Trigger a random event: nothing, battle, or loot."""
    r = random.random()
    
    if r < 0.92:
        nothing_happened()
    elif r < 0.96:
        random_battle(player)                    
    else:
        loot(player)

def random_battle(player: Player) -> None:
    """Start a random battle with one of three enemy types."""
    r = random.random()

    if r < 0.50:
        battle.fight(player, enemy.Ratling())
    elif r < 0.75:
        battle.fight(player, enemy.BogImp())
    else:
        battle.fight(player, enemy.Hobgoblin())

def nothing_happened() -> None:
    """Print a random 'nothing happened' message."""
    noEvent = random.choice(nothing_list)
    print(noEvent)

def loot(player: Player) -> None:
    """Give the player a random amount of gold."""
    gold_pickup = random.randint(1, 12)
    player.gold += gold_pickup

    if gold_pickup == 1:
        print(f"You find a {gold_pickup} gold coin on the floor")
    else:
        print(f"You find {gold_pickup} gold coins on the floor")

def spoon_found(player: Player) -> bool:
    """Handle the event where the player finds a spoon."""
    print("You find a spoon on the floor. Do you pick it up (Y or N)?")

    while True:
        decision = msvcrt.getch()

        if decision in {b'y', b'Y'}:
            print("You pick up the spoon")
            player.got_spoon_for_quest = True
            player.inventory.append("Spoon")
            return True
            
        if decision in {b'n', b'N'}:
            print("You decide to leave it")
            return False

def goblin_spoon_quest(player: Player) -> None:
    """Handle the goblin's spoon quest dialogue and rewards."""
    if not player.got_spoon_for_quest and not player.spoon_quest:
        print("Goblin: Have you seen my spoon?")
    
    elif player.got_spoon_for_quest and not player.spoon_quest:
        print("Goblin: You have found my spoon, thank you!!")
        print("Goblin: For your troubles, here is a Sword and a Leather Tunic")
        player.inventory.remove("Spoon")
        player.inventory.append(weapon.Sword())
        player.inventory.append(armour.LeatherTunic())
        player.spoon_quest = True

    else:
        print("Goblin: Spoon, spoon I love my spoon la la la laaaaaa")
        print("Goblin: Are you still here?")
        print("Goblin: You've beaten the game, go home and be a family person")
        input("Goblin: Here is a little victory dance to send you off (Press Enter)")
        win()