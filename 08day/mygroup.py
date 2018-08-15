import pygame

class GameSprite(pygame,sprite.Sprite):
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

		