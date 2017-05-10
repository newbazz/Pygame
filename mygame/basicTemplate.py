#Basic pygame template
###########import scetion###############
import pygame 
import random


########################################


########### variables ##################
HEIGHT=480
WIDTH=360
FPS=30

#Colors
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.Surface((50,50))
		self.image.fill(green)
		self.rect=self.image.get_rect()
		self.rect.center=(WIDTH/2,HEIGHT/2)
		self.yspeed=5
	def update(self):
		self.rect.x+=5
		self.rect.y+=self.yspeed
		if self.rect.bottom > HEIGHT-200:
			self.yspeed=-5
		if self.rect.top < 200:
			self.yspeed=5
		if self.rect.left > WIDTH:
			self.rect.right=0
#######################################


################initialise game########
pygame.init()
pygame.mixer.init()

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("my first pygame")
clock=pygame.time.Clock()
group=pygame.sprite.Group()
player=Player()
group.add(player)

#######################################


##############Game loop################
inplay=True
while inplay:
	#keep loop run at the right speed
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			inplay=False
	group.update()
	screen.fill(black)
	group.draw(screen)
	pygame.display.flip()

pygame.quit()
	

#########################################



