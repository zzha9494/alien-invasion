import pygame
import sys
from pygame.sprite import Sprite, Group
import pygame.font


class Settings:
    def __init__(self):
        # 设置屏幕
        self.screen_width, self.screen_height = 1200, 800
        self.screen_color = (255, 255, 255)

        # 设置飞船
        self.ship_width, self.ship_height = 30, 15
        self.ship_color = (0, 0, 0)

        # 设置目标
        self.target_width, self.target_height = 15, 100
        self.target_speed = 1
        self.target_color = (0, 0, 0)

        # 设置子弹
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (0, 0, 0)
        self.bullet_speed = 1

        # 设置生命值
        self.chances_left = 3

        # 设置难度增加率
        self.speedup_scale = 1.1

        self.game_active = False


class Ship:
    def __init__(self, game):
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.width = self.settings.ship_width
        self.height = self.settings.ship_height
        self.color = self.settings.ship_color

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midleft = self.screen_rect.midleft

        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1

    def draw_ship(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Target:
    def __init__(self, game):
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.color = self.settings.target_color

        self.rect = pygame.Rect(0, 0, self.settings.target_width, self.settings.target_height)
        self.rect.midright = self.screen_rect.midright

        self.moving_direction = 1
        self.y = float(self.rect.y)

    def update(self):
        if self.rect.top <= 0 or self.rect.bottom >= self.screen_rect.bottom:
            self.moving_direction *= -1
        self.y += self.settings.target_speed * self.moving_direction
        self.rect.y = self.y

    def draw_target(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Button:
    def __init__(self, game, msg):
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.width, self.height = 200, 50
        self.color = (200, 200, 200)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.msg_image = self.font.render(msg, True, self.text_color, self.color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def center_text(self):
        self.msg_image_rect.center = self.rect.center


class Bullet(Sprite):
    def __init__(self, game):
        super().__init__()
        self.settings = game.settings
        self.screen = game.screen
        self.color = self.settings.bullet_color
        self.width, self.height = self.settings.bullet_width, self.settings.bullet_height
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midright = game.ship.rect.midright

    def update(self):
        self.rect.x += self.settings.bullet_speed

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        # 设置屏幕
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('shooting practise')
        self.screen_rect = self.screen.get_rect()

        self.play_button = Button(self, 'PLAY')
        # 难度按钮
        self.level_2_button = Button(self, 'Lv 2')
        self.level_2_button.rect.midtop = self.screen_rect.midtop
        self.level_2_button.center_text()

        self.level_1_button = Button(self, 'Lv 1')
        self.level_1_button.rect.midright = self.level_2_button.rect.midleft
        self.level_1_button.center_text()

        self.level_3_button = Button(self, 'Lv 3')
        self.level_3_button.rect.midleft = self.level_2_button.rect.midright
        self.level_3_button.center_text()

        self.ship = Ship(self)
        self.target = Target(self)
        self.bullets = Group()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.play_button.rect.collidepoint(mouse_pos) and not self.settings.game_active:
                    self._start_new_game()
                elif self.level_1_button.rect.collidepoint(mouse_pos) and not self.settings.game_active:
                    self._start_new_game()
                    self.settings.target_speed = 1.3
                elif self.level_2_button.rect.collidepoint(mouse_pos) and not self.settings.game_active:
                    self._start_new_game()
                    self.settings.target_speed = 1.5
                elif self.level_3_button.rect.collidepoint(mouse_pos) and not self.settings.game_active:
                    self._start_new_game()
                    self.settings.target_speed = 1.7

    def _start_new_game(self):
        self.ship.rect.midleft = self.screen_rect.midleft
        self.target.rect.midright = self.screen_rect.midright
        self.bullets.empty()
        self.settings.chances_left = 3
        self.settings.target_speed = 1
        self.settings.game_active = True

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        if event.key == pygame.K_SPACE:
            self._fire()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire(self):
        if self.settings.game_active:
            bullet = Bullet(self)
            self.bullets.add(bullet)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.sprites().copy():
            if bullet.rect.left >= self.screen_rect.right:
                self.bullets.remove(bullet)
                self.settings.chances_left -= 1

    def _hit_target(self):
        if pygame.sprite.spritecollide(self.target, self.bullets, True):
            self.settings.target_speed *= self.settings.speedup_scale
        if self.settings.chances_left <= 0:
            self.settings.game_active = False

    def _update_screen(self):
        self.screen.fill(self.settings.screen_color)
        self.ship.draw_ship()
        self.target.draw_target()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        if not self.settings.game_active:
            self.play_button.draw_button()
            self.level_1_button.draw_button()
            self.level_2_button.draw_button()
            self.level_3_button.draw_button()

        # 刷新屏幕
        pygame.display.flip()

    def run_game(self):
        while True:
            self._check_events()

            if self.settings.game_active:
                self.ship.update()
                self.target.update()
                self._update_bullets()
                self._hit_target()

            # 更新屏幕
            self._update_screen()

            # 调试输出
            # print(self.settings.target_speed)


shooting_game = Game()
shooting_game.run_game()
