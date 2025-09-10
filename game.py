import pygame

from data import *
from player import Player

class Main:
    def __init__(self):
        pygame.init()

        self.name = pygame.display.set_caption("Pixel Dash")
        self.window = pygame.display.set_mode((1200, 800))
        self.clock = pygame.time.Clock()
        self.running = True

        self.player = Player(100, 600)

        self.run()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.window.fill((0, 0, 0))  # Clear screen with black
            self.player.update()
            self.player.draw(self.window)

            pygame.display.flip()  # Update display
            self.clock.tick(60)  # Cap at 60 FPS

        pygame.quit()


if __name__ == "__main__":
    game = Main()
