import pygame


class Hud:
    """Manage HUD elements."""

    def __init__(self, game):
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.player = game.player

        self.text_color = self.settings.ui_color
        self.font = pygame.font.SysFont('Consolas', 18, True)

        self.update()

    def draw(self):
        self.screen.blit(self.energy_ui_image, self.energy_ui_rect)
        self.screen.blit(self.health_ui_image, self.health_ui_rect)

    def update(self):
        self._update_health_ui()
        self._update_energy_ui()

    def _update_health_ui(self):
        health_str = f"HEALTH: {self.player.health:.1f}"
        self.health_ui_image = self.font.render(health_str,
                                                True,
                                                self.text_color)
        self.health_ui_rect = self.health_ui_image.get_rect()
        self.health_ui_rect.left = 20
        self.health_ui_rect.top = 20

    def _update_energy_ui(self):
        energy_str = f"ENERGY: {self.player.energy:.1f}"
        self.energy_ui_image = self.font.render(energy_str,
                                                True,
                                                self.text_color)
        self.energy_ui_rect = self.energy_ui_image.get_rect()
        self.energy_ui_rect.left = 20
        self.energy_ui_rect.top = self.health_ui_rect.bottom + 5


