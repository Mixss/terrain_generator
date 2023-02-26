import pygame

from chunk import Chunk
from perlin_noise import PerlinNoiseFactory
from tile import Tile
from world import World


class TerrainGenerator:

    size = 1
    scale = 1
    pnf = PerlinNoiseFactory(2, 1)

    def __init__(self, size, scale):
        self.pnf = PerlinNoiseFactory(2, 1)
        self.size = size
        self.scale = scale

    @staticmethod
    def get_noise_at(x, y):
        return TerrainGenerator.pnf(x/TerrainGenerator.size * TerrainGenerator.scale, y/TerrainGenerator.size * TerrainGenerator.scale)

    def draw_noise(self, window: pygame.Surface):
        for i in range(self.size):
            for j in range(self.size):
                color = (self.get_noise_at(i, j) + 1) * 128
                window.set_at((i, j), (color, color, color))

    def generate_terrain(self, world: World):
        for x in range(world.width):
            y = round((self.get_noise_at(x, 0) + 1) * world.height/2)
            for i in range(y, world.height-1):
                tile = Tile(x, i, (123, 43, 11))
                world.set_tile(tile)

    @staticmethod
    def generate_chunk(world: World, chunk_x, chunk_y):
        """generates chunk for given x,y chunk coordinates"""
        tile_start_x = chunk_x * world.chunk_size
        tile_start_y = chunk_y * world.chunk_size

        for x in range(tile_start_x, tile_start_x+world.chunk_size):
            y = round((TerrainGenerator.get_noise_at(x, 0) + 1) * world.height / 2)
            if y > tile_start_y + world.chunk_size:
                continue
            elif y < tile_start_y:
                y = tile_start_y

            chunk = world.get_chunk_at(chunk_x, chunk_y)
            for i in range(y, tile_start_y + world.chunk_size):
                tile = Tile(x, i, (123, 43, 11))
                chunk.tiles[x % world.chunk_size][i % world.chunk_size] = tile



