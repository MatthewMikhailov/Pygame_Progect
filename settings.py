import math

# game settings
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
PENTA_HEIGHT = 5 * HEIGHT
DOUBLE_HEIGHT = 2 * HEIGHT
FPS = 60
TILE = 100
FPS_POS = (WIDTH - 65, 5)
DOUBLE_PI = 2 * math.pi

# minimap settings
MINIMAP_SCALE = 5
MINIMAP_RES = (WIDTH // MINIMAP_SCALE, HEIGHT // MINIMAP_SCALE)
MAP_SCALE = 2 * MINIMAP_SCALE
MAP_TILE = TILE // MAP_SCALE
MAP_POS = (0, HEIGHT - HEIGHT // MINIMAP_SCALE)

# ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 600
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 1.5 * DIST * TILE
SCALE = WIDTH // NUM_RAYS

# player settings
player_pos = (540, 140)
player_angle = 0
player_speed = 2
sensitivity = 0.002
speed_controller = 1

# sprite settings
CENTER_RAY = NUM_RAYS // 2 - 1
FAKE_RAYS = 100
FAKE_RAYS_RANGE = NUM_RAYS - 1 + 2 * FAKE_RAYS

# texture settings (1200 x 1200)
TEXTURE_WIDTH = 1200
TEXTURE_HEIGHT = 1200
TEXTURE_SCALE = TEXTURE_WIDTH // TILE

# map settings
maps = [
    "maps/map1.txt",
    "maps/map2.txt",
    "maps/map3.txt",
    "maps/map4.txt",
]

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 80, 0)
BLUE = (0, 0, 255)
DARKGRAY = (40, 40, 40)
PURPLE = (120, 0, 120)
SKYBLUE = (0, 186, 255)
YELLOW = (220, 220, 0)