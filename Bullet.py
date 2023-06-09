import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('pictures/bullet.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = ai_game.ship.rect.midbottom

        self.y = float(self.rect.y)


    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y


    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)


