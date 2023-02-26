import pygame

from chunk import Chunk


class World:
    def __init__(self, chunk_size):
        self.__chunks = {}
        self.chunk_size = chunk_size

    def set_tile(self, tile):
        x = tile.x
        y = tile.y
        chunk = self.get_chunk_for(x, y)
        chunk.tiles[x % self.chunk_size][y % self.chunk_size] = tile

    def get_chunk_for(self, x, y):
        """returns the chunk for the tile at x,y coordinates"""
        return self.get_chunk_at(x // self.chunk_size, y // self.chunk_size)

    def get_chunk_at(self, x, y):
        """returns the chunk for given x,y chunk coordinates"""
        key = self.__code_chunk_key(x, y)
        if key in self.__chunks:
            return self.__chunks[key]
        else:
            chunk = Chunk(x, y, self.chunk_size)
            self.__chunks[key] = chunk
            return chunk

    def if_chunk_exists(self, x, y):
        return self.__code_chunk_key(x, y) in self.__chunks

    def __code_chunk_key(self, x, y):
        return f"{x} {y}"

    def draw_chunk(self, x, y, camera_offset_x, camera_offset_y, window: pygame.Surface, scale):
        """draws chunk at x,y chunk coordinates"""
        chunk = self.get_chunk_at(x, y)
        for y in range(chunk.size):
            for x in range(chunk.size):
                tile = chunk.tiles[x][y]
                if tile is not None:
                    render_x = tile.x * scale + camera_offset_x
                    render_y = tile.y * scale + camera_offset_y
                    pygame.draw.rect(window, tile.color, pygame.Rect(render_x, render_y, scale, scale))

