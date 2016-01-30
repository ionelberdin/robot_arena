# robot\_arena
Game developed as a mock-up for a Systems Engineering project at MASI (UC3M)

# How to run this game on your computer

You need to have in your system:
- Python 2.7

In addition, some third party libraries are required:
- PyGame
- Numpy

# How to implement you own decision strategy

To play in the Robot Arena Challenge every
player may write their own decision strategy.

It must be written as a function:

- with arbitrary name
- that accepts a single input
- in a python file with arbitrary name
    eg: some_python_file.py
        >>> def best_strategy_ever(state):
        >>>     ...  # here it comes your logic
        >>>     return (some_x, some_y)  # where you want your robot to go to

This file contains two function examples:
- human\_choice
- step\_by\_step

Input is called *game\_state* in both examples.
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

#### INPUT
game\_state (tuple with 3 elements):

1. game\_state[0] = Information about the arena
  - Arena object. Take a look to the **arena.py** file
    to check its properties and methods.

2. game\_state[1] = Information about players

  - List of tuples:

    [(alive_bool_1, current_pos_tuple_1, goal_pos_tuple_1),
     (alive_bool_2, current_pos_tuple_2, goal_pos_tuple_2),
     (alive_bool_3, current_pos_tuple_3, goal_pos_tuple_3),
     (alive_bool_4, current_pos_tuple_4, goal_pos_tuple_4)]
   
  - eg:

    [(True, (3, 5), (17, 17)),
     (True, (13, 3), (1, 17)),
     (False, (15, 11), (1, 1)),
     (True, (5, 13), (17, 1))]

3. game\_state[2] = timestamp of player turn ending
  - 'seconds since Jan 01 1970. (UTC)'

    eg: 1454005673.82 => which corresponds to 2016-28-01 18:27:53.82
    current timestamp can be obtained using the time library:
        >>> import time
        >>> current_time = time.time()

    Documentation at: https://docs.python.org/2/library/time.html

#### OUTPUT
Target position for current turn.
Tuple with 2 floats.
    
    >>> (4.53, 13.10)
