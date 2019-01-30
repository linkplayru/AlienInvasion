import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	#init
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption(ai_settings.screen_caption)
	
	ship = Ship(screen)
	
	#main cycle
	while True:
		gf.check_events()
		gf.update_screen(ai_settings, screen, ship)
		
run_game()
