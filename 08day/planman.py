import pygame
from mygroup import *
class PlaneGame(object):
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()
    def start_game(self):
        while True:

            # 1. 设置刷新帧率
            self.clock.tick(60)

            # 2. 事件监听
            self.__event_handler()

            # 3. 碰撞检测
            self.__check_collide()

            # 4. 更新精灵组
            self.__update_sprites()

            # 5. 更新屏幕显示
            pygame.display.update()

    def __create_sprites(self):
        self.back_group = pygame.sprite.Group()
        # 敌机组
        self.enemy_group = pygame.sprite.Group()
        # 英雄组
        self.hero_group = pygame.sprite.Group()

    def __event_handler(self):
        """事件监听"""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                PlaneGame.__game_over()

    def __check_collide(self):
        """碰撞检测"""
        self.back_group = pygame.sprite.Group()
        # 敌机组
        self.enemy_group = pygame.sprite.Group()
        # 英雄组
        self.hero_group = pygame.sprite.Group()


    def __update_sprites(self):
        """更新精灵组"""
        for group in [self.back_group, self.enemy_group, self.hero_group]:
            group.update()
            group.draw(self.screen)


    @staticmethod
    def __game_over():
       """游戏结束"""

       print("游戏结束")
       pygame.quit()
       exit()



if __name__ == "__main__":
    game = PlaneGame()
    game.start_game()
