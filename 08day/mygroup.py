import pygame
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

class GameSprite(pygame.sprite.Sprite):
	def __init__(self,imagename,speed=1):
		super().__init__()
		self.image = pygame.image.load(imagename)
		self.rect = self.image.get_rect()
		self.speed = speed

	def update(self):
		self.rect.y += self.speed


class EnemySprite(GameSprite):
	def __init__(self):
		self.imagename = "./images/images/enemy0.png"
		super().__init__(self.imagename)

	def update(self):
		super().update()


class BackGroundSprites(EnemySprite):
    """游戏背景精灵"""

    def update(self):

        # 1. 调用父类的方法实现
        super().update()

        # 2. 判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height
            
class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):

        # 1. 调用父类方法，创建敌机精灵，并且指定敌机的图像
        super().__init__("./images/enemy1.png")

        # 2. 设置敌机的随机初始速度

        # 3. 设置敌机的随机初始位置

    def update(self):

        # 1. 调用父类方法，让敌机在垂直方向运动
        super().update()

        # 2. 判断是否飞出屏幕，如果是，需要将敌机从精灵组删除
        if self.rect.y >= SCREEN_RECT.height:
            print("敌机飞出屏幕...")    


		