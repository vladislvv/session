# game/animation.py
import pygame
from settings import BLACK, TILE_SIZE, ROWS, COLS, PADDING, GRAY
from game.maze import maze_data

def play_animation(screen, message, color):
    font = pygame.font.SysFont("Arial", 60, bold=True)
    text = font.render(message, True, color)
    rect = text.get_rect(center=(COLS * TILE_SIZE // 2 + PADDING, ROWS * TILE_SIZE // 2 + PADDING))
    clock = pygame.time.Clock()

    for _ in range(60):
        screen.fill(BLACK)
        for y in range(ROWS):
            for x in range(COLS):
                if maze_data[y][x] == "#":
                    pygame.draw.rect(screen, GRAY,
                                     (PADDING + x * TILE_SIZE,
                                      PADDING + y * TILE_SIZE,
                                      TILE_SIZE, TILE_SIZE))
        screen.blit(text, rect)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    exit()
