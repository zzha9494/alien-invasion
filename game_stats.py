class GameStats:
    """Track game stats"""

    def __init__(self, ai_game):
        """initialize stats"""
        self.settings = ai_game.settings
        self.reset_stats()

        # not active when game begins
        self.game_active = False

    def reset_stats(self):
        """initialize stats that can be changed during game run."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
