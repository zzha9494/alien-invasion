import pygame


class Ship:
    """A class that manage ships."""

    def __init__(self, ai_game):
        """initialized thr ship and set location."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get the bounding rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # put every new ship on the middle of bottom
        self.rect.midbottom = self.screen_rect.midbottom

        # store float number in attribute x
        self.x = float(self.rect.x)

        # moving flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """change the position of ship according to moving flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update rect according to self.x
        self.rect.x = self.x

    def blitme(self):
        """draw the ship on the location you decided."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """put the ship on midbottom of screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
