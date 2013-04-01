import pygame 
from pygame.locals import *

import sgc
from sgc.locals import *

import pypalgame as pal

import engine

def pospos(pos):
    pos[0] *= 10
    pos[1] *= -10
    pos[0]+=250
    pos[1]+=490
    return pos

def posposn(pos):
    pos[0] *= 10
    pos[1] *= -10
    pos[0]+=250
    pos[1]+=250
    return pos

pygame.init()
window = sgc.surface.Screen((500,500))

pal.init()

drawable = pygame.sprite.Group()

terain =  pal.body.Terrain.create((0,0,0),60)
t = terain.obj
tsprite = pygame.sprite.Sprite(drawable)
tsprite.image = pygame.Surface((500,10))
tsprite.image.fill((255,0,0))
tsprite.rect = Rect(pospos([terain.get_position()[0],terain.get_position()[1],500,10]))

box = pal.body.StaticBox.create((0,10,0,1,1,1))
b = box.obj
bsprite = pygame.sprite.Sprite(drawable)
bsprite.image = pygame.Surface((10,10))
bsprite.image.fill((0,255,0))
bsprite.rect = Rect(pospos([box.get_position()[0],box.get_position()[1],10,10]))


sphere = pal.body.Sphere.create((5,10,0,1),mass=1)
s = sphere.obj
ssprite = pygame.sprite.Sprite(drawable)
ssprite.image = pygame.Surface((20,20))
pygame.draw.circle(ssprite.image,(0,0,255),(10,10),10)
ssprite.rect = Rect(pospos([sphere.get_position()[0],sphere.get_position()[1],20,20]))

#revolute = pal.link.Revolute.create(box,sphere,box.get_position(),(0,.5,.5))
#r = revolute.obj

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
                sphere.set_position((0,3,0))
    print "ready to update", terain.obj, box.obj, sphere.obj,\
          t == terain.obj,b == box.obj, s == sphere.obj#, r == revolute.obj
    pal.update(1./50.)
    print "updated"

    print "extracting s ",
    ssprite.rect.center = pospos([sphere.get_position()[0],sphere.get_position()[1]])
    print "t ",
    tsprite.rect.center = pospos([terain.get_position()[0],terain.get_position()[1]])
    print "b ",
    bsprite.rect.center = pospos([box.get_position()[0],box.get_position()[1]])
    print "extracted all"

    print "draw"
    window.fill((0,0,0))
    drawable.draw(window)
    pygame.display.flip()
    print "loop"

print sphere.get_size(),pal._pal.all_objects#,box.get_size()

pal.cleanup()




def draw_box(box):
    points = box.get_size()
    print points
    location = box.get_location()
    print location


