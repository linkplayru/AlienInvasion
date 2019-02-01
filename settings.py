class Settings():
	
	def __init__(self):
		#screen
		self.screen_caption = 'Alien Invasion'
		self.screen_width = 640
		self.screen_height = 640
		self.bg_color = (230, 230, 230)
		
		#ship
		self.ship_limit = 3
		
		#bullet
		self.bullet_width = 3000
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3

		#aliens
		self.fleet_drop_speed = 10
		#fleet_direction = 1 вправо, -1 - влево
		self.fleet_direction = 1
		
		#game
		self.speedup_scale = 1.1
		
		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1
		self.alien_points = 50
		
	def increase_speed(self):
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
