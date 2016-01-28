"""
To play in the Robot Arena Challenge every
player may write their own decision strategy.

It must be written as a function:
    * with arbitrary name
    * that accepts a single input
    * in a python file with arbitrary name
    eg: some_python_file.py
        >>> def the_best_strategy_ever(state):
        >>>     ...  # here it comes your logic
        >>>     return (some_x, some_y)  # where you want your robot to go to

This file contains two function examples:
    * human_choice
    * step_by_step

Input is called 'game_state' in both examples.
Nevertheless, its name is completely arbitrary.

Arena topology:
    |-> x
  _  _________________  top-right
  | |_|_|_|_|_|_|_|_|_| corner at (18, 0)
  v |_|_|_|_|_|_|_|_|_| center of corner square at (17, 1)
  y |_|_|_|_|_|_|_|_|_|
    |_|_|_|_|_|_|_|_|_|
    |_|_|_|_|_|_|_|_|_| center of the arena at (9, 9)
    |_|_|_|_|_|_|_|_|_|
    |_|_|_|_|_|_|_|_|_|
    |_|_|_|_|_|_|_|_|_|
    |_|_|_|_|_|_|_|_|_| bottom-right
                        corner at (18, 18)
                        center of corner square at (17, 17)

INPUT: game_state (tuple with 3 elements):

    1) game_state[0] = Information about the arena
       List of lists containing:
           * a number one for ground squares
           * a number zero for pit squares
       eg: [[1, 1, 1, 0, 1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 0, 1, 1, 1, 1],
            [0, 0, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1, 0, 1, 1, 1]]

    2) game_state[1] = Information about players, list of tuples:
        [(alive_bool_1, current_pos_tuple_1, goal_pos_tuple_1),
         (alive_bool_2, current_pos_tuple_2, goal_pos_tuple_2),
         (alive_bool_3, current_pos_tuple_3, goal_pos_tuple_3),
         (alive_bool_4, current_pos_tuple_4, goal_pos_tuple_4)]
       eg: [(True, (3, 5), (17, 17)),
            (True, (13, 3), (1, 17)),
            (False, (15, 11), (1, 1)),
            (True, (5, 13), (17, 1))]

    3) game_state[2] = timestamp of player turn ending
        'seconds since Jan 01 1970. (UTC)'
        eg: 1454005673.82 => which corresponds to 2016-28-01 18:27:53.82
        current timestamp can be obtained using the time library:
            >>> import time
            >>> current_time = time.time()

        Documentation at: https://docs.python.org/2/library/time.html

OUTPUT: target position for current turn. Tuple with 2 floats.
    eg: (4.53, 13.10)
"""

import pygame


def human_choice(game_state):
    """
    Wait for the user to click over the arena and return
    the position of the mouse when realising a button.

    game_state is not required, but it is included
    as input anyway for compatibility reasons
    """

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                return pygame.mouse.get_pos()
