import pygame 
from pygame.locals import *

from OpenGL.GL import (
    GL_DEPTH_TEST, glEnable, glTranslate)
from OpenGL.GLU import gluPerspective, gluLookAt

import glhelp as glh

import pypal as pal

pygame.init()
pygame.display.set_mode(
    (1024, 768), pygame.locals.OPENGL | pygame.locals.DOUBLEBUF)

glEnable(GL_DEPTH_TEST)
gluPerspective(60.0, 640.0 / 480.0, 0.5, 1000.0)
glTranslate(0, -15, -60)

objects = []

terrain =  pal.body.StaticBox((0,0,0,60,1,60))
sbox = pal.body.StaticBox((0,10,0,1.,1.,1.))
sbox1 = pal.body.StaticBox((10,10,0,1.,1.,1.))
box1 = pal.body.Box((-10,5,0,1,1,1),mass=10)
ssphere = pal.body.StaticSphere((-10,10,0,1))
sphere = pal.body.Sphere((5,10,0,1),mass=1)

objects.append(glh.Box(terrain,(0,0,255)))
objects.append(glh.Box(sbox, (255, 0, 0)))
objects.append(glh.Box(sbox1, (0, 255, 0)))
objects.append(glh.Ball(sphere, (0, 255, 255)))
objects.append(glh.Box(box1, (255, 255, 0)))
objects.append(glh.Ball(ssphere, (255, 0, 255)))

#prismatic = pal.link.Prismatic(sbox,sphere,sbox.get_position(),(1,0,0),False)
#prismatic.set_limits(0,20)
#revolute = pal.link.Spherical(sbox1,box,sbox1.get_position(),False)

#rigid = pal.link.Rigid(box,sphere.body,False)

control = box1

gluLookAt(5,5,5,0,0,0,0,1,0)
running = True
while running:
    pal.update(1./50.)
    glh.render(objects)
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            running = not running
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                pass
            elif event.key == K_RIGHT:
                control.set_active(True)
                control.apply_impulse((75,0,0))
            elif event.key == K_LEFT:
                control.set_active(True)
                control.apply_impulse((-75,0,0))
            elif event.key == K_UP:
                control.set_active(True)
                control.apply_impulse((0,75,0))
            elif event.key == K_DOWN:
                control.set_active(True)
                control.apply_impulse((0,-75,0))
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
