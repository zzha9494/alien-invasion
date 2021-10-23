import sys
import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    def __init__(self, game):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\ZiJie.Zhao\PycharmProjects\alien_invasion\practise\star.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.screen = game.screen

    def update(self):
        self.rect.y += 1


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('stars')

        self.screen_rect = self.screen.get_rect()

        self.stars = pygame.sprite.Group()
        self._create_stars()

    def run_game(self):
        while True:
            self._check_events()

            self._remove_stars()
            self.stars.update()

            self._update_screen()

    def _create_stars(self):
        for column in range(6):
            star = Star(self)
            star.rect.x = star.rect.width + 2 * star.rect.width * column
            self.stars.add(star)

    def _check_edges(self):
        for star in self.stars.sprites():
            if star.rect.top >= self.screen_rect.bottom:
                self._create_stars()
                break

    def _remove_stars(self):
        self._check_edges()
        for star in self.stars.sprites().copy():
            if star.rect.top >= self.screen_rect.bottom:
                self.stars.remove(star)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill((255, 255, 255))

        self.stars.draw(self.screen)

        pygame.display.flip()


stars = Game()
stars.run_game()
