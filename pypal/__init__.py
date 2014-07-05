
"""
Python Bindings for PAL geared toward game development

Module functions:

"""

print "DEBUG PYPAL VERSION SELECTED!"

import collada

import actuator
import body
import fluid
import geometry
import link
import material
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

def load_vertices_from_collada_file(f_name):
    mesh = collada.Collada(f_name)
    objects = []
    matricies = []
    for i in range(len(mesh.geometries)):
        objects.append(mesh.geometries[i].primitives[0].vertex.tolist())
        matricies.append(mesh.geometries[i].collada.scene.nodes[i].matrix[2][:3])
    return objects, matricies




def notify_collision(body,enabled):
    """informs the body that it can at any time have its current collision points requested"""
    _pal.lib.collision_notify(body.obj,enabled)
    if enabled:
        notified_objects.append(weakref.proxy(body))
    elif body.obj in notified_objects:
        notified_objects.remove(body)

def get_contacts(body):
    """returns the bodies that this body is currently in contact with."""
    contacts = _pal.lib.get_contacts(body.obj)
    ret = []
    _pal.lib.contacts_get_distance.restype = c.c_float
    try:
        for x in range(_pal.lib.contacts_get_size(contacts)):
            ret.append([weakref.proxy(_pal.all_objects[str(_pal.lib.contacts_get_body_one(contacts,x))]),
                      weakref.proxy(_pal.all_objects[str(_pal.lib.contacts_get_body_two(contacts,x))])])
        _pal.lib.remove_contact(contacts)
    except KeyError:
        pass
    return ret
    
def get_unique_contacts(body):
    """returns the bodies that this body is currently in contact with."""
    contacts = _pal.lib.get_contacts(body.obj)
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