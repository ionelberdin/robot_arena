import pygame


class Arena(object):
    colors = {'#': (255, 255, 255),
              'x': (0, 0, 0)}

    def __init__(self, squares, square_size=40):
        self.squares = squares
        self.square_size = square_size

    def draw(self, surface):
        size = self.square_size
        for i, line in enumerate(self.squares):
            for j, square in enumerate(line):
                pygame.draw.rect(surface, self.colors[square],
                                 (j*size, i*size, size, size), 0)

    @classmethod
    def from_file(cls, filename):
        with open("battlefields/{0}".format(filename), "r") as txt:
            squares = []
            for line in txt.readlines():
                squares.append(line.strip().split(" "))
        return cls(squares)
