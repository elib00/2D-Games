import sys
# import pygame
from game import *
        
if __name__ == "__main__":  
    game = Game()
    game.show_intro_screen()
    game.new_game()
    
    while game.running:
        game.main()
        game.game_over()
        
    pygame.quit()
    sys.exit()
