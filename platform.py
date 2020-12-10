import pygame

class Platform:

	def __init__(self, Arena_Game):
		#Init Screen For Platform
		self.screen = Arena_Game.screen
		self.screen_rect = Arena_Game.screen.get_rect()

		#Init Platform Image
		self.game_settings = Arena_Game.game_settings
		self.image = self.game_settings.platform_image
		self.image_rect = self.image.get_rect()

		#Init Platform Position
		self.image_rect.midbottom = self.screen_rect.midbottom

	def show_platform(self):
		#Show Platform using Blit from Pygame
		self.screen.blit(self.image, self.image_rect)