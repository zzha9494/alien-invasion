import sys
import pygame
from settings import Settings


class AlienInvasion:
    """A class that manage the resources and behavior of the game."""

    def __init__(self):
        """Initialize the game and create resources. """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """start the main loop."""
        while True:
            # monitor the event of keyboard and mouse.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # re-draw the screen every loop
            self.screen.fill(self.settings.bg_color)

            # make the screen drawn recently visible
            pygame.display.flip()


if __name__ == '__main__':
    # create instance and run.
    ai = AlienInvasion()
    ai.run_game()
