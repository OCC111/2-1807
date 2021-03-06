import pygame
from mygroup import *
CREATE_ENEMY_EVENT = pygame.USEREVENT


class PlaneGame(object):
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)

        # 判断是否交替图片，如果是，将图片设置到屏幕顶部
        if is_alt:
            self.rect.y -= self.rect.height

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
        # 创建背景精灵和精灵组
        #global bg1
       # global bg2
        bg1 = BackgroundSprite()
        bg2 = BackgroundSprite(True)
        bg2 = Background("./images/images/background.png")
        self.back_group = pygame.sprite.Group(bg1, bg2)
        bg2.rect.y = -bg2.rect.height
        self.enemy_group = pygame.sprite.Group()
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def __event_handler(self):
        """事件监听"""
        for event in pygame.event.get():

            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # print("敌机出场...")
                enemy = EnemySprite()
                self.enemy_group.add(enemy)

    def __check_collide(self):
        """碰撞检测"""
        pass

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        if event.type == CREATE_ENEMY_EVENT:
            self.enemy_group.add(Enemy())
        self.hero_group.update()
        self.hero_group.draw(self.screen)

    @staticmethod
    def __game_over():
        """游戏结束"""

        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == "__main__":
    game = PlaneGame()
    game.start_game()
