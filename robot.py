import numpy as np

import pygame


class Robot(pygame.sprite.Sprite):

    def __init__(self, position, angle, goal, color, width, choose_move):
        pygame.sprite.Sprite.__init__(self)

        self.position = np.array(position)
        self.angle = angle
        self.goal = goal
        self.color = color
        self.width = width
        self.choose_move = choose_move

        self.size = width, width
        self.image_0 = pygame.Surface(self.size)
        self.image_0.fill(self.color)

        self.alive = True
        self.speed = 0.
        self.omega = 0.

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.px_pos, self.width/2, 0)

    def update(self, dt=0.1):
        self.angle += self.omega * dt
        # self.image = pygame.transform.rotate(pygame.surface.Surface,
        #                                      self.image_0)
        self.image = self.image_0
        self.rect = self.image.get_rect()
        self.position = self.position + self.speed * self.direction * dt

    @property
    def direction(self):
        return np.array([np.cos(self.angle), np.sin(self.angle)])

    @property
    def px_pos(self):
        return tuple([int(pos) for pos in self.position])

    @property
    def state(self):
        public_properties = {
            'alive': self.alive,
            'position': self.position,
            'goal': self.goal,
            'width': self.width
        }
        return public_properties
