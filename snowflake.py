import random
import pygame

def init(width, height, surface, images):
    global d_width, d_height, d_surface, d_images
    d_width = width
    d_height = height
    d_surface = surface
    d_images = images

def restric(val, add, minval, maxval):
    newval = val + add
    if newval > maxval:
        return maxval
    elif newval < minval:
        return minval
    else:
        return newval

class Snowflake(object):
    """Define the properties of the flakes"""
    def __init__(self):
        self.posx = random.randint(1, d_width)
        self.posy = random.randint(-300, -100)
        self.velx = 0
        self.vely = 0
        self.accx = 0
        self.accy = 0
        self.image = None
        #self.angle = 0
        self.r = abs(int(random.gauss(0, 10))) + 3
        self.getImage(random.choice(d_images))

    def applyForce(self, forcex, forcey):
        fx = forcex * self.r
        fy = forcey * self.r
        self.accx += fx
        self.accy += fy

    def update(self):
        self.velx += self.accx
        #self.vely += self.accy
        self.vely = restric(self.vely, self.accy, 5, self.r * 0.3)
        self.posx += self.velx
        self.posy += self.vely
        self.accx *= 0
        self.accy *= 0
        #self.angle += 1
        self.recycle()

    def recycle(self):
        if self.posy > d_height + self.r:
            self.posx = random.randint(1, d_width)
            self.posy = random.randint(-300, -100)
            #self.angle = 0
            self.r = abs(int(random.gauss(0, 10))) + 3
            self.getImage(random.choice(d_images))
            
    def getImage(self, image):
        self.image = pygame.transform.smoothscale(image, (self.r * 2, self.r * 2))

    def draw(self):
        #pygame.draw.circle(d_surface, (255, 255, 255), (int(self.posx), int(self.posy)), self.r)
        #rotImage = pygame.transform.rotate(self.image, self.angle)
        d_surface.blit(self.image, ((int(self.posx), int(self.posy))))