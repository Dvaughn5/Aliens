import pygame 
from pygame.sprite import Sprite

class Ship(Sprite):
	
	def __init__(self, ai_game):
		# A class to manage the ship

		super().__init__()

		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		# Starting each ship at the middle bottom of the screen
		self.rect.midbottom = self.screen_rect.midbottom

		# Storing a decimal value for the ship's horizontal positon
		self.x = float(self.rect.x)

		# Movement Flags
		self.moving_right = False
		self.moving_left = False

	def update(self):
		# update the ship's position based on the movement flag 
		# Update the ship's x value rather than the rect.
		
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed

		# Update the rect object from self.x
		self.rect.x = self.x

	def blitme(self):

		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		# Center the ship on the screen

		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)