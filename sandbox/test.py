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

terain =  pal.body.Terrain((0,0,0),60)
tsprite = pygame.sprite.Sprite(drawable)
tsprite.image = pygame.Surface((500,10))
tsprite.image.fill((255,0,0))
tsprite.rect = Rect(pospos([terain.get_position()[0],terain.get_position()[1],500,10]))
terain1 =  pal.body.Terrain((10,-10,0),60)

box = pal.body.StaticBox((0,10,0,1,1,1))
bsprite = pygame.sprite.Sprite(drawable)
bsprite.image = pygame.Surface((10,10))
bsprite.image.fill((0,255,0))
bsprite.rect = Rect(pospos([box.get_position()[0],box.get_position()[1],10,10]))

box1 = pal.body.Box((-10,5,0,1,1,1),mass=10)
b1sprite = pygame.sprite.Sprite(drawable)
b1sprite.image = pygame.Surface((10,10))
b1sprite.image.fill((0,255,0))
b1sprite.rect = Rect(pospos([box.get_position()[0],box.get_position()[1],10,10]))

box3 = pal.body.Box((-10,10,0,1,1,1),mass=10)
b3sprite = pygame.sprite.Sprite(drawable)
b3sprite.image = pygame.Surface((10,10))
b3sprite.image.fill((0,255,0))
b3sprite.rect = Rect(pospos([box.get_position()[0],box.get_position()[1],10,10]))

box4 = pal.body.Compound((10,10,10))
b4sprite = pygame.sprite.Sprite(drawable)
b4sprite.image = pygame.Surface((10,10))
b4sprite.image.fill((0,255,0))
b4sprite.rect = Rect(pospos([box.get_position()[0],box.get_position()[1],10,10]))


box2 = pal.body.StaticBox((15,10,0,1,1,1))
b2sprite = pygame.sprite.Sprite(drawable)
b2sprite.image = pygame.Surface((10,10))
b2sprite.image.fill((0,255,0))
b2sprite.rect = Rect(pospos([box.get_position()[0],box.get_position()[1],10,10]))


sphere = pal.body.Sphere((5,10,0,1),mass=1)
ssprite = pygame.sprite.Sprite(drawable)
ssprite.image = pygame.Surface((20,20))
pygame.draw.circle(ssprite.image,(0,0,255),(10,10),10)
ssprite.rect = Rect(pospos([sphere.get_position()[0],sphere.get_position()[1],20,20]))

prismatic = pal.link.Prismatic(box,box3,box.get_position(),(1,0,0),False)
prismatic.set_limits(3,20)
#revolute = pal.link.Revolute(box3,box1,box3.get_position(),(0,0,1),False)

rigid = pal.link.Rigid(box2,sphere,False)

box1.notify_collision(True)

box2.set_group(2)
box1.set_group(1)
terain.set_group(1)

motorbool = False
cl = pygame.time.Clock()
running = True
while running:
    time = cl.tick(50)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = not running
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                pass
            elif event.key == K_RIGHT:
                box1.set_active(True)
                box1.apply_impulse((75,0,0))
            elif event.key == K_LEFT:
                box1.set_active(True)
                box1.apply_impulse((-75,0,0))
            elif event.key == K_UP:
                box1.set_active(True)
                box1.apply_impulse((0,75,0))
            elif event.key == K_DOWN:
                box1.set_active(True)
                box1.apply_impulse((0,-75,0))
    
    pal.update(1./50.)
    if motorbool: motor.run()

    bsprite.rect.center = pospos([box.get_position()[0],box.get_position()[1]])
    b1sprite.rect.center = pospos([box1.get_position()[0],box1.get_position()[1]])
    b2sprite.rect.center = pospos([box2.get_position()[0],box2.get_position()[1]])
    b3sprite.rect.center = pospos([box3.get_position()[0],box3.get_position()[1]])
    b4sprite.rect.center = pospos([box4.get_position()[0],box4.get_position()[1]])
    tsprite.rect.center = pospos([terain.get_position()[0],terain.get_position()[1]])
    ssprite.rect.center = pospos([sphere.get_position()[0],sphere.get_position()[1]])

    window.fill((0,0,0))
    drawable.draw(window)
    pygame.display.flip()
    #print "time:%2.2f pos:%2.2f %2.2f %2.2f " % (pal.get_time(), 
    #                                             box1.get_position()[0], 
    #                                             box1.get_position()[1], 
    #                                             box1.get_position()[2])
    print box1.set_position((3,3,3))

print pal._pal.all_objects, pal._pal.sensor_objects
box.delete()
box1.delete()
box2.delete()
box3.delete()
box4.delete()
sphere.delete()
terain.delete()
#revolute.delete()
prismatic.delete()
rigid.delete()
print pal._pal.all_objects, pal._pal.sensor_objects

pal.cleanup()
