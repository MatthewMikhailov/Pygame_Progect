from settings import *
import pygame
import math
from map import collision_walls


class Player:
    def __init__(self):
        self.player_speed = player_speed
        self.speed_controller = speed_controller
        self.sensivity = sensitivity
        self.x, self.y = player_pos
        self.angle = player_angle
        self.side = 50
        self.rect = pygame.Rect(*player_pos, self.side, self.side)


    @property
    def pos(self):
        return (self.x, self.y)

    def detect_collision(self, dx, dy):
        next_rect = self.rect.copy()
        next_rect.move_ip(dx, dy)
        hit_indexes = next_rect.collidelistall(collision_walls)

        if len(hit_indexes):
            delta_x, delta_y = 0, 0
            for hit_index in hit_indexes:
                hit_rect = collision_walls[hit_index]
                if dx > 0:
                    delta_x += next_rect.right - hit_rect.left
                else:
                    delta_x += hit_rect.right - next_rect.left
                if dy > 0:
                    delta_y += next_rect.bottom - hit_rect.top
                else:
                    delta_y += hit_rect.bottom - next_rect.top
            if not (delta_x == delta_y and delta_x > 103 and delta_y > 103):
                if abs(delta_y - delta_x) < 10:
                    dx, dy = 0, 0
                elif delta_x > delta_y:
                    dy = 0
                elif delta_y > delta_x:
                    dx = 0
        self.x += dx
        self.y += dy

    def max_fps(self, FPS):
        diference = FPS - 60
        self.player_speed = self.speed_controller * (player_speed - diference * 2 / FPS)
        self.sensivity = sensitivity - 0.001 * (diference // 60)

    def movement(self):
        self.keys_control()
        self.mouse_control()
        self.rect.center = self.x, self.y
        self.angle %= DOUBLE_PI

    def keys_control(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        self.speed_controller = 1
        if keys[pygame.K_ESCAPE]:
            exit()

        if keys[pygame.K_LSHIFT]:
            self.speed_controller = 2
        if keys[pygame.K_LCTRL]:
            self.speed_controller = 0.5
        if keys[pygame.K_w]:
            dx = self.player_speed * cos_a
            dy = self.player_speed * sin_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_s]:
            dx = -self.player_speed * cos_a
            dy = -self.player_speed * sin_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_a]:
            dx = self.player_speed / 1.5 * sin_a
            dy = -self.player_speed / 1.5 * cos_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_d]:
            dx = -self.player_speed / 1.5 * sin_a
            dy = self.player_speed / 1.5 * cos_a
            self.detect_collision(dx, dy)

        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02

    def mouse_control(self):
        if pygame.mouse.get_focused():
            difference = pygame.mouse.get_pos()[0] - HALF_WIDTH
            pygame.mouse.set_pos((HALF_WIDTH, HALF_HEIGHT))
            self.angle += difference * self.sensivity
