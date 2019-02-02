import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	
	def __init__(self, ai_settings, screen):
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		self.image1 = pygame.image.load('images/alien.png')
		self.image2 = pygame.image.load('images/alien2.png')
		self.image = self.image1
		
		self.rect = self.image.get_rect()
		
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		self.x = float(self.rect.x)
		
		self.count = 0
		
	def check_edges(self):
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True	
		
	def update(self):
		self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
		self.rect.x = self.x
		
		self.count += 1
		if self.count >= 100:
			self.count = 0
		if self.count >= 50:
			self.image = self.image2
		else:
			self.image = self.image1
			
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)
