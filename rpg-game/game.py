import pygame
from pygame.locals import *
from sprites import Player, Block, SpriteSheet, Ground, Grass
from config import *

class Game:
    def __init__(self): 
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("RPG Game")
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.character_spritesheet = SpriteSheet("images/character.png")
        self.terrain_spritesheet = SpriteSheet("images/terrain.png")
    
    def create_map(self) -> None:
        for i, row in enumerate(TILE_MAP):
            print(row)
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == 0:
                    Block(self, j, i)
                elif column == 2:
                    Player(self, j, i) 
                elif column == 3:
                    Grass(self, j, i)
                                   
    
    def new_game(self) -> None:
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        # Player(self, (WINDOW_WIDTH // 2) - (TILE_SIZE // 2), (WINDOW_HEIGHT // 2) - (TILE_SIZE // 2))
        self.create_map()
    
    def update(self) -> None:
        self.all_sprites.update()

    def events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
    
    def draw(self) -> None:
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def game_over(self) -> None:
        pass

    def show_intro_screen(self) -> None:
        pass

    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
        
        self.running = False