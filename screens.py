import pygame
from colors import Colors

def draw_start_screen(screen, font):
    screen.fill(Colors.dark_blue)
    title_surface = font.render("PYTHON TETRIS", True, Colors.white)
    start_surface = font.render("Press any key to start", True, Colors.white)

    title_rect = title_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 40))
    start_rect = start_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 40))

    screen.blit(title_surface, title_rect)
    screen.blit(start_surface, start_rect)
    pygame.display.flip()

def draw_game_over_screen(screen, font):
    screen.fill(Colors.dark_blue)
    game_over_surface = font.render("GAME OVER", True, Colors.white)
    restart_surface = font.render("Press any key to restart", True, Colors.white)

    game_over_rect = game_over_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 30))
    restart_rect = restart_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 30))

    screen.blit(game_over_surface, game_over_rect)
    screen.blit(restart_surface, restart_rect)
    pygame.display.flip()
