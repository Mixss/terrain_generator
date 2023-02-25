import pygame

from perlin_noise import PerlinNoiseFactory


class TerrainGenerator:
    def __init__(self, size, scale):
        self.pnf = PerlinNoiseFactory(2, 1)
        self.size = size
        self.scale = scale

    def get_noise_at(self, x, y):
        return self.pnf(x/self.size * self.scale, y/self.size * self.scale)

    def draw_noise(self, window: pygame.Surface):
        for i in range(self.size):
            for j in range(self.size):
                color = (self.get_noise_at(i,j) + 1) * 128
                window.set_at((i, j), (color, color, color))

    def draw(self, window: pygame.Surface):
        pass


