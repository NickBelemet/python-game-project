import pygame
import sys

from game import Game
from colour import Colours


# Initialize Pygame
pygame.init()


def load_font(path, size):
    """Load a font and use Pygame's default font if loading fails."""
    try:
        return pygame.font.Font(path, size)
    except (FileNotFoundError, pygame.error) as error:
        print(f"Could not load arcade font: {error}")
        print("Using the default Pygame font instead.")
        return pygame.font.Font(None, size)


# Fonts
title_font = load_font("assets/ARCADECLASSIC.TTF", 36)
large_font = load_font("assets/ARCADECLASSIC.TTF", 64)
small_font = load_font("assets/ARCADECLASSIC.TTF", 24)


# Main game text
score_surface = title_font.render(
    "SCORE",
    True,
    Colours.white
)

next_surface = title_font.render(
    "NEXT",
    True,
    Colours.white
)

game_over_surface = title_font.render(
    "GAME OVER",
    True,
    Colours.white
)

restart_surface = small_font.render(
    "PRESS R TO RESTART",
    True,
    Colours.white
)

menu_surface = small_font.render(
    "PRESS SPACE FOR MENU",
    True,
    Colours.white
)


# Start-screen text
start_title_surface = large_font.render(
    "TETRIS",
    True,
    Colours.white
)

start_prompt_surface = small_font.render(
    "PRESS SPACE TO START",
    True,
    Colours.white
)

move_surface = small_font.render(
    "LEFT AND RIGHT TO MOVE",
    True,
    Colours.white
)

drop_surface = small_font.render(
    "DOWN TO DROP",
    True,
    Colours.white
)

rotate_surface = small_font.render(
    "UP TO ROTATE",
    True,
    Colours.white
)


# Interface panels
score_rect = pygame.Rect(320, 55, 170, 50)
next_rect = pygame.Rect(320, 215, 170, 180)


# Window
screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()
game = Game()

game_started = False


# Position labels once
score_label_rect = score_surface.get_rect(
    centerx=score_rect.centerx,
    bottom=score_rect.top - 10
)

next_label_rect = next_surface.get_rect(
    centerx=next_rect.centerx,
    bottom=next_rect.top - 20
)


# Automatic block movement
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)


def draw_start_screen():
    """Draw the arcade-style start screen."""
    screen.fill(Colours.dark_purple)

    title_rect = start_title_surface.get_rect(
        center=(250, 120)
    )
    screen.blit(start_title_surface, title_rect)

    instructions_rect = pygame.Rect(55, 220, 390, 280)

    pygame.draw.rect(
        screen,
        Colours.lilac,
        instructions_rect,
        border_radius=15
    )

    pygame.draw.rect(
        screen,
        Colours.white,
        instructions_rect,
        width=3,
        border_radius=15
    )

    prompt_rect = start_prompt_surface.get_rect(
        center=(250, 270)
    )

    move_rect = move_surface.get_rect(
        center=(250, 350)
    )

    drop_rect = drop_surface.get_rect(
        center=(250, 405)
    )

    rotate_rect = rotate_surface.get_rect(
        center=(250, 460)
    )

    screen.blit(start_prompt_surface, prompt_rect)
    screen.blit(move_surface, move_rect)
    screen.blit(drop_surface, drop_rect)
    screen.blit(rotate_surface, rotate_rect)


def draw_game_screen():
    """Draw the game grid, score panel, and next-piece panel."""
    screen.fill(Colours.dark_purple)

    score_value_surface = title_font.render(
        str(game.score),
        True,
        Colours.white
    )

    screen.blit(score_surface, score_label_rect)
    screen.blit(next_surface, next_label_rect)

    pygame.draw.rect(
        screen,
        Colours.lilac,
        score_rect,
        border_radius=10
    )

    pygame.draw.rect(
        screen,
        Colours.lilac,
        next_rect,
        border_radius=10
    )

    score_value_rect = score_value_surface.get_rect(
        center=score_rect.center
    )

    screen.blit(score_value_surface, score_value_rect)

    game.draw(screen)

    if game.game_over:
        overlay = pygame.Surface((500, 620), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 165))
        screen.blit(overlay, (0, 0))

        game_over_rect = game_over_surface.get_rect(
            center=(250, 245)
        )

        restart_rect = restart_surface.get_rect(
            center=(250, 325)
        )

        menu_rect = menu_surface.get_rect(
            center=(250, 375)
        )

        screen.blit(game_over_surface, game_over_rect)
        screen.blit(restart_surface, restart_rect)
        screen.blit(menu_surface, menu_rect)


while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            # Start screen
            if not game_started:
                if event.key == pygame.K_SPACE:
                    game.reset()
                    game.game_over = False
                    game_started = True

                continue

            # Game-over controls
            if game.game_over:
                if event.key == pygame.K_r:
                    game.reset()
                    game.game_over = False
                    game_started = True

                elif event.key == pygame.K_SPACE:
                    game.reset()
                    game.game_over = False
                    game_started = False

                continue

            # Active gameplay controls
            if event.key == pygame.K_LEFT:
                game.move_left()

            elif event.key == pygame.K_RIGHT:
                game.move_right()

            elif event.key == pygame.K_DOWN:
                game.move_down()
                game.update_score(0, 1)

            elif event.key == pygame.K_UP:
                game.rotate()

            elif event.key == pygame.K_ESCAPE:
                game.reset()
                game.game_over = False
                game_started = False

        # Automatic downward movement
        if (
            event.type == GAME_UPDATE
            and game_started
            and not game.game_over
        ):
            game.move_down()

    if game_started:
        draw_game_screen()
    else:
        draw_start_screen()

    pygame.display.update()
    clock.tick(60)