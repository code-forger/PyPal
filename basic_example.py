#this example is equivelent to the C++ basic pal example as seen on <www.>

import pypalgame as pal

pal.init()

terain =  pal.body.Terrain.create((0,0,0),50)
box = pal.body.Box.create((0,5,0,1,1,1),mass = 1)

for x in range(5):
    pal.update(0.02)
    print "Current box position is %6.5f at time %4.2f" % \
          (box.get_position()[1],pal.get_time())

pal.cleanup()
