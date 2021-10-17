import pygame


class Ship:
    """A class that manage ships."""

    def __init__(self, ai_game):
        """initialized thr ship and set location."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get the bounding rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # put every new ship on the middle of bottom
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """draw the ship on the location you decided."""
        self.screen.blit(self.image, self.rect)
