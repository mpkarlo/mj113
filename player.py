import pygame.image

from util import clamp


class Player:
    def __init__(self, game):
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # Load player's ship image and get its rect.
        self.image = pygame.image.load('sprites/ship_L.png')
        self.rect = self.image.get_rect()

        # Start a new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store decimal values of player's position for fine movement.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Store movement flags.
        self.mov_r = False
        self.mov_l = False
        self.mov_u = False
        self.mov_d = False
        self.mov_b = False

        # Store player data
        self.health = 100.0
        self.energy = 100.0

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self._update_mov()

    def _update_mov(self):
        delta_x = 0.0
        delta_y = 0.0

        if self.mov_u and not self.mov_d \
                and self.rect.top > self.screen_rect.top:
            delta_y -= self.settings.player_y_speed
        elif self.mov_d and not self.mov_u \
                and self.rect.bottom < self.screen_rect.bottom:
            delta_y += self.settings.player_y_speed / 2  # move slower reverse.

        if self.mov_r and not self.mov_l \
                and self.rect.right < self.screen_rect.right:
            delta_x+= self.settings.player_x_speed
        elif self.mov_l and not self.mov_r \
                and self.rect.left > self.screen_rect.left:
            delta_x -= self.settings.player_x_speed

        self.x += delta_x * \
                  (self.settings.player_boost_mult if self.mov_b else 1) * \
                  (self.settings.player_drain_mult if self.energy < 25 else 1)
        self.y += delta_y * \
                  (self.settings.player_boost_mult if self.mov_b else 1) * \
                  (self.settings.player_drain_mult if self.energy < 25 else 1)

        self.rect.x = self.x
        self.rect.y = self.y

    def timed_update(self):
        """Update player time based stats."""
        mov_lr = self.mov_l or self.mov_r
        energy_drain = (self.settings.player_fwd_drain * self.mov_u) + \
                       (self.settings.player_rwd_drain * self.mov_d) + \
                       (self.settings.player_lat_drain * mov_lr) + \
                       (self.settings.player_boost_drain * self.mov_b)
        energy_delta = self.energy - energy_drain + \
                       self.settings.player_energy_regen
        self.energy = clamp(energy_delta, 0, 100)
