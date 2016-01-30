"""
"""

# Standard librariy imports
import sys

# Third party imports
import numpy as np
import pygame

# Project imports
from arena import Arena
from robot import Robot

################################################################################
#                        Game configuration parameters                         #

# Choose strategy for all the players
from strategies.human_choice import human_choice as robot1_logic
from strategies.human_choice import human_choice as robot2_logic
from strategies.human_choice import human_choice as robot3_logic
from strategies.human_choice import human_choice as robot4_logic

# Define game characteristic lengths in pixels
square_width = 40
robot_width = 30

# Choose the arena
arena_name = "symmetric_06"

#                       End of configuration parameters                        #
################################################################################

arena = Arena.from_name(arena_name)
screen = pygame.display.set_mode(arena.size)

positions = arena.corner_centers
angles = [np.pi * i for i in range(4)]
goals = positions[2:] + positions[:2]
colors = [(255, 0, 0, .6), (0, 255, 0, .6), (0, 0, 255, .6), (255, 0, 255, .6)]
robot_widths = [robot_width for _ in range(4)]
strategies = [robot1_logic, robot2_logic, robot3_logic, robot4_logic]
arg_list = zip(positions, angles, goals, colors, robot_widths, strategies)

robots = [Robot(*args) for args in arg_list]


class Manager(object):

    def __init__(self, arena, robots):
        self.arena = arena
        self.robots = robots

    def run_game(self):
        pass

    def assess_winner(self):
        pass


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    arena.draw(screen)
    for robot in robots:
        robot.update()
        screen.blit(robot.image, robot.pos)
    pygame.display.update()
