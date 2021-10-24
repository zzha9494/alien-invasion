class GameStats:
    """Track game stats"""

    def __init__(self, ai_game):
        """initialize stats"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """initialize stats that can be changed during game run."""
        self.ships_left = self.settings.ship_limit
