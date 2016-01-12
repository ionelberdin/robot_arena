import sys

import pygame

from arena import Arena

size = width, height = 450, 450

arena_test = Arena.from_file("symmetric_01.txt")

screen = pygame.display.set_mode(size)

arena_test.draw(screen)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        pygame.display.update()
