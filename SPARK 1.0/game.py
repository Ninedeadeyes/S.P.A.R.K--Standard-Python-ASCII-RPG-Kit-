from __future__ import annotations
from typing import Any
import title_screen
import events
import maps
import player
import instructions
import sound

def main() -> None:
    """Main game loop: initializes the player, map, and handles all movement + events."""
    
    # This is the player (level, exp, health, power, gold, x, y):
    hero = player.Player(1, 0, 100, 12, 0, 9, 4)

    game_loop = True   # initiate game loop

    sound.play_background_music("Music/background.wav")  # background music 
    title_screen.intro()  # Provide a description/setting/title screen of the game before it begins  

    # Clears the screen, prints the map, initializes backend + frontend, returns tile under player
    position = maps.clear_screen(hero)

    while game_loop:

        maps.recall_step(hero)  # Capture previous x,y for solid interaction  
        maps.flush(hero)        # Remove previous @ so the player doesn't leave a trail  
        instructions.commands(hero)  # Movement + inventory commands  
        position = maps.clear_screen(hero)  # Return backend tile at new position
  
        # -------------------------
        # TILE LOGIC
        # -------------------------

        if position == ".":           
            events.random_event(hero)  # Random encounter  

        if position == "#":
            maps.solid_interaction(hero, "#")
            print("You hit a wall..")

        if position == "G":
            maps.solid_interaction(hero, "G")
            events.goblin_spoon_quest(hero)

        if position == "S":
            taken = events.spoon_found(hero)

            if taken:
                # Remove the S from backend so event cannot trigger again
                maps.data_map_choice[hero.y][hero.x] = "."       
            else:
                # If player refuses spoon, push them back
                maps.solid_interaction(hero, "S")
                
        if position == ">":
            maps.going_downstairs(hero)

        if position == "<":
            maps.going_upstairs(hero)

if __name__ == "__main__":
    main()
