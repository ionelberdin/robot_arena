import pygame


def human_choice(game_state):
    """
    Wait for user to click over the arena and return
    the position of the mouse when realising a button.

    game_state is not required, but it is included
    as input anyway for compatibility reasons.
    """

    arena = game_state[0]

    while True:
        mouse_over_arena = arena.is_point_over_arena(pygame.mouse.get_pos())
        for event in pygame.event.get():
            mouse_button_up = event.type == pygame.MOUSEBUTTONUP
            if mouse_button_up and mouse_over_arena:
                return pygame.mouse.get_pos()
