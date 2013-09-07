
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
import ctypes as c
import weakref

import private_globals as _pal


def init(gravity = (0,-9.8,0)):
    """Initializes the module.

    This function must be called before any other function from this library is called

    gravity: int int int, default = (0,-9.8,0): gravity to be applied to the world.
    pygame: the pygame instance to be used to emit events.
    """
    libs = c.c_char_p("/usr/local/lib/")
    _pal.lib.pal_init(libs)
    _pal.lib.physics_init(c.c_float(gravity[0]),c.c_float(gravity[1]),c.c_float(gravity[2]))

def update(time_step):
    """Steps the simulation.

    timestep: time since last step
    """
    _pal.lib.physics_update(c.c_float(time_step))
    #print _pal.actions
    for action in _pal.actions.values():
        action.responce = action.function(*action.args,**action.kwargs)

def get_objects():
    """ Returns all physics objects"""
    objects = []
    for o in _pal.all_objects.values():
        objects.append(weakref.proxy(o))
    return objects

def get_actions():
    """ Returns all pal actions"""
    actions = {}
    for o in _pal.actions:
        actions[o] = weakref.proxy(_pal.actions[o])
    return actions

def cleanup():
    """Ends the simulation."""
    _pal.all_objects = {}
    _pal.lib.pal_cleanup()


def get_time():
    """Returns age of the simulation."""
    _pal.lib.pal_get_time.restype = c.c_float
    return _pal.lib.pal_get_time()

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
