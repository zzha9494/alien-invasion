import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to express an alien."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load alien image and set rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # set the position near the lefttop of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the accurate x position
        self.x = float(self.rect.x)

    def update(self):
        """move aliens right"""
        self.x += self.settings.alien_speed
        self.rect.x = self.x
