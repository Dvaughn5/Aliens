class Settings:
	# A class to store all the settings for alien invasion.

	def __init__(self):
		# Initializing the game's settings 

		# Screen Settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)

		# Ship settings 
		self.ship_limit = 3

		# Bullet Settings 
		self.bullet_height = 15
		self.bullet_color = (227,207,87)

		# Alien Settings
		self.fleet_drop_speed = 10

		# How quickly the game speeds up
		self.speedup_scale = 1.1

		# How quickly alien values increase
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		# Initializing settings that will change throughout the game

		self.bullet_width = 6
		self.ship_speed = 1.5
		self.bullet_speed = 1.5
		self.bullets_allowed = 3
		self.alien_speed = 1

		# Fleet direction
		self.fleet_direction = 1

		# Scoring
		self.alien_points = 50

	def increase_speed(self):
		# Increase the speed and point settings

		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		if self.bullet_width < 1000:
			self.bullet_width *= 2
		self.bullets_allowed += 1

		self.alien_points = int(self.alien_points * self.score_scale)