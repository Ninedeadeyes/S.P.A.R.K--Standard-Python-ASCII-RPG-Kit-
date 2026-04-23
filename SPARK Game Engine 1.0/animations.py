from __future__ import annotations
from typing import Any
import os
import time


def clear() -> None:
    """Clear the terminal screen using the appropriate OS command."""
    os.system('cls' if os.name == 'nt' else 'clear')


def intro_animation() -> None:
    """Play the intro loading animation."""
    clear()
    loop = 0

    while loop < 3:
        loop += 1

        print("""      
                                                                 
                              xx  x                               xx
                              xx   x                              xx  
                              xxxxxxxx                            xx
                              xx   x                              xx
                              xx  x                          xxxxxxxxx
                              xx                             xxxxxxxxx
                             x   x                           xxxxxxxxx 
                           x      x                          xxxxxxxxx
                      ddddddddddddddddddddddddddddddddddddddddddddddddddddddd                                   
                      loading . 
                   """)
        time.sleep(.3)
        clear()

        print("""   
              
                              xx  x                               xx
                              xx   x          x                   xx
                              xxxxxxxx   xxxxxxx                  xx
                              xx   x          x                   xx 
                              xx  x                          xxxxxxxxx
                              xx                             xxxxxxxxx
                             x   x                           xxxxxxxxx 
                           x      x                          xxxxxxxxx
                      ddddddddddddddddddddddddddddddddddddddddddddddddddddddd                                   
                      loading ..
                   """)
        time.sleep(.3)
        clear()

        print("""      
              
                              xx  x                               xx
                              xx   x              x               xx
                              xxxxxxxx       xxxxxxx              xx
                              xx   x              x               xx 
                              xx  x                          xxxxxxxxx
                              xx                             xxxxxxxxx
                             x   x                           xxxxxxxxx 
                           x      x                          xxxxxxxxx
                      ddddddddddddddddddddddddddddddddddddddddddddddddddddddd                                  
                      loading ... 
                   """)
        time.sleep(.3)
        clear()

        print("""     
              
                              xx  x                               xx
                              xx   x                  x           xx
                              xxxxxxxx           xxxxxxx          xx
                              xx   x                  x           xx
                              xx  x                          xxxxxxxxx
                              xx                             xxxxxxxxx
                             x   x                           xxxxxxxxx 
                           x      x                          xxxxxxxxx
                      ddddddddddddddddddddddddddddddddddddddddddddddddddddddd                                   
                      loading . 
                   """)
        time.sleep(.3)
        clear()

        print("""     
              
                              xx  x                               xx
                              xx   x                              xx
                              xxxxxxxx                     xxxxxxxxx
                              xx   x                              xx
                              xx  x                          xxxxxxxxx
                              xx                             xxxxxxxxx
                             x   x                           xxxxxxxxx 
                           x      x                          xxxxxxxxx
                      ddddddddddddddddddddddddddddddddddddddddddddddddddddddd                                    
                      loading ..
                   """)
        time.sleep(.3)
        clear()

        print("""          
              
                          x   xx   x                              xx
                          x   xx   x                              xx
                          xxxxxxxxxx                       xxxxxxxxx
                              xx                                  xx
                              xx                             xxxxxxxxx
                              xx                             xxxxxxxxx
                             x   x                           xxxxxxxxx 
                           x      x                          xxxxxxxxx
                      ddddddddddddddddddddddddddddddddddddddddddddddddddddddd                                                               
                      loading ...
                   """)
        time.sleep(.3)
        clear()


def win_animation() -> None:
    """Play the win animation shown at the end of the game."""
    clear()
    loop = 0

    while loop < 4:
        loop += 1

        print("""
              xxxxxx You Win !! (Game Over) xxxxxx   
              
                          x   xx   x                            
                          x   xx   x                            
                          xxxxxxxxxx                       
                              xx                                  
                              xx                           
                              xx                             
                             x   x                          
                           x      x                         
                      ddddddddddddddddddd                                                              
                     
                   """)
        time.sleep(.3)
        clear()

        print("""
              xxxxxx You Win !! (Game Over) xxxxxx         
              
                          x   xx                               
                          x   xx                               
                          xxxxxxxxxx                       
                              xx   x                               
                              xx   x                        
                            x xx x                             
                           x      x                          
                           x      x                         
                      ddddddddddddddddddd                                                              
                     
                   """)
        time.sleep(.3)
        clear()

        print("""
              xxxxxx You Win !! (Game Over) xxxxxx      
              
                              xx   x                            
                              xx   x                            
                          xxxxxxxxxx                       
                          x   xx                                  
                          x   xx                           
                              xx                             
                           x     x                          
                           x      x                         
                      ddddddddddddddddddd                                                              
                     
                   """)
        time.sleep(.3)
        clear()

        print("""
              xxxxxx You Win !! (Game Over) xxxxxx   
              
                              xx                               
                              xx                               
                          xxxxxxxxxx                       
                          x   xx   x                                
                          x   xx   x                        
                            x xx x                             
                          x       x                          
                        x         x                         
                      ddddddddddddddddddd                                                              
                     
                   """)
        time.sleep(.3)
        clear()
