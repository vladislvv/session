# game/ghost.py
import pygame
import math
import random
from settings import TILE_SIZE, PADDING, COLS
from game.maze import is_wall
from game.utils import get_center, get_grid_from_pos, is_at_center

class Ghost:
    def __init__(self, grid_pos):
        self.grid = list(grid_pos)
        self.pos = list(get_center(*grid_pos))
        self.dir = (0, 1)
        self.speed = 1.5
        self.image = pygame.transform.scale(pygame.image.load("assets/ghost.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))

    def update(self, target_pos):
        if not is_at_center(self.pos):
            self.pos[0] += self.dir[0] * self.speed
            self.pos[1] += self.dir[1] * self.speed
            return

        gx, gy = get_grid_from_pos(self.pos)

        # Телепортация призраков по горизонтали
        if gx < 0:
            gx = COLS - 1
            self.grid[0] = gx
            self.pos[0] = PADDING + gx * TILE_SIZE + TILE_SIZE // 2
            return
        elif gx >= COLS:
            gx = 0
            self.grid[0] = gx
            self.pos[0] = PADDING + gx * TILE_SIZE + TILE_SIZE // 2
            return

        tx, ty = get_grid_from_pos(target_pos)
        dx = tx - gx
        dy = ty - gy
        dist = abs(dx) + abs(dy)

        opposite = (-self.dir[0], -self.dir[1])
        directions = []
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if d != opposite:
                nx, ny = gx + d[0], gy + d[1]
                if not is_wall(nx, ny):
                    directions.append(d)

        if dist <= 8 and directions:
            best = min(directions, key=lambda d: abs(tx - (gx + d[0])) + abs(ty - (gy + d[1])))
            self.dir = best
        elif self.dir in directions and random.random() < 0.7:
            pass
        elif directions:
            self.dir = random.choice(directions)

        self.pos[0] += self.dir[0] * self.speed
        self.pos[1] += self.dir[1] * self.speed

    def check_collision(self, player):
        return math.hypot(self.pos[0] - player.pos[0], self.pos[1] - player.pos[1]) < 18

    def draw(self, screen):
        screen.blit(self.image, (int(self.pos[0]) - TILE_SIZE // 2, int(self.pos[1]) - TILE_SIZE // 2))
