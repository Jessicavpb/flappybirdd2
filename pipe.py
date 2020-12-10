import pygame
from pygame.sprite import Sprite


class Pipe(Sprite):

	def __init__(self, Arena_Game):
		super().__init__()

		self.screen = Arena_Game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = Arena_Game.game_settings

		self.pipe_image = pygame.Rect(0, 0, self.settings.pipe_width, self.settings.pipe_height)
		self.pipe_image.topright = self.screen_rect.topright

		self.pipe_image.x -= 50


	def show_pipe(self):
		pygame.draw.rect(self.screen, self.settings.pipe_color, self.pipe_image)
		pygame.draw.rect(self.screen, self.settings.pipe_color, self.pipe_image)

class Pipecover(Sprite):

	def __init__(self, Arena_Game):
		super().__init__()

		self.screen = Arena_Game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = Arena_Game.game_settings

		self.pipecover_image = pygame.Rect(0, 0, self.settings.pipecover_width, self.settings.pipecover_height)
		self.pipecover_image.topright = self.screen_rect.topright

		self.pipecover_image.x -= 45
		self.pipecover_image.y += 202.5

	def show_pipecover(self):
		pygame.draw.rect(self.screen, self.settings.pipecover_color, self.pipecover_image)