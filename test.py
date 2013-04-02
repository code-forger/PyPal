import pygame 
from pygame.locals import *

import sgc
from sgc.locals import *

import pypalgame as pal

import engine

def draw_box(b):
    points = b.get_size()
    print points
    location = b.get_location()
    print location

def pospos(pos):
    pos[0] *= 10
    pos[1] *= -10
    pos[0]+=250
    pos[1]+=490
    return pos

pygame.init()
window = sgc.surface.Screen((500,500))

pal.init()

drawable = pygame.sprite.Group()

terain =  pal.body.Terrain.create((0,0,0),60)
tsprite = pygame.sprite.Sprite(drawable)
tsprite.image = pygame.Surface((500,10))
tsprite.image.fill((255,0,0))
tsprite.rect = Rect(pospos([terain.get_position()[0],terain.get_position()[1],500,10]))

box = pal.body.StaticBox.create((0,10,0,1,1,1))
bsprite = pygame.sprite.Sprite(drawable)
bsprite.image = pygame.Surface((10,10))
bsprite.image.fill((0,255,0))
bsprite.rect = Rect(pospos([box.get_position()[0],box.get_position()[1],10,10]))

box1 = pal.body.Box.create((5,10,0,1,1,1),mass=1)
ssprite = pygame.sprite.Sprite(drawable)
ssprite.image = pygame.Surface((10,10))
ssprite.image.fill((0,255,0))
ssprite.rect = Rect(pospos([box.get_position()[0],box.get_position()[1],10,10]))


#sphere = pal.body.Sphere.create((5,10,0,1),mass=1)
#ssprite = pygame.sprite.Sprite(drawable)
#ssprite.image = pygame.Surface((20,20))
#pygame.draw.circle(ssprite.image,(0,0,255),(10,10),10)
#ssprite.rect = Rect(pospos([sphere.get_position()[0],sphere.get_position()[1],20,20]))


revolute = pal.link.Revolute.create(box,box1,box.get_position(),(0,0,1))



motorbool = False
cl = pygame.time.Clock()
running = True
print "starting loop"
while running:
    time = cl.tick(50)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = not running
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                if not motorbool:
                    motor = pal.actuator.DCMotor.create(revolute,5,1,1)
                    motor.set_voltage(10)
                else:
                    motor.delete()
                motorbool = not motorbool
    
    pal.update(1./50.)
    if motorbool: motor.run()
    ssprite.rect.center = pospos([box1.get_position()[0],box1.get_position()[1]])
    tsprite.rect.center = pospos([terain.get_position()[0],terain.get_position()[1]])
    bsprite.rect.center = pospos([box.get_position()[0],box.get_position()[1]])

    window.fill((0,0,0))
    drawable.draw(window)
    pygame.display.flip()

box.delete()
box1.delete()
terain.delete()
revolute.delete()

print pal._pal.all_objects#,box.get_size()

pal.cleanup()






