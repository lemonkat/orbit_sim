from tkinter import Tk, Canvas

from planet import Planet


class Universe:
    def __init__(self, grav, size, scale):
        self.grav = grav
        self.size = size
        self.planets = []
        self.scale = scale
        self.canvas = Canvas(Tk(), height=size * scale, width=size * scale, bg="#fff")

    def add_planet(self, x, y, xvel, yvel, mass, size, color):
        self.planets.append(Planet(x, y, xvel, yvel, mass, size, color))

    def lock(self):
        shift_x = 0
        shift_y = 0
        shift_xvel = 0
        shift_yvel = 0
        total_mass = 0

        for p in self.planets:
            shift_x -= p.x * p.mass
            shift_y -= p.y * p.mass
            shift_xvel -= p.xvel * p.mass
            shift_yvel -= p.yvel * p.mass
            total_mass += p.mass

        shift_x *= 1 / total_mass
        shift_y *= 1 / total_mass
        shift_xvel *= 1 / total_mass
        shift_yvel *= 1 / total_mass
        for p in self.planets:
            p.x += shift_x
            p.y += shift_y
            p.xvel += shift_xvel
            p.yvel += shift_yvel

    def step(self, t):
        for p in self.planets:
            p.compute_vel_change(self.planets, self.grav)
        for p in self.planets:
            p.move(t)

        self.lock()

    def paint(self):
        self.canvas.delete("all")
        for p in self.planets:
            p.paint(self.canvas, self.size, self.scale)
        self.canvas.pack()
        self.canvas.update()
