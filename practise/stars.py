import sys
import pygame
from pygame.sprite import Sprite
from random import randint


class Star(Sprite):
    def __init__(self, game):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\ZiJie.Zhao\PycharmProjects\alien_invasion\practise\star.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.screen = game.screen


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('stars')

        self.stars = pygame.sprite.Group()
        self.create_stars()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def create_stars(self):
        for row in range(4):
            for column in range(6):
                star = Star(self)
                random_number = randint(-10, 10)
                star.rect.x = star.rect.width + 2 * star.rect.width * column + random_number
                random_number = randint(-10, 10)
                star.rect.y = star.rect.height + 2 * star.rect.height * row + random_number
                self.stars.add(star)

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
