#this example is equivelent to the C++ basic pal example as seen on <www.>

import pypalgame as pal # Import the module.

pal.init() # Initialise module, this MUST be done before any other module call.

terain =  pal.body.Terrain.create((0,0,0),50) # Create a 50x50 terrain at (0,0,0).
box = pal.body.Box.create((0,5,0,1,1,1),mass = 1) # Create a 1x1x1 box at (0,5,0) with mass 1.

for x in range(5):
    pal.update(0.02) # Update the simulation by 0.02 seconds.
    print "Current box position is %6.5f at time %4.2f" % \
          (box.get_position()[1],pal.get_time()) # Print the box position and the simulation time.

pal.cleanup() # Done with the physics, release the memory and destroy all objects.
              # Note: you must not use any other pypal call after this, unless you recall 'pal.init()'.
