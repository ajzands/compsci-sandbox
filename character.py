from pygame.math import Vector2
import pgzero.actor as Actor
import steering_forces

wind = Vector2()

class Character():
    def __init__(self, imagename):
        self.pos = Vector2(0, 0)
        self.vel = Vector2(0, 0)    
        self.heading = Vector2()
        self.imagename = imagename
        

    def draw(self, layer):
        layer.blit(self.imagename, self.pos)


    def update(self):
        self.vel += wind
        self.vel *= .898989899
        self.pos += self.vel 
        self.setwind(Vector2())       
        

    def setwind(self, force):
       global wind
       wind = force




