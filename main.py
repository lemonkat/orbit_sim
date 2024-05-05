import time

from universe import Universe
from planet import Planet

u = Universe(50000, 1000, 0.7)
u.add_planet(300, 0, 0, 100, 1, 100, "#0f0")
u.add_planet(-100, 0, 0, 0, 4, 200, "#f00")

for i in range(10000):
    u.paint()
    for j in range(10):
        u.step(0.03)
    time.sleep(0.025)
