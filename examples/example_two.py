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

#import the helper module
import glhelp as glh

# set up our screen to show a nice view
pygame.init()
pygame.display.set_mode(
    (1024, 768), pygame.locals.OPENGL | pygame.locals.DOUBLEBUF)

glEnable(GL_DEPTH_TEST)
gluPerspective(60.0, 640.0 / 480.0, 0.5, 1000.0)

# Here begins the physics code.

# import and initialize pypal
import pypal as pal
pal.init()

# construct our physics objects 
# This is the 'anchor' for our moving box
anchor = pal.body.StaticBox((0,1.5,0),(1,1,1)) # Create a pypal object

# This is the ground
floor = pal.body.TerrainPlane((0,0,0),50)

# These are our 4 walls
wall1 = pal.body.StaticBox((10,1.5,0),(1.,3.,30.))
wall2 = pal.body.StaticBox((-10,1.5,0),(1.,3.,30.))
wall3 = pal.body.StaticBox((0,1.5,10),(30.,3.,1.))
wall4 = pal.body.StaticBox((0,1.5,-10),(30,3.,1.))

# create our moving box
box = pal.body.Box((4,1.5,0),(1,1,1), mass=75)


objects = [] # a list of all our graphical objects.
objects.append(glh.Box(anchor, (1, 0, 1))) # add a graphics object

objects.append(glh.Box(floor, (1, 1, 0)))

objects.append(glh.Box(wall1, (1, 0, 1)))
objects.append(glh.Box(wall2, (1, 0, 1)))
objects.append(glh.Box(wall3, (1, 0, 1)))
objects.append(glh.Box(wall4, (1, 0, 1)))

objects.append(glh.Box(box, (1, 1, 1)))

# all the balls
for x in xrange(-9,9,2):
    for y in xrange(-9,9,2):
        sphere = pal.body.Sphere((x,3,y,.8),(1,))
        objects.append(glh.Ball(sphere, (0, 1, 1)))

# set up links and actuators
revolute = pal.link.Revolute(anchor, box, anchor.get_position(),[0,1,0],False)

motor = pal.actuator.DCMotor(revolute,15,1,1)
motor.set_voltage(100)
motor.turn_on()


running = True
gluLookAt(25,25,25,0,0,0,0,1,0) # change these numbers to move the camera arround
while running:
    pal.update(1./50.)
    glh.render(objects) # this renders our scene

    for event in pygame.event.get(): # here we respond to pygame events
        if event.type == QUIT:
            running = not running # quit the application on the [x] button

pal.cleanup() # end the simulation
