from pygame.math import Vector2
import pgzero.actor as Actor
import steering_forces

windLocation = Vector2()

class Character():
    def __init__(self, imagename):
        self.pos = Vector2(0, 0)
        self.vel = Vector2(0, 0)    
        self.heading = Vector2()
        self.imagename = imagename
        self.mass = 1.0
        

    def draw(self, layer):
        layer.blit(self.imagename, self.pos)


    def update(self):
        ##Need to get windforce from wind pos and mario pos
        ##self.vel += wind
        currentwindforce = self.pos - windLocation
        accel = currentwindforce / self.mass
        print ('currentwindforce =', currentwindforce)
        self.vel += accel
        self.vel *= .898989899
        self.pos += self.vel 
        self.setwindLocation(Vector2(self.pos))
        print ("Mario's Vel =", self.vel)
        

    def setwindLocation(self, aPosition):
       global windLocation
       windLocation = aPosition




