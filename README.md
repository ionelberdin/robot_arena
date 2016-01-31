# robot\_arena
Game developed as a mock-up for a Systems Engineering project at MASI (UC3M)

# Does it work?
Nop, it is currently in development.  
Robots move when you click on the board, but most functionallities are not implemented yet.

# How to run this game on your computer

You need to have in your system:
- Python 2.7

In addition, some third party libraries are required:
- PyGame
- Numpy

# How to implement your own decision strategy

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
- and placed inside **strategies** folder

**strategies** folder contains some examples:
- human\_choice.py
- step\_by\_step.py

Input is called *game\_state* in those examples.
Nevertheless, its name is completely arbitrary.

Arena axes:

       |-> x
     _  _________________ 
     | |_|_|_|_|_|_|_|_|_|
     v |_|_|_|_|_|_|_|_|_|
     y |_|_|_|_|_|_|_|_|_|
       |_|_|_|_|_|_|_|_|_|
       |_|_|_|_|_|_|_|_|_|
       |_|_|_|_|_|_|_|_|_|
       |_|_|_|_|_|_|_|_|_|
       |_|_|_|_|_|_|_|_|_|
       |_|_|_|_|_|_|_|_|_|
                          
In order to make you easier to deal with movement choices,
some helping functions have been included in **simulator.py** file.

In particular, **simulate\_move** returns game\_state after one move.

#### INPUT
1. game\_state dictionary:

  . game\_state['arena'] = Information about the arena
    - Arena object. Take a look to the **arena.py** file
      to check its properties and methods.
  
  . game\_state['robots'] = Information about players
  
    - List of **dictionaries with public properties** about robots:
      * alive: True or False
      * position: (x, y) of robot center
      * goal: (xg, yg)
      * width: characteristic length, diameter for circular robots  
  
  . game\_state['turn'] = turn number
    - Incremental value starting at 0 and adding 1 for every completed turn
    - To compute which player moves:  
      >>> game\_state[3] % 4  # if 4 == number_of_players  
      Giving:  
      >>> 0  # for player 1  
      >>> 1  # for player 2  
      >>> 2  # for player 3  
      >>> 3  # for player 4  

2. game\_state['time\_limit'] = timestamp of player turn ending  
    _seconds since Jan 01 1970. (UTC)_  
    eg: 1454005673.82 => 2016-28-01 18:27:53.82  
    Current timestamp can be obtained using the time library:  
        >>> import time  
        >>> current_time = time.time()

    Documentation at: https://docs.python.org/2/library/time.html

#### OUTPUT
Target position for current turn.
Tuple with 2 floats.
    
    >>> (4.53, 13.10)

Be careful when relying on floats, since this simulator works with pixels (integer scale).
