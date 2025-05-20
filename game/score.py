# game/score.py
import pygame
from settings import WHITE

class Score:
    def __init__(self):
        self.value = 0
        self.font = pygame.font.SysFont("Arial", 24, bold=True)

    def add(self, amount):
        self.value += amount

    def reset(self):
        self.value = 0

    def draw(self, screen):
        text = self.font.render(f"Score: {self.value}", True, WHITE)
        screen.blit(text, (10, 5))