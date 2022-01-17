class Settings:
	# A class to store all the settings for alien invasion.

	def __init__(self):
		# Initializing the game's settings 

		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)
		self.alien_speed = 1.0
		self.fleet_drop_speed = 10
		self.fleet_direction = 1

		# Ship settings 
		self.ship_speed = 1.5

		# Bullet Settings 
		self.bullet_speed = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (255,127,0)
		self.bullets_allowed = 3