#Basic pygame template
###########import scetion###############
import pygame 
import random
from os import path

########################################

img_dir=path.dirname(__file__)



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
		self.image=pygame.transform.scale(player_img,(50,38))
		self.image.set_colorkey(black)
		self.rect=self.image.get_rect()
		self.radius=22
		self.shield=100
		#pygame.draw.circle(self.image,red,self.rect.center,self.radius)
		self.rect.centerx=WIDTH/2
		self.rect.bottom=HEIGHT-10
		self.speedx=0
		self.shoot_delay=250
		self.last_shot=pygame.time.get_ticks()
	def update(self):
		self.speedx=0
		keystate=pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speedx=-5
		if keystate[pygame.K_RIGHT]:
			self.speedx=5
		if keystate[pygame.K_SPACE]:
			self.shoot()
		self.rect.x+=self.speedx
		if self.rect.right > WIDTH:
			self.rect.right=WIDTH
		if self.rect.left<0:
			self.rect.left=0
	def shoot(self):
		now=pygame.time.get_ticks()
		if now - self.last_shot >= self.shoot_delay:
			self.last_shot=now
			m=Bullet(self.rect.centerx,self.rect.top)
			group.add(m)
			bullet.add(m)

font_name=pygame.font.match_font('arial')
def score_draw(surf,text,size,x,y):
	font=pygame.font.Font(font_name,size)
	text_surface=font.render(text,True,white)
	text_rect=text_surface.get_rect()
	text_rect.midtop=(x,y)
	surf.blit(text_surface,text_rect)



		
class Mob(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.transform.scale(enemy_img,(40,28))
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
		self.image=laser_img
		self.image.set_colorkey(black)
		#self.image.fill(yellow)
		self.rect=self.image.get_rect()
		self.rect.bottom=y
		self.rect.centerx=x
		self.speedy=-8
	def update(self):
		self.rect.y+=self.speedy
		if self.rect.bottom <0:
			self.kill()

def draw_shield(surf,x,y,per):
#	if per < 0:
#per=0
	BAR_LENGTH=100
	BAR_HEIGHT=10
	fill=(per*BAR_LENGTH)/100
	outline_rect=pygame.Rect(x,y,BAR_LENGTH,BAR_HEIGHT)
	fill_rect=pygame.Rect(x,y,fill,BAR_HEIGHT)
	pygame.draw.rect(surf,green,fill_rect)
	pygame.draw.rect(surf,white,outline_rect,2)
###########################################################



################initialise game########
pygame.init()
pygame.mixer.init()

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("my first pygame")
clock=pygame.time.Clock()
background=pygame.image.load(path.join(img_dir,"back.jpeg")).convert()
background= pygame.transform.scale(background, (600, 600))
background_rect=background.get_rect()
player_img=pygame.image.load(path.join(img_dir,"fri.jpeg"))
enemy_img=pygame.image.load(path.join(img_dir,"enemy.jpeg"))
laser_img=pygame.image.load(path.join(img_dir,"laser.png"))
	
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
score=0
while inplay:
	#keep loop run at the right speed
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			inplay=False
#		if event.type == pygame.KEYDOWN:
#			if event.key == pygame.K_SPACE:
#				player.shoot()
	group.update()
	hitb=pygame.sprite.groupcollide(bullet,mob,True,True)
	for hit in hitb:
		score+=100
		m=Mob()
		group.add(m)
		mob.add(m)
	hits=pygame.sprite.spritecollide(player,mob,True)
	if hits:
		m=Mob()
		group.add(m)
		mob.add(m)
		player.shield-=20
		if player.shield<=0:
			inplay=False
	
	screen.fill(black)
	screen.blit(background,(0,0))
	group.draw(screen)
	score_draw(screen,str(score),18,WIDTH/2,10)
#score_draw(screen,str(player.shield),18,WIDTH/2,30)
	draw_shield(screen,5,5,player.shield)
	pygame.display.flip()

pygame.quit()
	

#########################################



