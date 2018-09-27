import pgzrun
from pygame.math import Vector2

WIDTH = 1200
HEIGHT = 1200
x = 1
y = 1
pos = Vector2(x, y)
vel = Vector2(1, 0)
box = Rect(pos, (250, 150))


def draw():
    screen.fill("steelblue")
    screen.draw.filled_rect(box, "cyan")

def update():
    global box, vel, pos
    pos += vel
    box.left = pos.x
    box.top = pos.y
    
    
pgzrun.go()
