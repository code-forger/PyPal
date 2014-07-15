import time

import pygame.display
import pygame.event

import pygame 
from pygame.locals import *

import math

from OpenGL.GL import (
    GL_TRIANGLE_STRIP, GL_POLYGON, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT,
    glPushMatrix, glPopMatrix, glMultMatrixd, glColor, glClear,
    glBegin, glEnd, glTranslate, glVertex, glRotate)
from OpenGL.GLU import gluNewQuadric, gluSphere, gluLookAt

import pypal as pal



def render_cube(x,y,z, color):
        glBegin(GL_POLYGON)
        glColor((0,255,0))
        glVertex( -x, -y, -z)
        glVertex( -x,  y, -z)
        glVertex(  x,  y, -z)
        glVertex(  x, -y, -z)
        glEnd()

        glBegin(GL_POLYGON)
        glColor((255,0,0))
        glVertex(  x, -y, z )
        glVertex(  x,  y, z )
        glVertex( -x,  y, z )
        glVertex( -x, -y, z )
        glEnd()
         
        glBegin(GL_POLYGON)
        glColor((0,0,255))
        glVertex(x, -y, -z )
        glVertex( x,  y, -z )
        glVertex( x,  y,  z )
        glVertex( x, -y,  z )
        glEnd()
         
        glBegin(GL_POLYGON)
        glColor((255,255,0))
        glVertex( -x, -y,  z )
        glVertex( -x,  y,  z )
        glVertex( -x,  y, -z )
        glVertex( -x, -y, -z )
        glEnd()
         
        glBegin(GL_POLYGON)
        glColor(*color)
        glVertex(  x,  y,  z )
        glVertex(  x,  y, -z )
        glVertex( -x,  y, -z )
        glVertex( -x,  y,  z )
        glEnd()
         
        glBegin(GL_POLYGON)
        glColor((255,0,255))
        glVertex( x, -y, -z )
        glVertex(  x, -y,  z )
        glVertex( -x, -y,  z )
        glVertex( -x, -y, -z )
        glEnd()

class Box:
    def __init__(self,body,color):
        self.body = body
        self.color = color

    def render(self):
        x, y, z = map(lambda x: x/2.,self.body.get_size())
        glColor(*self.color)
        glMultMatrixd(self.body.get_location())
        render_cube(x,y,z,self.color)

class Ball:
    def __init__(self, body, color):
        self.body = body
        self.quad = gluNewQuadric()
        self.color = color

    def render(self):
        o = self.body.get_position()
        glColor(*self.color)
        glTranslate(o[0], o[1], o[2])
        gluSphere(self.quad, self.body.get_size()[0], 25, 25)

def render(objects):
    glPushMatrix()
    for o in objects:
        glPushMatrix()
        o.render()
        glPopMatrix()
    glPopMatrix()

    pygame.display.flip()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
