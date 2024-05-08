import pygame
from settings import Settings


class Ship:
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting"""
        self.screen = screen
        self.ai_settings = ai_settings
        # loading ship and get its matrix holding
        self.image = pygame.image.load("images/ship.bmp")
        # get rect obj
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # set new ship on the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Set decimals in the attributes of the ship
        self.center = float(self.rect.centerx)

        # moving flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the loc of the ship based on moving flag"""
        # rect 属性值为int，不易调整
        # if self.moving_right:
        #     self.rect.centerx += 1
        # if self.moving_left:
        #     self.rect.centerx -= 1
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # update rect based on self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship on the specific loc"""
        self.screen.blit(self.image, self.rect)
