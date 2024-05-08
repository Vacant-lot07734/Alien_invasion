import pygame
import sys

import bullet
from bullet import Bullet


def fire_bullet(ai_settings, screen, ship, bullets):
    # creat a bullet, add it to group
    if len(bullets) >= ai_settings.bullets_allowed:
        return
    new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_l:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_j:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_l:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_j:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """respond to keyboard events and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_bullets(bullets):
    """update loc of the bullets, and del bullets"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def update_screen(ai_settings, screen, ship, bullets):
    """update the obj on the screen, and switch to a new screen"""
    # redraw screen on each loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # redraw all the bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # set new screen visible
    pygame.display.flip()
