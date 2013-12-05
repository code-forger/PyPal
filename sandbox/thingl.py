import pygame 
from pygame.locals import *

from OpenGL.GL import (
    GL_DEPTH_TEST, glEnable, glTranslate)
from OpenGL.GLU import gluPerspective, gluLookAt

import glhelp as glh
import random
import pypal as pal

pal.init()

pygame.init()
pygame.display.set_mode(
    (1024, 768), pygame.locals.OPENGL | pygame.locals.DOUBLEBUF)

glEnable(GL_DEPTH_TEST)
gluPerspective(60.0, 640.0 / 480.0, 0.5, 1000.0)
glTranslate(-0, -5, -20)

objects = []
## HEAD END ##





pal.init()

box2 = pal.body.StaticBox((0,-5,0,50,1,50))
objects.append(glh.Box(box2, (255,255, 0)))

body = pal.body.GenericBody((0,0,0))



body.dynamics_type = "dynamic"
body.mass = 10
body.gravity_enabled = True #XXX
body.collision_response = True

boxgeom = pal.geometry.Box((0,0,0,2,2,2))
body.connect_geometry(boxgeom)
objects.append(glh.Generic(body, (0,0,255)))


box = pal.body.Box((0,20,0,2,2,2), mass=10)
objects.append(glh.Box(box, (0,255,0)))



## TAIL START ##
running = True
gluLookAt(10,10,10,0,0,0,0,1,0)
while running:
    pal.update(1./50.)
    #player.set_position([0,2,0])
    ## DO THINGS PER LOOP ##
    #print body.get_geometries()[0].get_location()
    
    glh.render(objects)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = not running
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                pass
            elif event.key == K_RIGHT:
                control.set_active(True)
                control.apply_angular_impulse((-1,0,0))
            elif event.key == K_LEFT:
                control.set_active(True)
                control.apply_angular_impulse((1,0,0))
            elif event.key == K_UP:
                control.set_active(True)
                control.apply_angular_impulse((0,1,0))
            elif event.key == K_DOWN:
                control.set_active(True)
                control.apply_angular_impulse((0,-1,0))

            elif event.key == K_d:
                control.set_active(True)
                control.apply_impulse((75,0,0))
            elif event.key == K_a:
                control.set_active(True)
                control.apply_impulse((-75,0,0))
            elif event.key == K_s:
                control.set_active(True)
                control.apply_impulse((0,0,75))
            elif event.key == K_w:
                control.set_active(True)
                control.apply_impulse((0,0,-75))


pal.cleanup()
