import pygame
import pypal as pal

pal.init()

terain =  pal.body.Terrain((0,0,0),60)


box = pal.body.Box((0,10,0,1,1,1), mass=10)

#box1 = pal.body.Box((-10,5,0,1,1,1),mass=10)

#box2 = pal.body.StaticBox((15,10,0,1,1,1))

#box3 = pal.body.Box((-10,10,0,1,1,1),mass=10)

#box4 = pal.body.Compound((10,10,10))

sphere = pal.body.Sphere((5,10,0,1),mass=1)

cl = pygame.time.Clock()
while True:
    time = cl.tick(50)
    
    pal.update(1./50.)
    print box.apply_force((1,1,1))
    print "sphere", sphere.apply_force((1,1,1))
pal.cleanup()
