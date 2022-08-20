import sys

import pygame

from settings import Settings


class SpaceGame:
    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((
            self.settings.screen_width,
            self.settings.screen_height
        ))

        pygame.display.set_caption('MJ 113 - Space Game')

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
