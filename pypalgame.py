
"""
Python Bindings for PAL geared toward game development

Module functions:

"""

import ctypes
_PAL = ctypes.cdll.LoadLibrary('./libPyPalGame.so')

def __init__(gravity = (0,-9.8,0)):
    """Initializes the module.

    gravity = (0,-9.8,0): gravity to be applied to the world.
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

def set_group_collision(a,b,enabled)
    """Sets the interactions between collision groups to enabled/disabled.

    a: palgroup a.
    b: palgroub b.
    enabled (bool): sets wether or not group a and b should collide.
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
    
class PalBodyBase():

    """The Base of any body in the world

    Provides a set of basic accessor functions for all bodies.
    """
    
    def get_position():
        """Returns position as a 3 part tuple:(x,y,z)."""
        pass

    def set_material(material):
        """Sets the material of the body."""
        pass

    def get_group():
        """Returns the collisions group of the body."""
        pass

    def set_group(group):
        """Puts the body in the provided collision group."""
        pass

    def set_user_data(data):
        """Sets user data to be stored in the body."""
        pass

    def get_user_data():
        """Returns the user data currently in the body."""
        pass

    def set_position(pos=None,rot=None):
        """Sets the position of the object and/or its orientation."""
        pass

    def apply_force(force,pos=(0,0,0)):
        """Applies a force to the object for a single step at an optional offset in world coordinates."""
        pass

    def apply_impulse(impulse,pos=(0,0,0)):
        """Applies an impulse to the object for a single step at an optional offset in world coordinates."""
        pass

    def apply_angular_impulse(impulse):
        """Applies an angular impulse to the object for a single step."""
        pass

    def get_velocity():
        """Returns the linear velocity of the body."""
        pass

    def set_velocity():
        """Sets the linear velocity of the body."""
        pass

    def get_angular_velocity():
        """Returns the angular velocity of the body."""
        pass

    def set_angular_velocity():
        """Sets the angular velocity of the body."""
        pass

    def is_active():
        """Returns true if the body is not asleep."""
        pass

    def set_active(active):
        """Sets the body to active or not."""
        pass

    @property
    def mass():
        """the mass of the object"""
        pass

if __name__ == "__main__":

    _PAL.runer()
