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
        self.frames = [
            pygame.transform.scale(pygame.image.load("assets/pacman_frames/pacman_0_0.png").convert_alpha(), (TILE_SIZE, TILE_SIZE)),
            pygame.transform.scale(pygame.image.load("assets/pacman_frames/pacman_0_1.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
        ]

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

            # Телепортация
            if gx < 0:
                self.grid[0] = COLS - 1
                self.pos[0] = PADDING + self.grid[0] * TILE_SIZE + TILE_SIZE // 2
                return
            elif gx >= COLS:
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
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.frame_timer = 0

    def check_dot_collision(self, dot_manager):
        rect = pygame.Rect(self.pos[0] - 10, self.pos[1] - 10, 20, 20)
        dot_manager.remove_collided(rect)

    def draw(self, screen):
        image = self.frames[self.frame_index]
        screen.blit(image, (int(self.pos[0]) - TILE_SIZE // 2, int(self.pos[1]) - TILE_SIZE // 2))
