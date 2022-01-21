import pygame.font

class Button:

	def __init__(self, ai_game, msg):
		# Initializing button attributes

		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		# Setting dimensions and properties for the button

		self.width, self.height = 200, 50
		self.button_color = (103, 103, 103)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		# Building the button's rect object and centering it.

		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		# Rendering the button's text to the screen

		self._prep_msg(msg)

	def _prep_msg(self, msg):
		# Turning the message into a rendered image and center the text on the button

		self.msg_image = self.font.render(msg, True, self.text_color,
			self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		# Drawing the blank button then the message

		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)