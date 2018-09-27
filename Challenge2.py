import pgzrun
from pygame.math import Vector2

class Character():
    def __init__(self, imagename):
        self.pos = Vector2(x, y)
        self.vel = Vector2(1, 0)    
        self.heading = Vector2()
        self.imagename = imagename

class Character():
    def __init__(self, imagename):
        self.pos = Vector2(x, y)
        self.vel = Vector2(1, 0)    
        self.heading = Vector2()
        self.imagename = imagename

    def draw(self):
        screen.blit(self.imagename, self.pos)


    def update(self):
        self.pos += self.vel
    
WIDTH = 1200
HEIGHT = 1200
x = 1
y = 1
mario = character('character1')
mario.vel = Vector2(3, 0 )


def draw():
    screen.clear()
    screen.fill("white")
    mario.draw(screen)

def update():
    mario.update()


pgzrun.go()
