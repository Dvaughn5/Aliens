import sys
import pygame 
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
	# Class to manage the game assets and behavior 

	def __init__(self):
		# Initializing the game, and setting the screen parameters.
		
		pygame.init() 
		self.settings = Settings()
		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		
		pygame.display.set_caption("Alien Invasion") 

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		self._create_fleet()

		self.bg_color = (211,211,211)

	def run_game(self):
		# Starting the main loop for the game.

		while True:
			# Starting the main loop for the game.
			self._check_events()
			self.ship.update()
			self._update_bullets()
			self._update_screen()
			
	def _check_events(self):
		# Respond to key presses and mouse events 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		if event.key == pygame.K_RIGHT:
			# Move the ship to the right 
			self.ship.moving_right = True 
		elif event.key == pygame.K_LEFT:
			# Moving the ship to the left.
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
			
	def _check_keyup_events(self,event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _fire_bullet(self):
		# Create a new bullet and add it to the bullets group
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _create_fleet(self):
		# Creating the first flet of aliens
		alien = Alien(self)
		alien_width = alien.rect.width
		available_space_x = self.settings.screen_width - (2 * alien_width)
		number_aliens_x = available_space_x // (2 * alien_width)

		# Create the first row of aliens
		for alien_num in range(number_aliens_x):
			# Create an alien and place it in the row 
			alien = Alien(self)
			alien.x = alien_width + 2 * alien_width * alien_num
			alien.rect.x = alien.x 
			self.aliens.add(alien)

	def _update_bullets(self):
		# Update the position of bullets and get rid of old bullets 
		self.bullets.update()

		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)

	def _update_screen(self):
		# Redrawing the screen and ship during each pass through the loop
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.aliens.draw(self.screen)

		pygame.display.flip() # Makes the screen visible 

if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()