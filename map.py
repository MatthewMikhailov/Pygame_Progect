import pygame
from settings import *
import random

sprites_map = []
name_map = maps[1]
text_map = []

with open(name_map, "r") as f:
    map = f.readlines()
for i in map:
    text_map.append(i[:-1])


WORLD_WIDTH = len(text_map[0]) * TILE
WORLD_HEIGHT = len(text_map) * TILE
world_map = {}
mini_map = set()
sprites_mini_map = set()
collision_walls = []
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == "K":
            sprites_map.append(('K', i + 0.5, j + 0.5))
            sprites_mini_map.add(('K', i * MAP_TILE, j * MAP_TILE))
        elif char == "B":
            sprites_map.append(('B', i + random.uniform(0, 0.8), j + random.uniform(0, 0.8)))
            sprites_mini_map.add(('B', i * MAP_TILE, j * MAP_TILE))
        elif char != "_":
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            collision_walls.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
            if char == "1":
                world_map[(i * TILE, j * TILE)] = 1
            elif char == "2":
                world_map[(i * TILE, j * TILE)] = 2
            elif char == "3":
                world_map[(i * TILE, j * TILE)] = 3
            elif char == "4":
                world_map[(i * TILE, j * TILE)] = 4
            elif char == "5":
                world_map[(i * TILE, j * TILE)] = 5
            elif char == "6":
                world_map[(i * TILE, j * TILE)] = 6


