"""
"""

# Standard librariy imports
from multiprocessing.pool import ThreadPool
import sys
import time
from itertools import count

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

    def __init__(self, arena, robots, screen, dt=0.1, v=100):
        self.arena = arena
        self.robots = robots
        self.screen = screen
        self.dt = dt
        self.v = v

    def run_game(self):
        for turn_count in count():

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            if not any([robot.alive for robot in self.robots]):
                self.game_over()
                break

            # check if robot is still alive
            robot_index = turn_count % len(self.robots)
            if not self.robots[robot_index].alive:
                continue

            self.update_display()

            # update game_state
            robots_state = [robot.state for robot in self.robots]
            limit_timestamp = time.time() + 60
            game_state = (self.arena, robots_state, limit_timestamp, turn_count)

            # get target position
            # pool = ThreadPool(processes=1)
            # choose_move = self.robots[robot_index].choose_move
            # async_result = pool.apply_async(choose_move, (game_state, ))
            # try:
            #     result = async_result.get(timeout=10)
            # except:
            #     print "next"
            #     continue

            target = self.robots[robot_index].choose_move(game_state)
            self.move(robot_index, target)

    def assess_winner(self):
        pass

    def game_over(self):
        pass

    def move(self, robot_index, target):
        robot = self.robots[robot_index]
        x0, y0 = robot.position
        x1, y1 = target
        step = self.dt * self.v
        dist = np.linalg.norm((x1 - x0, y1 - y0))
        N = int(dist / step)
        for x, y in zip(np.linspace(x0, x1, N), np.linspace(y0, y1, N)):
            robot.position = int(x), int(y)
            self.update_display()
            time.sleep(self.dt)

    def update_display(self):
        self.arena.draw(self.screen)
        for robot in self.robots:
            robot.update()
            robot.draw(screen)
            # screen.blit(robot.image, robot.position)
        pygame.display.update()


if __name__ == "__main__":
    manager = Manager(arena=arena, robots=robots, screen=screen)
    manager.run_game()
