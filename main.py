# main.py
import pygame
from settings import *
from game.maze import draw_maze
from game.player import Player
from game.ghost import Ghost
from game.dotmanager import DotManager
from game.animation import play_animation
from game.score import Score
from game.menu import Menu
from game.record import load_record, save_record

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man - Modular")
clock = pygame.time.Clock()

player = Player()
dot_manager = DotManager()
score = Score()
menu = Menu()
ghosts = [Ghost((28, 7)), Ghost((29, 7)), Ghost((30, 7))]
record = load_record()
saved_record = record
game_over = False

running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_over and menu.is_restart_clicked(event):
            # рестарт
            player = Player()
            dot_manager = DotManager()
            score = Score()
            ghosts = [Ghost((28, 7)), Ghost((29, 7)), Ghost((30, 7))]
            game_over = False

    if not game_over:
        player.handle_input()
        player.update()
        player.check_dot_collision(dot_manager, score)

        if dot_manager.all_collected():
            record = max(score.value, record)
            save_record(record)
            game_over = True

        for ghost in ghosts:
            ghost.update(player.pos)
            if ghost.check_collision(player):
                record = max(score.value, record)
                save_record(record)
                game_over = True

    draw_maze(screen)
    dot_manager.draw(screen)
    player.draw(screen)
    score.draw(screen)

    for ghost in ghosts:
        ghost.draw(screen)

    if game_over:
        menu.draw_game_over(screen, score.value, record)

    pygame.display.flip()

pygame.quit()
