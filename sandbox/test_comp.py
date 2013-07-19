import pygame 
from pygame.locals import *

import sgc
from sgc.locals import *

import pypalgame as pal

import engine

def draw_box(b):
    points = b.get_size()
    print points
    location = b.get_location()
    print location


def pospos(pos):
    pos[0] *= 10
    pos[1] *= -10
    pos[0]+=250
    pos[1]+=490
    return pos

def posposz(pos):
    pos[0] *= 10
    pos[1] *= -10
    pos[0]+=250
    pos[1]+=490
    return pos

def posposy(pos):
    pos[0] *= 10
    pos[1] *= -10
    pos[0]+=500+250
    pos[1]+=250
    return pos

pygame.init()
window = sgc.surface.Screen((1000,500))

pal.init()

drawable = pygame.sprite.Group()

terain =  pal.body.Terrain((0,0,0),60)
tsprite = pygame.sprite.Sprite(drawable)
tsprite.image = pygame.Surface((500,10))
tsprite.image.fill((255,0,0))
tsprite.rect = Rect(pospos([terain.get_position()[0],terain.get_position()[1],500,10]))

box = pal.body.StaticBox((0,10,0,1,1,1))
bsprite = pygame.sprite.Sprite(drawable)
bsprite.image = pygame.Surface((10,10))
bsprite.image.fill((0,255,0))
bsprite.rect = Rect(pospos([box.get_position()[0],box.get_position()[1],10,10]))
bspritey = pygame.sprite.Sprite(drawable)
bspritey.image = pygame.Surface((10,10))
bspritey.image.fill((0,255,0))
bspritey.rect = Rect(pospos([box.get_position()[0],box.get_position()[1],10,10]))

box1 = pal.body.Compound((-5,10,0))
box1.add_box((0,0,0,1,1,1),mass=10)
box1.finalize()

b1sprite = pygame.sprite.Sprite(drawable)
b1sprite.image = pygame.Surface((10,10))
b1sprite.image.fill((0,255,0))
b1sprite.rect = Rect(pospos([box.get_position()[0],box.get_position()[1],10,10]))
b1spritey = pygame.sprite.Sprite(drawable)
b1spritey.image = pygame.Surface((10,10))
b1spritey.image.fill((0,255,0))
b1spritey.rect = Rect(pospos([box.get_position()[0],box.get_position()[1],10,10]))

box2 = pal.body.Compound((-10,10,0))
box2.add_capsule((0,0,0,1,5),mass=10)
box2.finalize()

b2sprite = pygame.sprite.Sprite(drawable)
b2sprite.image = pygame.Surface((10,10))
b2sprite.image.fill((0,255,0))
b2sprite.rect = Rect(pospos([box.get_position()[0],box.get_position()[1],10,10]))
b2spritey = pygame.sprite.Sprite(drawable)
b2spritey.image = pygame.Surface((10,10))
b2spritey.image.fill((0,255,0))
b2spritey.rect = Rect(pospos([box.get_position()[0],box.get_position()[1],10,10]))

box1.set_group(1)
box2.set_group(1)
box.set_group(1)
terain.set_group(1)


motorbool = False
cl = pygame.time.Clock()
running = True
impulseforce = 75
while running:
    time = cl.tick(50)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = not running
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                pass
            elif event.key == K_RIGHT or event.key == K_d:
                box1.set_active(True)
                box1.apply_impulse((impulseforce,0,0))
            elif event.key == K_LEFT or event.key == K_a:
                box1.set_active(True)
                box1.apply_impulse((-impulseforce,0,0))
            elif event.key == K_UP:
                box1.set_active(True)
                box1.apply_impulse((0,impulseforce,0))
            elif event.key == K_DOWN:
                box1.set_active(True)
                box1.apply_impulse((0,-impulseforce,0))
            elif event.key == K_w:
                box1.set_active(True)
                box1.apply_impulse((0,0,impulseforce))
            elif event.key == K_s:
                box1.set_active(True)
                box1.apply_impulse((0,0,-impulseforce))
    
    pal.update(1./50.)
    if motorbool: motor.run()

    bsprite.rect.center = posposz([box.get_position()[0],box.get_position()[1]])
    b1sprite.rect.center = posposz([box1.get_position()[0],box1.get_position()[1]])
    b2sprite.rect.center = posposz([box2.get_position()[0],box2.get_position()[1]])
    tsprite.rect.center = posposz([terain.get_position()[0],terain.get_position()[1]])
    bspritey.rect.center = posposy([box.get_position()[0],box.get_position()[2]])
    b1spritey.rect.center = posposy([box1.get_position()[0],box1.get_position()[2]])
    b2spritey.rect.center = posposy([box2.get_position()[0],box2.get_position()[2]])
    
    window.fill((0,0,0))
    drawable.draw(window)
    pygame.display.flip()
    print box1.get_position()[1]


print pal._pal.all_objects
box.delete()
box1.delete()
terain.delete()

print pal._pal.all_objects

pal.cleanup()
