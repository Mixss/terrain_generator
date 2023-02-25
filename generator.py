import pygame

from perlin_noise import PerlinNoiseFactory


class TerrainGenerator:
    def __init__(self, size, scale):
        self.pnf = PerlinNoiseFactory(2, 1)
        self.noise = self.generate_noise(size, scale)

    def generate_noise(self, size, scale):
        noise = [[0]*size for i in range(size)]
        for i in range(size):
            for j in range(size):
                noise[i][j] = (self.pnf(i/size * scale, j/size * scale) + 1) * 128
        return noise

    def draw(self, window: pygame.Surface, size):
        for i in range(size):
            for j in range(size):
                window.set_at((i, j), (self.noise[i][j], self.noise[i][j], self.noise[i][j]))


