import numpy as np

import pygame


class Robot(pygame.sprite.Sprite):
    size = width, height = 30, 30

    def __init__(self, pos, color):
        pygame.sprite.Sprite.__init__(self)
        self.pos = np.array(pos)
        self.color = color
        self.image_0 = pygame.Surface(self.size)
        self.image_0.fill(self.color)
        self.speed = 0.
        self.angle = 0.5
        self.omega = 0.1

    def update(self, dt=0.1):
        self.angle += self.omega * dt
        self.image = pygame.transform.rotate(pygame.surface.Surface, self.image_0)
        self.rect = self.image.get_rect()
        self.pos = self.pos + self.speed * self.vec * dt

    @property
    def vec(self):
        return np.array([np.cos(self.angle), np.sin(self.angle)])
