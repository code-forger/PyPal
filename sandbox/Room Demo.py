import pygame 
from pygame.locals import *

from OpenGL.GL import (
    GL_DEPTH_TEST, glEnable, glTranslate)
from OpenGL.GLU import gluPerspective, gluLookAt

import glhelp as glh

import pypalgame as pal
pal.init()

pygame.init()
pygame.display.set_mode(
    (1024, 768), pygame.locals.OPENGL | pygame.locals.DOUBLEBUF)

glEnable(GL_DEPTH_TEST)
gluPerspective(60.0, 640.0 / 480.0, 0.5, 1000.0)
glTranslate(0, -5, -15)

objects = []
area_bodies = []
room2offset = 20
room3offset = 40


player = pal.body.Box((0,1,0,1,1,1),mass=10)
objects.append(glh.Box(player, (255, 255, 0)))



def wipe_area_bodies():
    global objects
    global area_bodies
    for b in area_bodies:
        b.delete()
    area_bodies = []
    objects = []
    objects.append(glh.Box(player, (255, 255, 0)))

def load_area_one():

    wipe_area_bodies()

    terrain1 = pal.body.StaticBox((0,0,0,30,1,20))
    objects.append(glh.Box(terrain1,(0,0,255)))

    sbox11 = pal.body.StaticBox((15,1.5,0,1.,3.,20.))
    objects.append(glh.Box(sbox11, (255, 0, 0)))
    sbox12 = pal.body.StaticBox((-15,1.5,0,1.,3.,20.))
    objects.append(glh.Box(sbox12, (255, 0, 0)))
    sbox13 = pal.body.StaticBox((0,1.5,10,30.,3.,1.))
    objects.append(glh.Box(sbox13, (255, 0, 0)))
    sbox14 = pal.body.StaticBox((15/2.+1,1.5,-10,15.-1,3.,1.))
    objects.append(glh.Box(sbox14, (255, 0, 0)))
    sbox15 = pal.body.StaticBox((-15/2.-1,1.5,-10,15.-1,3.,1.))
    objects.append(glh.Box(sbox15, (255, 0, 0)))

    terrain2 = pal.body.StaticBox((0,0,-room2offset,30,1,20))
    objects.append(glh.Box(terrain2,(0,0,255)))

    sbox21 = pal.body.StaticBox((15,1.5,-room2offset,1.,3.,20.))
    objects.append(glh.Box(sbox21, (255, 0, 0)))
    sbox22 = pal.body.StaticBox((-15,1.5,-10/2.-1-room2offset,1.,3.,10.-1))
    objects.append(glh.Box(sbox22, (255, 0, 0)))
    sbox26 = pal.body.StaticBox((-15,1.5,10/2.+1-room2offset,1.,3.,10.-1))
    objects.append(glh.Box(sbox26, (255, 0, 0)))
    sbox23 = pal.body.StaticBox((15/2.+1,1.5,10-room2offset,15.-1,3.,1.))
    objects.append(glh.Box(sbox23, (255, 0, 0)))
    sbox25 = pal.body.StaticBox((-15/2.-1,1.5,10-room2offset,15.-1,3.,1.))
    objects.append(glh.Box(sbox25, (255, 0, 0)))
    sbox24 = pal.body.StaticBox((0,1.5,-10-room2offset,30.,3.,1.))
    objects.append(glh.Box(sbox24, (255, 0, 0)))


    bridge_floor = pal.body.StaticBox((0-(room3offset/2),0,-room2offset,10,1,5))
    objects.append(glh.Box(bridge_floor,(0,0,255)))

    sboxbridge1 = pal.body.StaticBox((-room2offset,1.5,2.5-(room3offset/2),10.,3.,1.))
    objects.append(glh.Box(sboxbridge1, (255, 0, 0)))
    sboxbridge2 = pal.body.StaticBox((-room2offset,1.5,-2.5-(room3offset/2),10.,3.,1.))
    objects.append(glh.Box(sboxbridge2, (255, 0, 0)))


    trigger = pal.body.Ghost((0-(room3offset/2)-5,0,-room2offset,5,5,5))

    def switch_on_trigger(name,trigger):
        if trigger.collide(player):
            pal.get_actions()[name].pause()
            load_area_two()

    switcher = pal.actuator.Action("switcher", switch_on_trigger,"switcher",trigger)
    switcher.run()

    area_bodies.extend([terrain1,sbox11,sbox12,sbox13,sbox14,sbox15,
                       terrain2,sbox21,sbox22,sbox23,sbox24,sbox25,sbox26,
                       bridge_floor,sboxbridge1,sboxbridge2,trigger])


