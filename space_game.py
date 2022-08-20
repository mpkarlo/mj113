import sys

import pygame

from events import PLAYER_TIMER
from hud import Hud
from player import Player
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

        self.player = Player(self)
        self.hud = Hud(self)

        pygame.time.set_timer(PLAYER_TIMER, 250)

    def run(self):
        while True:
            self._check_events()
            self.screen.fill(self.settings.bg_color)
            self.player.update()
            self.hud.update()
            self.player.draw()
            self.hud.draw()
            pygame.display.flip()

    def _check_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event.key)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event.key)
            elif event.type == PLAYER_TIMER:
                self.player.timed_update()

    def _check_keydown_events(self, key):
        if key == pygame.K_UP:
            self.player.mov_u = True
        elif key == pygame.K_DOWN:
            self.player.mov_d = True
        elif key == pygame.K_RIGHT:
            self.player.mov_r = True
        elif key == pygame.K_LEFT:
            self.player.mov_l = True
        elif key == pygame.K_LSHIFT:
            self.player.mov_b = True

    def _check_keyup_events(self, key):
        if key == pygame.K_UP:
            self.player.mov_u = False
        elif key == pygame.K_DOWN:
            self.player.mov_d = False
        elif key == pygame.K_RIGHT:
            self.player.mov_r = False
        elif key == pygame.K_LEFT:
            self.player.mov_l = False
        elif key == pygame.K_LSHIFT:
            self.player.mov_b = False
