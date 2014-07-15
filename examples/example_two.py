"""
    This example file deomstrates; basic bodies, static bodies, links, and actuators.
    It also shows how to use the glhelp.py module I have provided to help prototype
    and test your use of pypal.
"""
# import pygame and gl for drawing to the screen
import pygame 
from pygame.locals import *

from OpenGL.GL import (
    GL_DEPTH_TEST, glEnable, glTranslate)
from OpenGL.GLU import gluPerspective, gluLookAt

import glhelp as glh

# import and initialize pypal
import pypal as pal
pal.init()

# set up our screen to show a nice view
pygame.init()
pygame.display.set_mode(
    (1024, 768), pygame.locals.OPENGL | pygame.locals.DOUBLEBUF)

glEnable(GL_DEPTH_TEST)
gluPerspective(60.0, 640.0 / 480.0, 0.5, 1000.0)
glTranslate(-0, -5, -20) # modify these numbers to move the entire graphics environment

# construct our objects 
objects = []

sbox2 = pal.body.StaticBox((0,1.5,0),(1,1,1)) # Create a pypal object
objects.append(glh.Box(sbox2, (255, 0, 255))) # add a graphics object

sbox1 = pal.body.StaticBox((0,0,0),(50,1,50))
objects.append(glh.Box(sbox1, (255, 255, 0)))

sbox11 = pal.body.StaticBox((10,1.5,0),(1.,3.,30.))
objects.append(glh.Box(sbox11, (255, 0, 255)))
sbox12 = pal.body.StaticBox((-10,1.5,0),(1.,3.,30.))
objects.append(glh.Box(sbox12, (255, 0, 255)))
sbox13 = pal.body.StaticBox((0,1.5,10),(30.,3.,1.))
objects.append(glh.Box(sbox13, (255, 0, 255)))
sbox14 = pal.body.StaticBox((0,1.5,-10),(30,3.,1.))
objects.append(glh.Box(sbox14, (255, 0, 255)))

#control here gives us easy acess to this object in the main loop
box = pal.body.Box((4,1.5,0),(1,1,1), mass=75)
objects.append(glh.Box(box, (255, 255, 255)))

# all the balls
for x in xrange(-9,9,2):
    for y in xrange(-9,9,2):
        sphere = pal.body.Sphere((x,3,y,.8),(1,))
        objects.append(glh.Ball(sphere, (0, 255, 255)))

# set up links and actuators
revolute = pal.link.Revolute(sbox2, box, sbox2.get_position(),[0,1,0],False)

motor = pal.actuator.DCMotor(revolute,15,1,1)
motor.set_voltage(100)


running = True
gluLookAt(25,25,25,0,0,0,0,1,0) # change these numbers to move the camera arround
while running:
    motor.apply() # make sure our actuator runs this step 
    pal.update(1./50.)
    glh.render(objects) # this renders our scene

    for event in pygame.event.get(): # here we respond to pygame events
        if event.type == QUIT:
            running = not running # quit the application on the [x] button

pal.cleanup() # end the simulation
