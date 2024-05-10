import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """class to represent aliens"""

    def __init__(self, ai_settings, screen):
        """initialize aliens and set the loc"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # load image and set rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # inital loc is in the upper-left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # specific loc
        self.x = float(self.rect.x)


    def check_edges(self):
        """check if the aliens collide with the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x

    def blitme(self):
        """draw alien at the specified loc"""
        self.screen.blit(self.image, self.rect)
