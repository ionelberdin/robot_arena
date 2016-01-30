import pygame


def manchester_distance((x1, y1), (x2, y2)):
    """Sum of absolute distances in both axes, namely: X & Y"""
    return abs(x1 - x2) + abs(y1 - y2)


class Arena(object):
    colors = {'#': (255, 255, 255), 'x': (0, 0, 0)}
    values = {'#': 1, 'x': 0}

    def __init__(self, squares, square_width=40):
        self.squares = squares
        self.square_width = square_width

    @property
    def centers(self):
        return [self.get_square_centers(x_index, y_index)
                for y_index, line in enumerate(self.squares)
                for x_index, item in enumerate(line)]

    @property
    def corner_centers(self):
        x_max = len(self.squares[0]) - 1
        y_max = len(self.squares) - 1
        indices = [(0, 0), (x_max, 0), (x_max, y_max), (0, y_max)]
        return [self.get_square_center(ij) for ij in indices]

    @property
    def height(self):
        return self.square_width * len(self.squares)

    @property
    def ones_and_zeros(self):
        return [[self.values[item] for item in line] for line in self.squares]

    @property
    def pit_centers(self):
        return filter(self.is_point_over_pit, self.centers)

    @property
    def size(self):
        return self.width, self.height

    @property
    def width(self):
        return self.square_width * len(self.squares[0])

    @classmethod
    def from_name(cls, arena_name, square_width=40):
        """
        Load an existent arena from ./arenas/ folder.
        Inputs:
            * name of the file without the extension
            * square_width in pixels (optional)
        """

        with open("arenas/{0}.txt".format(arena_name), "r") as txt:
            squares = []
            for line in txt.readlines():
                squares.append(line.strip().split(" "))
        return cls(squares, square_width)

    def nearest_center(self, (x, y)):
        points = map(lambda xc, yc: ((xc, yc),
                     manchester_distance((x, y), (xc, yc))), self.centers)
        nearest = reduce(lambda p1, p2: p1 if p1[1] < p2[1] else p2, points)
        return nearest[0]

    def draw(self, surface):
        L = self.square_width
        for i, line in enumerate(self.squares):
            I = i * L
            for j, square in enumerate(line):
                J = j * L
                pygame.draw.rect(surface, self.colors[square], (J, I, L, L), 0)

    def get_square_center(self, x_index, y_index):
        L = self.square_width
        return (x_index + .5) * L, (y_index + .5) * L

    def is_point_over_arena(self, (x, y)):
        if (0 < x < self.width) and (0 < y < self.height):
            return True
        return False

    def is_point_over_pit(self, (x, y)):
        d = self.square_width / 2.
        for xp, yp in self.pit_centers:
            if (xp - d < x < xp + d) and (yp - d < y < yp + d):
                return True
        return False
