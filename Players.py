# Player requiremnets

# 1. Show an image of player
# 2. move the player
# 3. Constrain player
# 4. Shoot laser + recharge


import pygame
 
from Try_laser import Laser

class Players(pygame.sprite.Sprite):
	def __init__(self,pos,constraint,speed):
		super().__init__()
		self.image = pygame.image.load('../Images/player1.png').convert_alpha()
		# C:\Users\Shanpoo\Desktop\3rd Semester\CPDP\Games\Test-Pooja
		self.rect = self.image.get_rect(midbottom = pos)
		self.speed = speed
		self.max_x_constraint = constraint
		self.ready = True
		self.laser_time = 0
		self.laser_cooldown = 500

		self.lasers = pygame.sprite.Group()

		self.laser_sound = pygame.mixer.Sound('../Audio/laser.wav')
		# C:\Users\Shanpoo\Desktop\3rd Semester\CPDP\Games\Test-Pooja\Space-invaders-main\audio
		self.laser_sound.set_volume(0.5)

	def get_input_and_move(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_RIGHT]:
			self.rect.x += self.speed
		elif keys[pygame.K_LEFT]:
			self.rect.x -= self.speed

		if keys[pygame.K_SPACE] and self.ready:
			self.shoot_laser()
			self.ready = False
			self.laser_time = pygame.time.get_ticks()
			self.laser_sound.play()

	def check_for_recharge(self):
		if not self.ready:
			current_time = pygame.time.get_ticks()
			if current_time - self.laser_time >= self.laser_cooldown:
				self.ready = True

	def keep_player_within_screen(self):
		if self.rect.left <= 0:
			self.rect.left = 0
		if self.rect.right >= self.max_x_constraint:
			self.rect.right = self.max_x_constraint

	def shoot_laser(self):
		self.lasers.add(Laser(self.rect.center,-8,self.rect.bottom))

	def update(self):
		self.get_input()
		self.constraint()
		self.recharge()
		self.lasers.update()
