import sys

import pygame


def human_choice(game_state):
    """
    Wait for user to click over the arena and return
    the position of the mouse when realising a button.
    """

    arena = game_state[0]

    while True:
        event = pygame.event.poll()

        if (event.type == pygame.MOUSEBUTTONUP and
                arena.is_point_over_arena(event.pos)):
            return event.pos

        elif event.type == pygame.QUIT:
            sys.quit()
