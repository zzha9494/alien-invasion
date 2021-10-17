class Settings:
    """A class that store all settings."""

    def __init__(self):
        """initialized game settings."""
        # set screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # configure ship
        self.ship_speed = 1.5
        