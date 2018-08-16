import pygame
import random
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
CREATE_ENEMY_EVENT = pygame.USEREVENT
class GameSprite(pygame.sprite.Sprite):
	def __init__(self):
		# 1. 调用父类方法，创建敌机精灵，并且指定敌机的图像
		#super().__init__("./images/images/enemy1.png")
		# 2. 设置敌机的随机初始速度 1 ~ 3
		self.speed = random.randint(1, 3)
		# 3. 设置敌机的随机初始位置
		self.rect.bottom = 0
		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,max_x)

	def update(self):
		self.rect.y += self.speed


class EnemySprite(GameSprite):
	def __init__(self):        
		super().__init__()
		self.imagename = "./images/images/enemy1.png"


	def update(self):
		super().update()
		# 2. 判断是否飞出屏幕，如果是，需要将敌机从精灵组删除
		if self.rect.y >= SCREEN_RECT.height:
		#print("敌机飞出屏幕...")   
			self.kill()


class BackgroundSprite(GameSprite):
	"""游戏背景精灵"""
	def __init__(self,is_alt=False):
	    self.imagename = "./images/images/background.png"
	    super().__init__(self.imagename,10)

	    # 判断是否交替图片，如果是，将图片设置到屏幕顶部
	    if is_alt:
	        self.rect.y = -self.rect.height     


	def update(self):
		# 1. 调用父类的方法实现
		super().update()

		# 2. 判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕的上方
		if self.rect.y >= SCREEN_RECT.height:
			self.rect.y = -self.rect.height

class HeroSprite(GameSprite):
	def __init__(self):
		self.imagename = "./images/images/hero.git"
		super().__init__(self.imagename,0)
		#settings 
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.top = 550
	def update(self):
		self.rect.x += self.speed