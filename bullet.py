import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets."""

    def __init__(self, ai_game):
        """create a bullet object on the current position of ship"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create a rect of bullet on (0,0), then move to right position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.screen_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # store the bullet position by float
        self.y = float(self.rect.y)

    def update(self):
        """move the bullet upward."""
        # update the float of bullet position
        self.y -= self.settings.bullet_speed
        # update the position of rect of bullet
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet on screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
