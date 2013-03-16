
"""
Python Bindings for PAL geared toward game development

Module functions:

"""

import actuator
import body
import fluid
import geometry
import link
import sensor
import vehicle

from private_locals import *

def __init__(gravity = (0,-9.8,0),pygame = None):
    """Initializes the module.

    gravity: int int int, default = (0,-9.8,0): gravity to be applied to the world.
    pygame: the pygame instance to be used to emit events.
    """
    pass

def update(time_step):
    """Steps the simulation.

    timestep: time since last step
    """
    pass

def cleanup():
    """Ends the simulation."""
    pass

def get_time():
    """Returns age of the simulation."""
    pass

def get_time_step():
    """Returns last timestep."""
    pass

def set_group_collision(group1,group2,collide):
    """
    group1,group2: the groups between which the relation is being set.
    collide: bool, wether or not the two groups can collide with eachother  
    """
    pass

def get_gravity():
    """Returns the current direction of gravity.

    returns:(x,y,z)
    """
    pass

def get_up_axis():
    """Return the index, i.e. x (0), y (1), or z(2), to use for up."""
    pass

def get_events():
    """
    returns all collision events for this step if ygame was not passed into
    __init__.
    if pygame was specifies in __init__ this function will post pygame mesages
    instead.
    """

#collision detection functions

def SetCollisionAccuracy(accuracy):
    """
    acccuracy: sets the acuracy of the simulateion, Ranges from 0..1, 0 indicates fast and inaccurate, 1 indicates accurate and slow. 
    """
    pass

def raycast(pos,direction,max_range):
    """
    returns a structure thusly: [pos,normal,distance,body,normal] any of these values may be 'None' if unavailable
    pos: the position to start the cast from
    dirction: the direction the cast will take
    max_range: the max range of the cast
    """
    pass

if __name__ == "__main__":

    x = pal_lib.build()
    print x
    pal_lib.runPhy(x)
