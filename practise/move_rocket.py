import pygame
import sys


def run_game():

    # 屏幕设置
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('rocket')

    # 火箭图像
    image = pygame.image.load(r'C:\Users\ZiJie.Zhao\PycharmProjects\alien_invasion\images\ship.bmp')
    image_rect = image.get_rect()

    # 屏幕rect
    screen_rect = screen.get_rect()

    # 设置初始位置
    image_rect.center = screen_rect.center

    # 火箭位移标志
    move_right = False
    move_left = False
    move_up = False
    move_down = False

    # 主循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # 判断移动标志
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move_right = True
                elif event.key == pygame.K_LEFT:
                    move_left = True
                elif event.key == pygame.K_UP:
                    move_up = True
                elif event.key == pygame.K_DOWN:
                    move_down = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    move_right = False
                elif event.key == pygame.K_LEFT:
                    move_left = False
                elif event.key == pygame.K_UP:
                    move_up = False
                elif event.key == pygame.K_DOWN:
                    move_down = False

        # 移动火箭
        if move_right and image_rect.right < screen_rect.right:
            image_rect.x += 1
        if move_left and image_rect.left > 0:
            image_rect.x -= 1
        if move_up and image_rect.top > 0:
            image_rect.y -= 1
        if move_down and image_rect.bottom < screen_rect.bottom:
            image_rect.y += 1

        screen.fill((230, 230, 230))
        screen.blit(image, image_rect)

        # 更新屏幕
        pygame.display.flip()


run_game()
