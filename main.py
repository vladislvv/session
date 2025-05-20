# main.py
import pygame
from settings import *
from game.maze import draw_maze
from game.player import Player
from game.ghost import Ghost
from game.dotmanager import DotManager
from game.animation import play_animation

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man - Modular")
clock = pygame.time.Clock()

# Игровые объекты
player = Player()
dot_manager = DotManager()
ghosts = [Ghost((34, 8)), Ghost((36, 8)), Ghost((38, 8))]

# Главный цикл игры
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.handle_input()
    player.update()
    player.check_dot_collision(dot_manager)

    if dot_manager.all_collected():
        play_animation(screen, "YOU WIN!", (255, 255, 0))

    for ghost in ghosts:
        ghost.update(player.pos)
        if ghost.check_collision(player):
            play_animation(screen, "GAME OVER", (255, 0, 0))

    draw_maze(screen)
    dot_manager.draw(screen)
    player.draw(screen)
    for ghost in ghosts:
        ghost.draw(screen)

    pygame.display.flip()

pygame.quit()
