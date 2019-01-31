class Settings():
	
	def __init__(self):
		#screen
		self.screen_caption = 'Alien Invasion'
		self.screen_width = 640
		self.screen_height = 640
		self.bg_color = (230, 230, 230)
		
		#ship
		self.ship_speed_factor = 1.5
		
		#bullet
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3

		#aliens
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		#fleet_direction = 1 вправо, -1 - влево
		self.fleet_direction = 1
