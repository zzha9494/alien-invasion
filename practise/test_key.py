import pygame
import sys


def run_game():

    # 屏幕设置
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('test key')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)
                print(type(event.key))


run_game()
