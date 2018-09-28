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
        self.maxspeed = 50
        self.maxwindSpeed = 50
        

    def draw(self, layer):
        layer.blit(self.imagename, self.pos)


    def update(self):
        ##Need to get windforce from wind pos and mario pos
        ##self.vel += wind
        currentwindforce = self.pos - windLocation
        if currentwindforce.length() > self.maxwindSpeed:
            currentwindforce.scale_to_length(0)
        accel = currentwindforce / self.mass
        print ('currentwindforce =', currentwindforce)
        self.vel += accel
        self.vel *= .898989899
        self.pos += self.vel 
        self.setwindLocation(Vector2(self.pos))
        print ("Mario's Vel =", self.vel)
        if self.vel.length() > self.maxspeed:
            self.vel.scale_to_length(maxspeed)
        

    def setwindLocation(self, aPosition):
       global windLocation
       windLocation = aPosition




