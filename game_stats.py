class GameStats:
	# Tracking statistics for the Alien Invasion game 

	def __init__(self, ai_game):
		# Initialize stats

		self.settings = ai_game.settings
		self.reset_stats()

		# Starting the active state of the game 
		self.game_active = True

	def reset_stats(self):
		# Initialize stats that can change during the game 

		self.ships_left = self.settings.ship_limit