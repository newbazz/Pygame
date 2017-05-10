#Basic pygame template
###########import scetion###############
import pygame 
import random


########################################


########### variables ##################
HEIGHT=600
WIDTH=480
FPS=60

#Colors
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)
class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.Surface((50,40))
		self.image.fill(green)
		self.rect=self.image.get_rect()
		self.radius=22
		#pygame.draw.circle(self.image,red,self.rect.center,self.radius)
		self.rect.centerx=WIDTH/2
		self.rect.bottom=HEIGHT-10
		self.speedx=0
	def update(self):
		self.speedx=0
		keystate=pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speedx=-5
		if keystate[pygame.K_RIGHT]:
			self.speedx=5
		self.rect.x+=self.speedx
		if self.rect.right > WIDTH:
			self.rect.right=WIDTH
		if self.rect.left<0:
			self.rect.left=0
	def shoot(self):
		m=Bullet(self.rect.centerx,self.rect.top)
		group.add(m)
		bullet.add(m)

		
class Mob(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.Surface((30,40))
		self.image.fill(red)
		self.rect=self.image.get_rect()
		self.radius=15
		#pygame.draw.circle(self.image,red,self.rect.center,self.radius)
		self.rect.x=random.randrange(WIDTH-self.rect.width)
		self.rect.y=random.randrange(-100,-40)
		self.speedy=random.randrange(1,8)
		self.speedx=random.randrange(-3,3)
	def update(self):
		self.rect.y+=self.speedy
		self.rect.x+=self.speedx
		if self.rect.top > HEIGHT +10 or self.rect.left<-25 or self.rect.right>WIDTH+25:
			self.rect.x=random.randrange(WIDTH-self.rect.width)
			self.rect.y=random.randrange(-100,-40)
			self.speedy=random.randrange(1,8)

class Bullet(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.Surface((10,20))
		self.image.fill(yellow)
		self.rect=self.image.get_rect()
		self.rect.bottom=y
		self.rect.centerx=x
		self.speedy=-8
	def update(self):
		self.rect.y+=self.speedy
		if self.rect.bottom <0:
			self.kill()
###########################################################


################initialise game########
pygame.init()
pygame.mixer.init()

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("my first pygame")
clock=pygame.time.Clock()
group=pygame.sprite.Group()
mob=pygame.sprite.Group()
bullet=pygame.sprite.Group()
player=Player()
group.add(player)
for i in range(8):
	m=Mob()
	group.add(m)
	mob.add(m)
#######################################


##############Game loop################
inplay=True
while inplay:
	#keep loop run at the right speed
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			inplay=False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				player.shoot()
	group.update()
	hitb=pygame.sprite.groupcollide(bullet,mob,True,True)
	for hit in hitb:
		m=Mob()
		group.add(m)
		mob.add(m)
	hits=pygame.sprite.spritecollide(player,mob,False)
	if hits:
		inplay=False
	screen.fill(black)
	group.draw(screen)
	pygame.display.flip()

pygame.quit()
	

#########################################



