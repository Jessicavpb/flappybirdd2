import pygame


from settings import Settings
from bird import Bird

from pipe import Pipe, Pipecover 
from stripe import Stripe, Stripee,Stripe2, Stripee2, Stripe3, Stripee3 
from platform import Platform 

class Arena_Game:

	################################
	#ARENA / SCREEN
	################################
	def __init__(self):
		pygame.init()
		self.game_settings = Settings()

		self.screen = pygame.display.set_mode([self.game_settings.screen_width, self.game_settings.screen_height])
		self.title = pygame.display.set_caption(self.game_settings.title)
		self.running = True

		############
		#OBJ IN GAME
		############
		#SINGLE OBJ
		self.game_bird = Bird(self)
		self.game_platform = Platform(self)

		#GROUP OBJ
		self.game_pipes = pygame.sprite.Group()
		self.create_pipes()

		self.game_pipescover = pygame.sprite.Group()
		self.create_pipescover()

		self.game_stripes = pygame.sprite.Group()
		self.create_stripes()

		self.game_stripees = pygame.sprite.Group()
		self.create_stripees()

		self.game_stripes2 = pygame.sprite.Group()
		self.create_stripes2()

		self.game_stripees2 = pygame.sprite.Group()
		self.create_stripees2()

		self.game_stripes3 = pygame.sprite.Group()
		self.create_stripes3()

		self.game_stripees3 = pygame.sprite.Group()
		self.create_stripees3()

	def update_bg_screen(self):
		self.screen.blit(self.game_settings.background, [0,0])

	###############################
	#BIRD
	###############################
	def update_bird(self):
		self.game_bird.show_bird()


	###############################
	#PIPE
	###############################
	def update_pipes(self):
		for pipe in self.game_pipes.sprites():
			pipe.show_pipe()

	def create_pipes(self):
		pipe_top = Pipe(self)
		pipe_bottom = Pipe(self)

		self.game_pipes.add(pipe_top)
		self.game_pipes.add(pipe_bottom)

	###############################
	#Pipe Cover
	###############################
	def update_pipescover(self):
		for pipecover in self.game_pipescover.sprites():
			pipecover.show_pipecover()

	def create_pipescover(self):
		pipecover_top = Pipecover(self)
		pipecover_bottom = Pipecover(self)

		self.game_pipescover.add(pipecover_top)
		self.game_pipescover.add(pipecover_bottom)

	def update_stripes(self):
		for stripe in self.game_stripes.sprites():
			stripe.show_stripe()

	def create_stripes(self):
		stripe_top = Stripe(self)
		stripe_bottom = Stripe(self)

		self.game_stripes.add(stripe_top)
		self.game_stripes.add(stripe_bottom)

	def update_stripees(self):
		for stripee in self.game_stripees.sprites():
			stripee.show_stripee()

	def create_stripees(self):
		stripee_top = Stripee(self)
		stripee_bottom = Stripee(self)

		self.game_stripees.add(stripee_top)
		self.game_stripees.add(stripee_bottom)

	def update_stripes2(self):
		for stripe2 in self.game_stripes2.sprites():
			stripe2.show_stripe2()

	def create_stripes2(self):
		stripe2_top = Stripe2(self)
		stripe2_bottom = Stripe2(self)

		self.game_stripes2.add(stripe2_top)
		self.game_stripes2.add(stripe2_bottom)

	def update_stripees2(self):
		for stripee2 in self.game_stripees2.sprites():
			stripee2.show_stripee2()

	def create_stripees2(self):
		stripee2_top = Stripee2(self)
		stripee2_bottom = Stripee2(self)

		self.game_stripees2.add(stripee2_top)
		self.game_stripees2.add(stripee2_bottom)

	def update_stripes3(self):
		for stripe3 in self.game_stripes3.sprites():
			stripe3.show_stripe3()

	def create_stripes3(self):
		stripe3_top = Stripe3(self)
		stripe3_bottom = Stripe3(self)

		self.game_stripes3.add(stripe3_top)
		self.game_stripes3.add(stripe3_bottom)

	def update_stripees3(self):
		for stripee3 in self.game_stripees3.sprites():
			stripee3.show_stripee3()

	def create_stripees3(self):
		stripee3_top = Stripee3(self)
		stripee3_bottom = Stripee3(self)

		self.game_stripees3.add(stripee3_top)
		self.game_stripees3.add(stripee3_bottom)

	###############################
	#Platform
	###############################
	def update_platform(self):
		self.game_platform.show_platform()



	################################
	#RUN GAME
	################################
	def rg_check_events(self):
		events = pygame.event.get()
		#print(events)
		for event in events:
			if event.type == pygame.QUIT:
				self.running = False

	def rg_update_screen(self):
		self.update_bg_screen() #Update BG
		self.update_bird() # Update Bird Postision
		self.update_pipes() #Update Pipes
		self.update_platform() #update platform
		self.update_pipescover()
		self.update_stripes()
		self.update_stripees()
		self.update_stripes2()
		self.update_stripees2()
		self.update_stripes3()
		self.update_stripees3()
		pygame.display.flip() #Update Frame Every Second


	def run_game(self):
		while self.running:
			self.rg_check_events()
			self.rg_update_screen()

flappy_bird_game = Arena_Game()
flappy_bird_game.run_game()