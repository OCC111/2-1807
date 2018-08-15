import pygame


pygame.init()

screen = pygame.display.set_mode((480,852))

bg = pygame.image.load("./images/images/background.png")



hero = pygame.image.load("./images/images/hero1.png")

herorect = pygame.Rect(200,500,120,140)

clock = pygame.time.Clock()

while True:
	clock.tick(60)

	herorect.y -= 1

	screen.blit(bg,(0,0))
	screen.blit(hero,herorect)

	if herorect.bottom <= 0:
		herorect.bottom = 700
		pygame.quit()


	pygame.display.update()


