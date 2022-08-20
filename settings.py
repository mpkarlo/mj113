class Settings:
    def __init__(self):
        # Screen
        self.screen_width = 1200
        self.screen_height = 800

        # UI
        self.bg_color = (29, 41, 81)
        self.ui_color = (240, 248, 255)

        # Player
        self.player_x_speed = 0.9
        self.player_y_speed = 1.2
        self.player_fwd_drain = 0.5
        self.player_rwd_drain = 3.5
        self.player_lat_drain = 1.5
        self.player_boost_drain = 4.5
        self.player_energy_regen = 5
        self.player_boost_mult = 2
        self.player_drain_mult = 0.1
