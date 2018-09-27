import pgzrun
from pygame.math import Vector2
import character
import steering_forces

didClick = False
mario = character.Character('character1')
mario.pos = (600, 600)
clickPos = (0, 0)
WIDTH = 1200
HEIGHT = 1200
midscreen = Vector2(0.5 * WIDTH, 0.5 * HEIGHT)

def on_mouse_down(pos):
    global didClick
    global clickPos
    didClick = True
    clickPos = pos


def draw():
    screen.fill('white')
    mario.draw(screen) 

def update():
    global didClick
    if didClick:
        didClick = False
        ##Compute wind
        wind = steering_forces.wind(midscreen, clickPos)
        ##set wind.pos = clickPos
        print ('wind =', wind)
        ##set wind
        print ('You Clicked', clickPos)
        mario.setwind(wind)
        
    mario.update()
    print ("Mario's Position =", mario.pos)
        

pgzrun.go()
