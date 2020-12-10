import pygame

class Settings:
	def __init__(self):

		#Arena Settings
		self.screen_width = 360
		self.screen_height = 640
		self.title = "Flappy Bird"
		self.background = pygame.image.load("img/bg.PNG")


		#Bird Settings
		self.bird_image = pygame.image.load("img/bird.PNG")


		#Pipe Settings
		self.pipe_width = 50
		self.pipe_height = 200
		self.pipe_color = [27, 128, 1]

		#Stripe Settings
		self.stripe_width = 2.5
		self.stripe_height = 202.5
		self.stripe_color = [0, 0, 0]

		#Stripe 2 Settings
		self.stripe2_width = 60
		self.stripe2_height = 2.5
		self.stripe2_color = [0, 0, 0]

		#Stripe 3 Settings
		self.stripe3_width = 2.5
		self.stripe3_height = 30
		self.stripe3_color = [0, 0, 0]

		#Pipe Cover Settings
		self.pipecover_width = 60
		self.pipecover_height = 25
		self.pipecover_color = [27, 128, 1]

		#Platform Settings 
		self.platform_image = pygame.image.load('img/ground.PNG')
