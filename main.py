import pygame

from camera import Camera
from generator import TerrainGenerator
from world import World

SIZE = 900
SCALE = 16
CHUNK_SIZE = 16
BLOCK_SIZE = 5


class App:
    def __init__(self, width, height, window_title):
        self.world = None
        self.run = True
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(window_title)
        self.camera = Camera(width, height)

    def generate_world(self):
        TerrainGenerator.size = SIZE
        TerrainGenerator.scale = SCALE
        self.world = World(BLOCK_SIZE)

    def draw_world(self, world, window: pygame.Surface, camera, scale):
        render_border_left = -camera.x // (world.chunk_size * scale)
        render_border_right = (-camera.x + window.get_width()) // (world.chunk_size * scale) + 1
        render_border_up = -camera.y // (world.chunk_size * scale)
        render_border_down = (-camera.y + window.get_height()) // (world.chunk_size * scale) + 1

        for y in range(render_border_up, render_border_down):
            for x in range(render_border_left, render_border_right):
                world.draw_chunk(x, y, camera.x, camera.y, window, scale)

    def render(self):
        pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(0, 0, self.window.get_width(), self.window.get_height()))

        self.draw_world(self.world, self.window, self.camera, BLOCK_SIZE)

        pygame.display.update()

    def update(self):
        render_border_left = -self.camera.x // (self.world.chunk_size * BLOCK_SIZE)
        render_border_right = (-self.camera.x + self.window.get_width()) // (self.world.chunk_size * BLOCK_SIZE) + 1
        render_border_up = -self.camera.y // (self.world.chunk_size * BLOCK_SIZE)
        render_border_down = (-self.camera.y + self.window.get_height()) // (self.world.chunk_size * BLOCK_SIZE) + 1

        for y in range(render_border_up, render_border_down):
            for x in range(render_border_left, render_border_right):
                if not self.world.if_chunk_exists(x, y):
                    TerrainGenerator.generate_chunk(self.world, x, y, 150)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.camera.x += 5
        if keys[pygame.K_RIGHT]:
            self.camera.x -= 5
        if keys[pygame.K_UP]:
            self.camera.y += 5
        if keys[pygame.K_DOWN]:
            self.camera.y -= 5

    def loop(self):
        self.generate_world()

        while self.run:
            self.handle_events()
            self.update()
            self.render()


app = App(1200, 900, "Terrain Generator")
app.loop()

