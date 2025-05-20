# game/dot_manager.py
import pygame
from game.maze import maze_data
from settings import TILE_SIZE, PADDING

class DotManager:
    def __init__(self):
        self.dots = []
        dot_img = pygame.transform.scale(pygame.image.load("assets/dot.png").convert_alpha(), (6, 6))
        self.dot_img = dot_img
        for y, row in enumerate(maze_data):
            for x, char in enumerate(row):
                if char == ".":
                    rect = pygame.Rect(PADDING + x * TILE_SIZE + 7, PADDING + y * TILE_SIZE + 7, 6, 6)
                    self.dots.append(rect)

    def remove_collided(self, player_rect):
        self.dots = [dot for dot in self.dots if not player_rect.colliderect(dot)]

    def all_collected(self):
        return len(self.dots) == 0

    def draw(self, screen):
        for dot in self.dots:
            screen.blit(self.dot_img, (dot.x, dot.y))
