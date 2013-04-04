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

def posz(pos):
    pos[0] *= 10
    pos[1] *= -10
    pos[0]+=250
    pos[1]+=490
    return pos

def posy(pos):
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
tsprite.rect = Rect(posz([terain.get_position()[0],terain.get_position()[1],500,10]))
box = []
sprites = []
spritesd = []
dim = 6
number = dim*dim*dim
fps = 50.
cl = pygame.time.Clock()
f = sgc.FPSCounter(pos=(10,10),clock=cl,label="fps")
f.add()
for i in range(number):
    b = pal.body.Box((i%dim,(i/dim)%dim,i/(dim*dim),1,1,1),mass=10)
    bsprite = pygame.sprite.Sprite(drawable)
    bsprite.image = pygame.Surface((10,10))
    bsprite.image.fill((0,255,0))
    bsprite.rect = Rect(posz([b.get_position()[0],b.get_position()[1],10,10]))
    sprites.append(bsprite)
    bsprite = pygame.sprite.Sprite(drawable)
    bsprite.image = pygame.Surface((10,10))
    bsprite.image.fill((255,0,0))
    bsprite.rect = Rect(posz([b.get_position()[0],b.get_position()[1],10,10]))
    spritesd.append(bsprite)
    box.append(b)


b = pal.body.Sphere((2.5,1000,2.5,1.5),mass=20)
bsprite = pygame.sprite.Sprite(drawable)
bsprite.image = pygame.Surface((10,10))
bsprite.image.fill((0,255,0))
bsprite.rect = Rect(posz([b.get_position()[0],b.get_position()[1],10,10]))
sprites.append(bsprite)
bsprite = pygame.sprite.Sprite(drawable)
bsprite.image = pygame.Surface((10,10))
bsprite.image.fill((255,0,0))
bsprite.rect = Rect(posz([b.get_position()[0],b.get_position()[1],10,10]))
spritesd.append(bsprite)
box.append(b)

running = True
while running:
    time = cl.tick()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = not running
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                pass
    
    pal.update(time/1000.)
    print time
    for i in range(number+1):
        sprites[i].rect.center = posz([box[i].get_position()[0],box[i].get_position()[1]])
    tsprite.rect.center = posz([terain.get_position()[0],terain.get_position()[1]])
    
    for i in range(number+1):
        spritesd[i].rect.center = posy([box[i].get_position()[0],box[i].get_position()[2]])
    window.fill((128,128,128))
    sgc.update(time)
    drawable.draw(window)
    pygame.display.flip()

print pal._pal.all_objects
for b in box:
    b.delete()
print pal._pal.all_objects

pal.cleanup()
