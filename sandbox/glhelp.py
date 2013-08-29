import time

import pygame.display
import pygame.event

import pygame 
from pygame.locals import *

from OpenGL.GL import (
    GL_TRIANGLE_STRIP, GL_POLYGON, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT,
    glPushMatrix, glPopMatrix, glColor, glClear,
    glBegin, glEnd, glTranslate, glVertex)
from OpenGL.GLU import gluNewQuadric, gluSphere, gluLookAt


import pypalgame as pal

pal.init()


def render_cube(x,y,z):
        glBegin(GL_POLYGON)
        glVertex( -x, -y, -z)
        glVertex( -x,  y, -z)
        glVertex(  x,  y, -z)
        glVertex(  x, -y, -z)
        glEnd()

        glBegin(GL_POLYGON)
        glVertex(  x, -y, z )
        glVertex(  x,  y, z )
        glVertex( -x,  y, z )
        glVertex( -x, -y, z )
        glEnd()
         
        glBegin(GL_POLYGON)
        glVertex(x, -y, -z )
        glVertex( x,  y, -z )
        glVertex( x,  y,  z )
        glVertex( x, -y,  z )
        glEnd()
         
        glBegin(GL_POLYGON)
        glVertex( -x, -y,  z )
        glVertex( -x,  y,  z )
        glVertex( -x,  y, -z )
        glVertex( -x, -y, -z )
        glEnd()
         
        glBegin(GL_POLYGON)
        glVertex(  x,  y,  z )
        glVertex(  x,  y, -z )
        glVertex( -x,  y, -z )
        glVertex( -x,  y,  z )
        glEnd()
         
        glBegin(GL_POLYGON)
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
        x, y, z = map(lambda x: x/2,self.body.get_size())
        o = self.body.get_position()
        glColor(*self.color)
        glTranslate(o[0], o[1], o[2])
        render_cube(x,y,z)

class Ball:
    def __init__(self, body, color):
        self.body = body
        self.quad = gluNewQuadric()
        self.color = color


    def render(self):
        o = self.body.get_position()
        glColor(*self.color)
        glTranslate(o[0], o[1], o[2])
        gluSphere(self.quad, self.body.get_size(), 25, 25)

def render(objects):
    glPushMatrix()
    for o in objects:
        glPushMatrix()
        o.render()
        glPopMatrix()
    glPopMatrix()

    pygame.display.flip()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)