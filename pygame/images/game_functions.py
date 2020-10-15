import sys
import pygame
import random


def check_events(ship):
    """ 响应按键和鼠标事件 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                check_keyright_events(event,ship)
            elif event.key == pygame.K_LEFT:
                check_keyleft_events(event,ship)
            elif event.key == pygame.K_UP:
                check_keyup_events(event,ship)
            elif event.key == pygame.K_DOWN:
                check_keydown_events(event,ship)

def check_keyup_events(event, ship):
    if event.key == pygame.K_UP:
        # 向上移动飞船
        ship.rect.bottom -= 10
        ship.moving_right = False
        ship.moving_left = False
        ship.moving_up = True
        ship.moving_down = False


def check_keydown_events(event, ship):
    if event.key == pygame.K_DOWN:
        # 向下移动飞船
        ship.rect.bottom += 10
        ship.moving_right = False
        ship.moving_left = False
        ship.moving_up = False
        ship.moving_down = True


def check_keyright_events(event, ship):
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.rect.centerx += 10
        ship.moving_right = True
        ship.moving_left = False
        ship.moving_up = False
        ship.moving_down = False


def check_keyleft_events(event, ship):
    if event.key == pygame.K_LEFT:
        # 向左移动飞船
        ship.rect.centerx -= 10
        ship.moving_left = True
        ship.moving_right = False
        ship.moving_up = False
        ship.moving_down = False


def update_screen(ai_settings, screen, ship):
    # colors = [(10, 32, 44), (23, 42, 223), (41, 21, 213), (233, 23, 3)]
    # screen.fill(colors[random.randint(0, len(colors) - 1)])
    ship.update()
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
