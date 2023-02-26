import pygame

from generator import TerrainGenerator
from world import World

SIZE = 900
SCALE = 16
CHUNK_SIZE = 16
BLOCK_SIZE = 10


class App:
    def __init__(self, width, height, window_title):
        self.world = None
        self.run = True
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(window_title)
        self.camera_offset_x = 0
        self.camera_offset_y = 0

    def generate_world(self):
        TerrainGenerator.size = SIZE
        TerrainGenerator.scale = SCALE
        self.world = World(500, 100, BLOCK_SIZE)

    def draw_world(self, world, window: pygame.Surface, camera_offset_x, camera_offset_y, scale):
        render_border_left = -camera_offset_x // (world.chunk_size * scale)
        render_border_right = (-camera_offset_x + window.get_width()) // (world.chunk_size * scale) + 1
        render_border_up = -camera_offset_y // (world.chunk_size * scale)
        render_border_down = (-camera_offset_y + window.get_height()) // (world.chunk_size * scale) + 1

        for y in range(render_border_up, render_border_down):
            for x in range(render_border_left, render_border_right):
                if not world.if_chunk_exists(x, y):
                    TerrainGenerator.generate_chunk(world, x, y)
                world.draw_chunk(x, y, camera_offset_x, camera_offset_y, window, scale)

    def render(self):
        pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(0, 0, self.window.get_width(), self.window.get_height()))

        self.draw_world(self.world, self.window, self.camera_offset_x, self.camera_offset_y, BLOCK_SIZE)

        pygame.display.update()

    def update(self):
        pass

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.camera_offset_x += 5
        if keys[pygame.K_RIGHT]:
            self.camera_offset_x -= 5
        if keys[pygame.K_UP]:
            self.camera_offset_y += 5
        if keys[pygame.K_DOWN]:
            self.camera_offset_y -= 5

    def loop(self):
        self.generate_world()

        while self.run:
            self.handle_events()
            self.update()
            self.render()


app = App(1200, 900, "Terrain Generator")
app.loop()

