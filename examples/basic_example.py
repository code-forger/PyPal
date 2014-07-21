# This example is equivelent to the C++ basic pal example as seen on <http://www.adrianboeing.com/pal/current/pal/pal/documentation/html/index.html>

import pypal as pal

pal.init()

terain =  pal.body.TerrainPlane((0,0,0),50)
box = pal.body.Box((0,5,0),(1,1,1),mass = 1)

for x in range(25):
    pal.update(0.02)
    print "Current box position is %6.5f at time %4.2f" % \
          (box.get_position()[1],pal.get_time())

pal.cleanup()
