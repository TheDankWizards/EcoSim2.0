import pygame
import os
import threading
from properties import *
from widgets import widget___tiled_map
from threading import Thread
from sprites.sprite import Sprite
from sprites.sprite___deer import DeerSprite
from sprites.sprite___wolf import WolfSprite
from sprites.sprite____eagle import EagleSprite
from sprites.sprite___lynx import LynxSprite
from sprites.sprite___hare import HareSprite
from sprites.sprite___ticks import TickSprite
from sprites.poc___plant import PlantSprite
from sprites.poc___bees import BeesSprite
from sprites.poc___fish import FishSprite
from sprites.poc___bear import BearSprite
from groups.group___all_sprites import AllSpritesGroup
from groups.group____fish import FishGroup
from groups.group____wolf import WolfGroup
from groups.group___bear import BearGroup
from groups.group___bees import BeesGroup
from groups.group___deer import DeerGroup
from groups.group___plant import PlantGroup


def sprite_test():
    pygame.init()

    world_map = widget___tiled_map.WorldMap("map1.tmx", (0, 0))

    world_map.render_entire_map()

    GRID_LOCK = threading.Lock()

    fish_group = FishGroup()
    bear_group = BearGroup()
    bees_group = BeesGroup()
    wolf_group = WolfGroup()
    deer_group = DeerGroup()
    plant_group = PlantGroup()

    s1 = EagleSprite(world_map, GRID_LOCK, (500, 500))
    s2 = EagleSprite(world_map, GRID_LOCK, (550, 550))
    s3 = FishSprite(world_map, GRID_LOCK, (450, 450))
    s4 = WolfSprite(world_map, GRID_LOCK, (55, 35))
    #s5 = WolfSprite(world_map, GRID_LOCK, (0, 35))
    #s6 = BearSprite(world_map, GRID_LOCK)

    s7 = DeerSprite(world_map, GRID_LOCK)
    s8 = DeerSprite(world_map, GRID_LOCK)
    s9 = DeerSprite(world_map, GRID_LOCK)
    s10 = DeerSprite(world_map, GRID_LOCK)
    s11 = BearSprite(world_map, GRID_LOCK)
    s12 = BearSprite(world_map, GRID_LOCK)

    s13 = HareSprite(world_map, GRID_LOCK)
    s14 = HareSprite(world_map, GRID_LOCK)
    s15 = HareSprite(world_map, GRID_LOCK)

    #s16 = LynxSprite(world_map, GRID_LOCK)
    #s17 = LynxSprite(world_map, GRID_LOCK)
    #s18 = LynxSprite(world_map, GRID_LOCK)

    s19 = TickSprite(world_map, GRID_LOCK)
    s20 = TickSprite(world_map, GRID_LOCK)
    # s1.update()
    # s2.update()
    # s3.update()
    # s4.update()
    # s5.update()
    # s6.update()
    sprites = AllSpritesGroup([fish_group, bear_group, bees_group, wolf_group, deer_group, plant_group], s1, s2, s3, s4,s7, s9, s10, s11, s13, s14, s15, s19, s20)
    # sprites.add_to_correct_group(s4)
    # sprites.add_to_correct_group(s5)
    # sprites.add_to_correct_group(s6)
    # sprites.add_to_correct_group(s7)
    # sprites.add_to_correct_group(s8)
    # sprites.add_to_correct_group(s9)
    # sprites.add_to_correct_group(s10)
    # sprites.add_to_correct_group(s11)
    # sprites.add_to_correct_group(s12)
    # deer_group.update()
    #
    # fish_group.update()
    # bear_group.update()
    # bees_group.update()
    # wolf_group.update()
    # plant_group.update()
    # wolf_group.determine_pack_leader()
    sprites.update()
    #

    done = False
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True

sprite_test()
