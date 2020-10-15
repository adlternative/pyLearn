import sys
import pygame
from pygame.sprite import Group
import images.game_functions as gf
from settings import Settings
from   ship import Ship
def run_game():
# 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_setting=Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    ship =Ship(ai_setting,screen)
    bullets=Group()
    # screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    # 开始游戏的主循环
    while True:
    # 监视键盘和鼠标事件
        gf.check_events(ship)
        gf.update_screen(ai_setting,screen,ship)
if __name__ == '__main__':

    run_game()