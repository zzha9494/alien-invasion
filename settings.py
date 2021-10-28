class Settings:
    """A class that store all settings."""

    def __init__(self):
        """initialized game settings."""
        # set screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # configure ship
        self.ship_limit = 3

        # configure bullet
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # configure alien speed
        self.alien_drop_speed = 10

        # the scale of speed up the game
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize the settings changed along with running game"""
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 1.0

        # fleet_direction = 1 means move right, -1 means left
        self.fleet_direction = 1

        # get score
        self.alien_points = 50

    def increase_speed(self):
        """increase the speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

