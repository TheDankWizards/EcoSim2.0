from sprite import Sprite
import pygame
import vision
import os
from properties import *


class WolfSprite(Sprite):
    sprite_image = pygame.image.load(os.path.join(sprites_dir, "wolf.png"))

    def __init__(self, world_map, GRID_LOCK, coordinates=None):
        Sprite.__init__(self, world_map, self.sprite_image, GRID_LOCK, coordinates)
        self.type = "wolf"
        self.movable_terrain = world_map.get_all_land_tile_types()
        self.prey = ["deer"]

    def move(self, target=None):
        visible_tiles = vision.vision(4, self.world_map, self.tile)
        target_tile = vision.find_target(visible_tiles, self.prey)
        if target_tile:
            move_to_tile = vision.approach(self.tile, target_tile, self.world_map)
            if Sprite.is_movable_terrain(self, move_to_tile) and Sprite.not_contains_sprite(self, move_to_tile, self.prey):
                if move_to_tile == target_tile:
                    move_to_tile.contains_sprite.die()
                Sprite.move(self, move_to_tile)
            else:
                Sprite.move(self)
        else:
            Sprite.move(self)
