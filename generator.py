import pygame

from chunk import Chunk
from perlin_noise import PerlinNoiseFactory
from tile import Tile
from world import World


class TerrainGenerator:

    size = 1
    scale = 1
    pnf = PerlinNoiseFactory(2, 1)

    @staticmethod
    def get_noise_at(x, y):
        return TerrainGenerator.pnf(x/TerrainGenerator.size * TerrainGenerator.scale, y/TerrainGenerator.size * TerrainGenerator.scale)

    @staticmethod
    def generate_chunk(world: World, chunk_x, chunk_y, valleys_height):
        """generates chunk for given x,y chunk coordinates"""
        tile_start_x = chunk_x * world.chunk_size
        tile_start_y = chunk_y * world.chunk_size

        for x in range(tile_start_x, tile_start_x+world.chunk_size):
            y = round((TerrainGenerator.get_noise_at(x, 0) + 1) * valleys_height/ 2)
            if y > tile_start_y + world.chunk_size:
                continue
            elif y < tile_start_y:
                y = tile_start_y

            chunk = world.get_chunk_at(chunk_x, chunk_y)
            for i in range(y, tile_start_y + world.chunk_size):
                tile = Tile(x, i, (123, 43, 11))
                chunk.tiles[x % world.chunk_size][i % world.chunk_size] = tile



