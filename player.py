import pygame.image


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

        # Store player data
        self.health = 100.0
        self.energy = 100.0

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.mov_u and not self.mov_d \
                and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.y_speed
        elif self.mov_d and not self.mov_u \
                and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.y_speed / 2 # move slower reverse.

        if self.mov_r and not self.mov_l \
                and self.rect.right < self.screen_rect.right:
            self.x += self.settings.x_speed
        elif self.mov_l and not self.mov_r \
                and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.x_speed

        self.rect.x = self.x
        self.rect.y = self.y


