import pygame

"""
To play in the Robot Arena Challenge every
player can write their own decision strategy.

It must be written as a function that accepts a
single input that in the example is called 'game_state'.

Arena topology:
    -> x
  |  _________________  top-right
  v |_|_|_|_|_|_|_|_|_| corner at (18, 0)
  y |_|_|_|_|_|_|_|_|_| center of corner square at (17, 1)
    |_|_|_|_|_|_|_|_|_|
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
"""


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
