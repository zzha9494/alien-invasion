import pygame.font


class Scoreboard:
    """A class showing score"""

    def __init__(self, ai_game):
        """initialize properties related to showing score"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # the font settings used by showing score
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # prepare image of score
        self.prep_score()

    def prep_score(self):
        """render a font into an image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # show the score on top right
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """show score on screen"""
        self.screen.blit(self.score_image, self.score_rect)
