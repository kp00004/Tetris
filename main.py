import pygame, sys
from game import Game
from colors import Colors
from screens import draw_start_screen, draw_game_over_screen

pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()
game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over:
                game.reset()
                game.game_over = False
            else:
                if event.key == pygame.K_LEFT:
                    game.move_left()
                if event.key == pygame.K_RIGHT:
                    game.move_right()
                if event.key == pygame.K_DOWN:
                    game.move_down()
                    game.update_score(0, 1)
                if event.key == pygame.K_UP:
                    game.rotate()
        if event.type == GAME_UPDATE and not game.game_over:
            game.move_down()

    if game.game_over:
        if game.score == 0:
            draw_start_screen(screen, title_font)
        else:
            draw_game_over_screen(screen, title_font)
    else:
        score_value_surface = title_font.render(str(game.score), True, Colors.white)
        screen.fill(Colors.dark_blue)
        screen.blit(score_surface, (365, 20, 50, 50))
        screen.blit(next_surface, (375, 180, 50, 50))
        pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
        screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))
        pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
        game.draw(screen)
        pygame.display.update()

    clock.tick(60)
