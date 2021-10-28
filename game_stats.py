import json


class GameStats:
    """Track game stats"""

    def __init__(self, ai_game):
        """initialize stats"""
        self.settings = ai_game.settings
        self.reset_stats()

        # not active when game begins
        self.game_active = False

        # read log
        self.log_path = 'log.json'

        try:
            with open(self.log_path) as f:
                self.high_score = json.load(f)
        except FileNotFoundError:
            self.high_score = 0

    def reset_stats(self):
        """initialize stats that can be changed during game run."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def save_score(self):
        filename = self.log_path
        with open(filename, 'w') as f:
            json.dump(self.high_score, f)
