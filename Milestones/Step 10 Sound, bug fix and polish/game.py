import title
import events 
import maps
import player
import instructions
import sound 

def main():
    maps.set_terminal_size(135, 49)  # Width and Height 
    hero=player.Player(1,0,100,12,0,9,4)  #This is the player (level,exp,health,power,gold,x,y):
    game_loop=True   # initate game loop 
    sound.play_background_music("Music/background.wav")  #background music 
    title.intro ()   # Provide a description/setting/title screen of the game before it begin.  
    maps.clear_screen(hero)  # clears the screen and reprint map. 

    while game_loop:
        maps.recall_step(hero) # This capture previous x and y used for the solid interaction function.  
        maps.flush(hero)  #remove previous @ and replace it with a . so don't leave a trail of @ when moving 
        instructions.commands(hero)  # This is where the command instructions is contained  eg: movement 
        position = maps.data_map_choice[hero.y][hero.x]  #initate the players position in the backend 
        maps.clear_screen(hero)
  
        if position == ".":           # If backend 'logic' is x,y,z this happens... 
            events.random_event(hero) # generate a random event ( eg: an enemy might appear) 

        if position == "#":
            maps.solid_interaction(hero,"#")  # initate when you hit something solid it push you back to previous x and y  
            print("You hit a wall..")

        if position == "G":
            maps.solid_interaction(hero,"G")
            events.goblin_spoon_quest(hero)

        if position=="S":
            taken=events.spoon_found(hero)
            if taken:
                maps.data_map_choice[hero.y][hero.x] = "."       # It removes the 'S' from the backend hence event won't be triggerd again. 
                                                                #  On the frontend it is a @ due to maps.clear_screen(hero) 
            else:
                maps.solid_interaction(hero,"S")  # if you say 'no' to picking the spoon, it push you back to previous step and the S remains  
                
        if position == ">":
            maps.going_downstairs(hero)

        if position == "<":
            maps.going_upstairs(hero)

if __name__ == "__main__":
    main()