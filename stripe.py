import pygame
from pygame.sprite import Sprite

class Stripe(Sprite): #vertikal kiri panjang

	def __init__(self, Arena_Game):
		super().__init__()

		self.screen = Arena_Game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = Arena_Game.game_settings

		self.stripe_image = pygame.Rect(0, 0, self.settings.stripe_width, self.settings.stripe_height)
		self.stripe_image.topright = self.screen_rect.topright

		self.stripe_image.x -= 100

	def show_stripe(self):
		pygame.draw.rect(self.screen, self.settings.stripe_color, self.stripe_image)

class Stripee(Sprite): #vertikal kanan panjang

	def __init__(self, Arena_Game):
		super().__init__()

		self.screen = Arena_Game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = Arena_Game.game_settings

		self.stripee_image = pygame.Rect(0, 0, self.settings.stripe_width, self.settings.stripe_height)
		self.stripee_image.topright = self.screen_rect.topright

		self.stripee_image.x -= 47.5

	def show_stripee(self):
		pygame.draw.rect(self.screen, self.settings.stripe_color, self.stripee_image)

class Stripe2(Sprite): #horizontal atas

	def __init__(self, Arena_Game):
		super().__init__()

		self.screen = Arena_Game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = Arena_Game.game_settings

		self.stripe2_image = pygame.Rect(0, 0, self.settings.stripe2_width, self.settings.stripe2_height)
		self.stripe2_image.topright = self.screen_rect.topright

		self.stripe2_image.x -= 45
		self.stripe2_image.y += 200

	def show_stripe2(self):
		pygame.draw.rect(self.screen, self.settings.stripe2_color, self.stripe2_image)

class Stripee2(Sprite): #horizontal bawah

	def __init__(self, Arena_Game):
		super().__init__()

		self.screen = Arena_Game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = Arena_Game.game_settings

		self.stripee2_image = pygame.Rect(0, 0, self.settings.stripe2_width, self.settings.stripe2_height)
		self.stripee2_image.topright = self.screen_rect.topright

		self.stripee2_image.x -= 45
		self.stripee2_image.y += 227.5

	def show_stripee2(self):
		pygame.draw.rect(self.screen, self.settings.stripe2_color, self.stripee2_image)

class Stripe3(Sprite): #vertikal kiri pendek

	def __init__(self, Arena_Game):
		super().__init__()

		self.screen = Arena_Game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = Arena_Game.game_settings

		self.stripe3_image = pygame.Rect(0, 0, self.settings.stripe3_width, self.settings.stripe3_height)
		self.stripe3_image.topright = self.screen_rect.topright

		self.stripe3_image.x -= 105
		self.stripe3_image.y += 200

	def show_stripe3(self):
		pygame.draw.rect(self.screen, self.settings.stripe3_color, self.stripe3_image)

class Stripee3(Sprite): #vertikal kanan pendek

	def __init__(self, Arena_Game):
		super().__init__()

		self.screen = Arena_Game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = Arena_Game.game_settings

		self.stripee3_image = pygame.Rect(0, 0, self.settings.stripe3_width, self.settings.stripe3_height)
		self.stripee3_image.topright = self.screen_rect.topright

		self.stripee3_image.x -= 45
		self.stripee3_image.y +=200

	def show_stripee3(self):
		pygame.draw.rect(self.screen, self.settings.stripe3_color, self.stripee3_image)