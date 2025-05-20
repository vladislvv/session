# game/menu.py
import pygame
from settings import WIDTH, HEIGHT, WHITE, BLACK

class Menu:
    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 36, bold=True)
        self.small_font = pygame.font.SysFont("Arial", 24)
        self.restart_button = pygame.Rect(WIDTH // 2 - 80, HEIGHT // 2 + 40, 160, 50)

    def draw_game_over(self, screen, score, record):
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))

        title = self.font.render("GAME OVER", True, WHITE)
        screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60)))

        score_text = self.small_font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (WIDTH // 2 - 60, HEIGHT // 2 - 10))

        record_text = self.small_font.render(f"Record: {record}", True, WHITE)
        screen.blit(record_text, (WIDTH // 2 - 60, HEIGHT // 2 + 20))

        pygame.draw.rect(screen, WHITE, self.restart_button, border_radius=8)
        restart_text = self.small_font.render("Restart", True, BLACK)
        screen.blit(restart_text, restart_text.get_rect(center=self.restart_button.center))

    def is_restart_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.restart_button.collidepoint(event.pos)
