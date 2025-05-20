# game/player.py
import pygame
from settings import TILE_SIZE, PADDING, COLS
from game.maze import is_wall
from game.utils import get_center, get_grid_from_pos, is_at_center

class Player:
    def __init__(self):
        self.grid = [0, 7]  # старт в левом портале
        self.pos = list(get_center(*self.grid))
        self.dir = (0, 0)
        self.next_dir = (0, 0)
        self.speed = 2
        self.frame_index = 0
        self.frame_timer = 0
        self.frames = self.load_frames()

    def load_frames(self):
        directions = ["right", "up", "left", "down"]
        all_frames = []
        for i in range(4):
            row = [
                pygame.transform.scale(
                    pygame.image.load(f"assets/pacman_frames/pacman_{i}_0.png").convert_alpha(),
                    (TILE_SIZE, TILE_SIZE)),
                pygame.transform.scale(
                    pygame.image.load(f"assets/pacman_frames/pacman_{i}_1.png").convert_alpha(),
                    (TILE_SIZE, TILE_SIZE))
            ]
            all_frames.append(row)
        return all_frames

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.next_dir = (-1, 0)
        elif keys[pygame.K_RIGHT]:
            self.next_dir = (1, 0)
        elif keys[pygame.K_UP]:
            self.next_dir = (0, -1)
        elif keys[pygame.K_DOWN]:
            self.next_dir = (0, 1)

    def update(self):
        if is_at_center(self.pos):
            gx, gy = self.grid

            # Телепортация только в строке 7
            if gy == 7 and gx == 0 and self.dir == (-1, 0):
                self.grid[0] = COLS - 1
                self.pos[0] = PADDING + self.grid[0] * TILE_SIZE + TILE_SIZE // 2
                return
            elif gy == 7 and gx == COLS - 1 and self.dir == (1, 0):
                self.grid[0] = 0
                self.pos[0] = PADDING + self.grid[0] * TILE_SIZE + TILE_SIZE // 2
                return

            nx, ny = gx + self.next_dir[0], gy + self.next_dir[1]
            if not is_wall(nx, ny):
                self.dir = self.next_dir
            nx, ny = gx + self.dir[0], gy + self.dir[1]
            if not is_wall(nx, ny):
                self.grid[0] = nx
                self.grid[1] = ny
            else:
                self.dir = (0, 0)

        self.pos[0] += self.dir[0] * self.speed
        self.pos[1] += self.dir[1] * self.speed

        # Анимация
        self.frame_timer += 1
        if self.frame_timer >= 5:
            self.frame_index = (self.frame_index + 1) % 2
            self.frame_timer = 0

    def check_dot_collision(self, dot_manager, score):
        rect = pygame.Rect(self.pos[0] - 10, self.pos[1] - 10, 20, 20)
        before = len(dot_manager.dots)
        dot_manager.remove_collided(rect)
        after = len(dot_manager.dots)
        score.add((before - after) * 10)

    def draw(self, screen):
        direction_map = {
            (1, 0): 0,   # right
            (0, -1): 1,  # up
            (-1, 0): 2,  # left
            (0, 1): 3    # down
        }
        dir_index = direction_map.get(self.dir, 0)
        image = self.frames[dir_index][self.frame_index]
        screen.blit(image, (int(self.pos[0]) - TILE_SIZE // 2, int(self.pos[1]) - TILE_SIZE // 2))
