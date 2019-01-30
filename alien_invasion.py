import sys
import pygame

from settings import Settings
from ship import Ship

def run_game():
	#init
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption(ai_settings.screen_caption)
	
	ship = Ship(screen)
	
	#main cycle
	while True:
		#events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				
		screen.fill(ai_settings.bg_color)
		ship.blitme()
		
		pygame.display.flip()
		
run_game()
