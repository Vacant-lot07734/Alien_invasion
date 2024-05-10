import pygame
import sys
from alien import Alien
import bullet
from bullet import Bullet


def fire_bullet(ai_settings, screen, ship, bullets):
    # creat a bullet, add it to group
    if len(bullets) >= ai_settings.bullets_allowed:
        return
    new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    """calculates the number of aliens each row"""
    available_space_x = ai_settings.screen_width - alien_width * 2
    number_aliens_x = int(available_space_x / (alien_width * 2))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """calculates the number of row"""
    available_space_y = (ai_settings.screen_height - alien_height * 3 - ship_height)
    number_rows = int(available_space_y / (alien_height * 2))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """creates an alien and adds it to the screen"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + alien_number * alien_width * 2
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + alien.rect.height * row_number * 2
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """create alien fleet"""
    # The alien distance is the alien width
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        # create an alien and add it to the cur row
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """check if alien arrive at the edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """change fleet direction and move down"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, aliens):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()


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
    elif event.key == pygame.K_q:
        sys.exit()


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


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """update the obj on the screen, and switch to a new screen"""
    # redraw screen on each loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # redraw all the bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    aliens.draw(screen)

    # set new screen visible
    pygame.display.flip()
