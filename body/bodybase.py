from private_locals import *

class BodyBase():

    """The Base of any body in the world

    Provides a set of basic accessor functions for all bodies.
    """
    def get_position(self):
        """Returns position as a 3 part tuple:(x,y,z)."""
        pos = [c.c_float() for x in range(3)]
        pal_lib.get_position(self.obj,c.byref(pos[0]),c.byref(pos[1]),c.byref(pos[2]))
        
        return [p.value for p in pos]

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

    #collision detection functions

    def notifyCollision():
        """informs the body that it can at any time have its current collision points requested"""
        pass

    def getContacts():
        """returns the bodies that this body is currently in contact with."""
        pass

    @property
    def mass():
        """the mass of the object"""
        pass
