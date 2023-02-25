import pygame

from generator import TerrainGenerator

SIZE = 900
SCALE = 5

class App:
    def __init__(self, width, height, window_title):
        self.run = True
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(window_title)

        self.generator = TerrainGenerator(SIZE, SCALE)

    def render(self):
        pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(0, 0, SIZE, SIZE))

        self.generator.draw_noise(self.window)
        pygame.display.update()

    def update(self):
        pass

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

    def loop(self):
        while self.run:
            self.handle_events()
            self.update()
            self.render()



app = App(SIZE, SIZE, "Terrain Generator")
app.loop()

