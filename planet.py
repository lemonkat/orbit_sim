import math
class Planet:
	def __init__(self, x:float, y:float, xvel:float, yvel:float, mass:float, size:float, color:str, universe):
		self.x = x
		self.y = y
		self.xvel = xvel
		self.yvel = yvel
		self.mass = mass
		self.size = size
		self.color = color
		self.universe = universe

	def compute_vel_change(self, t):
		for p in self.universe.planets:
			if (p.x != self.x or p.y != self.y):
				dist = math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)
				pull = self.universe.grav * (self.mass * p.mass) / ((dist ** 2) * self.mass)

				self.xvel += pull * (p.x - self.x) / dist
				self.yvel += pull * (p.y - self.y) / dist
				

	def move(self, t):
		self.x += self.xvel * t
		self.y += self.yvel * t

	def paint(self):
		self.universe.canvas.create_oval(
			(self.x - self.size / 2 + self.universe.size / 2) * self.universe.scale,
			(self.y - self.size / 2 + self.universe.size / 2) * self.universe.scale,
			(self.x + self.size / 2 + self.universe.size / 2) * self.universe.scale,
			(self.y + self.size / 2 + self.universe.size / 2) * self.universe.scale,
			fill=self.color
			)
