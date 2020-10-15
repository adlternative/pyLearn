import pygame


class Ship():
    def __init__(self,ai_settings,screen):
        """ 初始化飞船并设置其初始位置 """
        self.screen = screen
        self.ai_settings=ai_settings
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # print(self.rect.bottom)#608 底部距离顶部
        # print(self.rect.centerx)#540 中间的x坐标
        # print(self.rect.height)#608    高度
        # print(self.rect.right)#x右
        # print(self.rect.left)#x左
        # print(self.rect.top)# y顶部
        print(self.rect.x)#x 默认0　左上　
        print(self.rect.y)#y 默认0　左上

        self.screen_rect = screen.get_rect()
        # print(self.screen_rect)
        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.center =float(self.rect.centerx)
        self.height =float(self.rect.bottom)

    def update(self):
        # print(self.rect.x)  # x 0
        # print(self.rect.y)  # y 0

        if self.moving_right and self.rect.right< self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
            self.rect.centerx=self.center
        elif self.moving_left and self.rect.left>0:
            self.center -= self.ai_settings.ship_speed_factor
            self.rect.centerx=self.center

        elif self.moving_up and self.rect.top>0:
            self.height -= self.ai_settings.ship_speed_factor
            self.rect.bottom=self.height
        elif self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.height += self.ai_settings.ship_speed_factor
            self.rect.bottom=self.height

    def blitme(self):
        """ 在指定位置绘制飞船 """
        self.screen.blit(self.image, self.rect)
