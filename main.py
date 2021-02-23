import pygame
from settings import *
from player import Player
from drawing import Drawing
from sprite_objects import *
from ray_casting import ray_casting_walls

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface(MINIMAP_RES)

sprites = Sprites()
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
player = Player()
drawing = Drawing(sc, sc_map)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    sc.fill(BLACK)

    drawing.background(player.angle)
    walls = ray_casting_walls(player, drawing.textures)
    drawing.world(walls + [obj.object_locate(player, walls) for obj in sprites.list_of_objects])
    drawing.fps(clock)
    drawing.mini_map(player)
    FPS = int(clock.get_fps())
    if FPS > 0:
        player.max_fps(FPS)

    pygame.display.flip()
    clock.tick()
