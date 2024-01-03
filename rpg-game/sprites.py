import pygame
from config import *
import math
import random

class SpriteSheet():
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()
    
    def get_sprite_image(self, x, y, width, height) -> pygame.Surface:
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite
    
    
class Player(pygame.sprite.Sprite):
    def __init__(self, game: "Game", x: int, y: int):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        self.x_coordinate = x * TILE_SIZE
        self.y_coordinate = y * TILE_SIZE
        self.delta_x = 0
        self.delta_y = 0
        
        self.face_direction = "DOWN"

        self.image = self.game.character_spritesheet.get_sprite_image(1, 0, self.width, self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x_coordinate
        self.rect.y = self.y_coordinate
        
        
    def move(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.delta_x += PLAYER_SPEED
            self.face_direction = "RIGHT"
            self.image = self.game.character_spritesheet.get_sprite_image(2, 66, self.width, self.height)
        elif keys[pygame.K_a]:
            self.delta_x -= PLAYER_SPEED
            self.face_direction = "LEFT"
            self.image = self.game.character_spritesheet.get_sprite_image(2, 98, self.width, self.height)
        elif keys[pygame.K_w]:
            self.delta_y -= PLAYER_SPEED
            self.face_direction = "UP"
            self.image = self.game.character_spritesheet.get_sprite_image(3, 35, self.width, self.height)
        elif keys[pygame.K_s]:
            self.delta_y += PLAYER_SPEED
            self.face_direction = "DOWN"
            self.image = self.game.character_spritesheet.get_sprite_image(1, 0, self.width, self.height)
        
    
    def handle_collision(self, direction):
        if direction == "x_direction":
            collides = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if collides:
                print("igo sa x")
                if self.delta_x > 0:
                    self.rect.x = collides[0].rect.left - self.rect.width
                elif self.delta_x < 0:
                    self.rect.x = collides[0].rect.right
        
        if direction == "y_direction":
            collides = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if collides:
                print("igo sa y")
                if self.delta_y > 0:
                    self.rect.y = collides[0].rect.top - self.rect.height
                elif self.delta_y < 0:
                    self.rect.y = collides[0].rect.bottom
            
    def update(self) -> None:
        self.move()
    
        self.rect.x += self.delta_x
        self.x_coordinate = self.rect.x
        self.handle_collision("x_direction")
    

        self.rect.y += self.delta_y
        self.y_coordinate = self.rect.y
        self.handle_collision("y_direction")
        
        self.delta_x = 0
        self.delta_y = 0
        
class Block(pygame.sprite.Sprite):
    def __init__(self, game: "Game", x: int, y: int):
        self.game = game
        self._layer = BLOCK_LAYER
        self.x_coordinate = x * TILE_SIZE
        self.y_coordinate = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups) 
        
        self.image = self.game.terrain_spritesheet.get_sprite_image(960, 448, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x_coordinate
        self.rect.y = self.y_coordinate
        
class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.x_coordinate = x * TILE_SIZE
        self.y_coordinate = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = self.game.terrain_spritesheet.get_sprite_image(64, 352, self.width, self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x_coordinate
        self.rect.y = self.y_coordinate

class Grass(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.x_coordinate = x * TILE_SIZE
        self.y_coordinate = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = self.game.terrain_spritesheet.get_sprite_image(353, 351, self.width, self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x_coordinate
        self.rect.y = self.y_coordinate