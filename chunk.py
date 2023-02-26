class Chunk:
    def __init__(self, x, y, size):
        # x and y are coordinates position
        self.x = x
        self.y = y
        self.size = size
        self.tiles = [[None] * size for _ in range(size)]