def load_area_two():

    wipe_area_bodies()

    terrain3 = pal.body.StaticBox((0-room3offset,0,0,30,1,20))
    objects.append(glh.Box(terrain3,(0,0,255)))

    sbox31 = pal.body.StaticBox((15-room3offset,1.5,0,1.,3.,20.))
    objects.append(glh.Box(sbox31, (255, 0, 0)))
    sbox32 = pal.body.StaticBox((-15-room3offset,1.5,0,1.,3.,20.))
    objects.append(glh.Box(sbox32, (255, 0, 0)))
    sbox33 = pal.body.StaticBox((0-room3offset,1.5,10,30.,3.,1.))
    objects.append(glh.Box(sbox33, (255, 0, 0)))
    sbox34 = pal.body.StaticBox((15/2.+1-room3offset,1.5,-10,15.-1,3.,1.))
    objects.append(glh.Box(sbox34, (255, 0, 0)))
    sbox35 = pal.body.StaticBox((-15/2.-1-room3offset,1.5,-10,15.-1,3.,1.))
    objects.append(glh.Box(sbox35, (255, 0, 0)))


    terrain4 = pal.body.StaticBox((0-room3offset,0,-room2offset,30,1,20))
    objects.append(glh.Box(terrain4,(0,0,255)))

    sbox41 = pal.body.StaticBox((-15-room3offset,1.5,-room2offset,1.,3.,20.))
    objects.append(glh.Box(sbox41, (255, 0, 0)))
    sbox42 = pal.body.StaticBox((15-room3offset,1.5,-10/2.-1-room2offset,1.,3.,10.-1))
    objects.append(glh.Box(sbox42, (255, 0, 0)))
    sbox46 = pal.body.StaticBox((15-room3offset,1.5,10/2.+1-room2offset,1.,3.,10.-1))
    objects.append(glh.Box(sbox46, (255, 0, 0)))
    sbox43 = pal.body.StaticBox((15/2.+1-room3offset,1.5,10-room2offset,15.-1,3.,1.))
    objects.append(glh.Box(sbox43, (255, 0, 0)))
    sbox45 = pal.body.StaticBox((-15/2.-1-room3offset,1.5,10-room2offset,15.-1,3.,1.))
    objects.append(glh.Box(sbox45, (255, 0, 0)))
    sbox44 = pal.body.StaticBox((0-room3offset,1.5,-10-room2offset,30.,3.,1.))
    objects.append(glh.Box(sbox44, (255, 0, 0)))


    bridge_floor = pal.body.StaticBox((0-(room3offset/2),0,-room2offset,10,1,5))
    objects.append(glh.Box(bridge_floor,(0,0,255)))

    sboxbridge1 = pal.body.StaticBox((-room2offset,1.5,2.5-(room3offset/2),10.,3.,1.))
    objects.append(glh.Box(sboxbridge1, (255, 0, 0)))
    sboxbridge2 = pal.body.StaticBox((-room2offset,1.5,-2.5-(room3offset/2),10.,3.,1.))
    objects.append(glh.Box(sboxbridge2, (255, 0, 0)))

    trigger = pal.body.Ghost((0-(room3offset/2)+5,0,-room2offset,5,5,5))


    def switch_on_trigger(name,trigger):
        if trigger.collide(player):
            pal.get_actions()[name].pause()
            load_area_one()

    switcher = pal.actuator.Action("switcher", switch_on_trigger,"switcher",trigger)
    switcher.run()

    area_bodies.extend([terrain3,sbox31,sbox32,sbox33,sbox34,sbox35,
                       terrain4,sbox41,sbox42,sbox43,sbox44,sbox45,sbox46,
                       bridge_floor,sboxbridge1,sboxbridge2,trigger])

load_area_one()





#prismatic = pal.link.Prismatic(sbox,sphere,sbox.get_position(),(1,0,0),False)
#prismatic.set_limits(0,20)
#revolute = pal.link.Spherical(sbox1,box,sbox1.get_position(),False)

#rigid = pal.link.Rigid(box,sphere.body,False)

control = player

running = True
gluLookAt(5,5,5,0,0,0,0,1,0)
while running:
    pal.update(1./50.)
    #player.set_position([0,2,0])
    glh.render(objects)
    events = pygame.event.get()
    print "%1.3f,%1.3f,%1.3f,%1.3f,%1.3f,%1.3f"%(player.get_location()[3],player.get_location()[4],player.get_location()[5],
                                     player.get_angular_velocity()[0],player.get_angular_velocity()[1],player.get_angular_velocity()[2])
    for event in events:
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
