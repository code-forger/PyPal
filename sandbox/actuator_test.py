import pygame 
from pygame.locals import *

from OpenGL.GL import (
    GL_DEPTH_TEST, glEnable, glTranslate)
from OpenGL.GLU import gluPerspective, gluLookAt

import glhelp as glh
import random
import pypalgame as pal

pal.init()

pygame.init()
pygame.display.set_mode(
    (1024, 768), pygame.locals.OPENGL | pygame.locals.DOUBLEBUF)

glEnable(GL_DEPTH_TEST)
gluPerspective(60.0, 640.0 / 480.0, 0.5, 1000.0)
glTranslate(-0, -5, -20)

objects = []


sbox1 = pal.body.StaticBox((0,0,0,50,1,50))
objects.append(glh.Box(sbox1, (255, 0, 0)))

sbox2 = pal.body.StaticBox((0,1.5,0,1.,1.,1.))
objects.append(glh.Box(sbox2, (255, 0, 0)))

sbox11 = pal.body.StaticBox((10,1.5,0,1.,3.,30.))
objects.append(glh.Box(sbox11, (255, 0, 0)))
sbox12 = pal.body.StaticBox((-10,1.5,0,1.,3.,30.))
objects.append(glh.Box(sbox12, (255, 0, 0)))
sbox13 = pal.body.StaticBox((0,1.5,10,30.,3.,1.))
objects.append(glh.Box(sbox13, (255, 0, 0)))
sbox14 = pal.body.StaticBox((0,1.5,-10,30,3.,1.))
objects.append(glh.Box(sbox14, (255, 0, 0)))

control = box = pal.body.Box((-2,1.5,0,1,1,1), mass=75)
objects.append(glh.Box(box, (255, 0, 0)))

box1 = pal.body.Box((-4,1.5,2,1,1,1), mass=75)
objects.append(glh.Box(box1, (255, 0, 0)))


for x in xrange(-9,9,2):
    for y in xrange(-9,9,2):
        for z in xrange(3,15,2): pass
            #sphere = pal.body.Sphere((x,z,y,.8),1)
            #objects.append(glh.Ball(sphere, (random.randint(0,1), random.randint(0,1), random.randint(0,1))))
p = list(sbox2.get_position())
revolute = pal.link.Revolute(sbox2, box,p ,[0,1,0],True)

motor = pal.actuator.DCMotor(revolute,100,1,1)
motor.set_voltage(200)
motor.turn_on()

spring = pal.actuator.Spring(box,box1,2,10,1)
spring.turn_on()

running = True
gluLookAt(5,5,5,0,0,0,0,1,0)
while running:
    pal.update(1./50.)
    #player.set_position([0,2,0])
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
