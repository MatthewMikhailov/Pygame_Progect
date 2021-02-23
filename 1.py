def mini_map(self, player):
    self.sc_map.fill(BLACK)
    map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE
    pygame.draw.line(self.sc_map, YELLOW, (map_x, map_y), (map_x + 12 * math.cos(player.angle),
                                                           map_y + 12 * math.sin(player.angle)), 2)
    pygame.draw.circle(self.sc_map, RED, (int(map_x), int(map_y)), 5)
    for x, y in mini_map:
        pygame.draw.rect(self.sc_map, GREEN, (x, y, MAP_TILE, MAP_TILE))
    self.sc.blit(self.sc_map, MAP_POS)