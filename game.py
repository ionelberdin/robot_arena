import sys

import pygame

from arena import Arena
from robot import Robot

size = width, height = 360, 360

arena_test = Arena.from_file("symmetric_04.txt")

screen = pygame.display.set_mode(size)

a = 20-15
b = 9*40-20-15

robots = [
    Robot((a, a), (255, 0, 0, 0.6)),
    Robot((b, a), (0, 255, 0, 0.6)),
    Robot((a, b), (0, 0, 255, 0.6)),
    Robot((b, b), (255, 0, 255, 0.6))
]

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    arena_test.draw(screen)
    for robot in robots:
        robot.update()
        screen.blit(robot.image, robot.pos)
    pygame.display.update()
