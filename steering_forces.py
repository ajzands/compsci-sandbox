from pygame.math import Vector2

maxwind = 50

def wind(pointa, pointb):
    global maxwind
    wind = pointb - pointa
    if wind.length() > maxwind:
        wind.scale_to_length(maxwind)
    return wind
