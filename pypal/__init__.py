
"""
Python Bindings for PAL.
"""

import collada

import actuator
import body
import geometry
import link
import material
import sensor
import ctypes as c
import weakref

import private_globals as _pal


def init(gravity = (0,-9.8,0)):
    """
    Initializes the module.

    This function must be called before any other function from this library is called.

    Parameters:
      gravity: ``float[3]``, default = (0,-9.8,0): gravity to be applied to the world.
    """
    libs = c.c_char_p("/usr/local/lib/")
    _pal.lib.pal_init(libs)
    _pal.lib.physics_init(c.c_float(gravity[0]),c.c_float(gravity[1]),c.c_float(gravity[2]))

def update(time_step):
    """
    Steps the simulation.

    Parameters:
      timestep: ``float`` time since last step.
    """
    _pal.lib.physics_update(c.c_float(time_step))
    for action in _pal.actions.values():
        action.response = action.function(*action.args,**action.kwargs)

def get_objects():
    """ Returns a weakref to all the physics objects """
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
    """ Ends the simulation. """
    _pal.all_objects = {}
    _pal.actions = {}
    _pal.lib.pal_cleanup()

def get_time():
    """ Returns age of the simulation. """
    _pal.lib.physics_get_time.restype = c.c_float
    return _pal.lib.physics_get_time()

def get_time_step():
    """ Returns last timestep. """
    _pal.lib.physics_get_last_timestep.restype = c.c_float
    return _pal.lib.physics_get_last_timestep()

def set_group_collision(group1,group2,collide):
    """
    Sets weather or not tho bodies from the specified groups should collide.

    Parameters:
      group1,group2: the groups between which the relation is being set.
      collide: bool, weather or not the two groups can collide with eachother  
    """
    _pal.lib.physics_set_group_collision(c.c_int(group1),c.c_int(group2),c.c_bool(collise));

def get_gravity():
    """ Returns the current gravity vector. """
    ret = _pal.Vec3()
    _pal.lib.physics_get_gracity(ret);
    return [x for x in ret]

def get_up_axis():
    """Return the index, i.e. x (0), y (1), or z(2), to use for up."""
    return _pal.lib.physics_get_up_axis()

#collision detection functions

def SetCollisionAccuracy(accuracy):
    """
    Not implemented yet.
    acccuracy: sets the acuracy of the simulateion, Ranges from 0..1, 0 indicates fast and inaccurate, 1 indicates accurate and slow. 
    """
    pass

def raycast(pos,direction,max_range):
    """
    Returns a dictionary with 'pos' and 'body' these values may be 'None' if unavailable
    
    Parameters:
      pos: ``float[3]`` The position to start the cast from
      dirction: ``float[3] The direction the cast will take
      max_range: ``float`` The max range of the cast.
    """
    _pal.lib.pal_ray_hit(c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),
                         c.c_float(direction[0]),c.c_float(direction[1]),c.c_float(direction[2]),
                         c.c_float(max_range))
    try:
        body = weakref.proxy(_pal.all_objects[str(_pal.lib.get_last_hit_body())])
    except KeyError:
        difference = 1000000000000000000 #XXX HACK
        key = None
        body = _pal.lib.get_last_hit_body()
        if body == 0:
            return None
        for k in _pal.all_objects.keys():
            if abs(int(k) - body) < difference:
                key = k
                difference = abs(int(k) - body)
        body = weakref.proxy(_pal.all_objects[key])
    pos = [c.c_float() for x in range(3)]
    _pal.lib.get_last_hit_location(c.byref(pos[0]),c.byref(pos[1]),c.byref(pos[2]))
    pos = [p.value for p in pos]
    return {'pos':pos, 'body': body}


def notify_collision(body,enabled):
    """
    Informs the body that it can at any time have its current collision points requested.

    Parameters:
      body: ``pypal.body`` The body to notify. 
      enabled: ``bool`` Weather we want to collect the collision poinsts later or not.
    """

    _pal.lib.collision_notify(body._body,enabled)
    if enabled:
        _pal.notified_objects.append(body)
    elif body.obj in notified_objects:
        _pal.notified_objects.remove(body)

def get_contacts(body):
    """
    Returns the bodies that this body is currently in contact with.

    Paramters:
      body: ``pypal.body`` The body we are qwerying the contacts.
      """
    contacts = _pal.lib.get_contacts(body._body)
    ret = []
    _pal.lib.contacts_get_distance.restype = c.c_float
    try:
        for x in range(_pal.lib.contacts_get_size(contacts)):
            ret.append([weakref.proxy(_pal.all_objects[str(_pal.lib.contacts_get_body_one(contacts,x))]),
                      weakref.proxy(_pal.all_objects[str(_pal.lib.contacts_get_body_two(contacts,x))])])
        _pal.lib.remove_contact(contacts)
    except KeyError:
        print "ERROR PAL HAS FAILED TO SUCCESFULLY CONSTRUCT A COLLISION!!!!"
    return ret
    
def get_unique_contacts(body):
    """
    Returns the bodies that this body is currently in contact with withought repeats.

    Paramters:
      body: ``pypal.body`` The body we are qwerying the contacts.
      """
    contacts = _pal.lib.get_contacts(body._body_base)
    ret = []
    _pal.lib.contacts_get_distance.restype = c.c_float
    try:
        for x in range(_pal.lib.contacts_get_size(contacts)):
            a = weakref.proxy(_pal.all_objects[str(_pal.lib.contacts_get_body_one(contacts,x))])
            b = weakref.proxy(_pal.all_objects[str(_pal.lib.contacts_get_body_two(contacts,x))])
            if [a,b] not in ret:
                ret.append([a,b])
        _pal.lib.remove_contact(contacts)
    except KeyError:
        pass
    try:
        print ret[0] == ret[1]
    except: pass
    return ret