import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """class for bullet object"""

    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen
        # first create a matrix for bullet on (0,0),then set its righting loc
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # decimals for loc
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """movement of the bullet"""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)
