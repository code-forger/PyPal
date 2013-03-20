from private_globals import *

class BodyBase():

    """The Base of any body in the world

    Provides a set of basic accessor functions for all bodies.
    """
    def get_position(self):#TESTED
        """Returns position as a 3 part tuple:(x,y,z)."""
        pos = [c.c_float() for x in range(3)]
        lib.body_get_position(self.obj,c.byref(pos[0]),c.byref(pos[1]),c.byref(pos[2]))
        return [p.value for p in pos]

    def set_material(self,material):
        """Sets the material of the body. DO NOT USE"""
        lib.body_set_material(self.obj,c.c_void_p(None))

    def get_group(self):#TESTED
        """Returns the collisions group of the body."""
        return lib.body_get_group(self.obj)

    def set_group(self,group):#TESTED
        """Puts the body in the provided collision group."""
        lib.body_set_group(self.obj,group)

    def set_user_data(self,data):#TESTED
        """Sets user data to be stored in the body."""
        userdata[lib.body_get_data(self.obj)] = data

    def get_user_data(self):#TESTED
        """Returns user data currently stored in the body."""
        return userdata[lib.body_get_data(self.obj)]

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

    def notify_collision(self,enabled):
        """informs the body that it can at any time have its current collision points requested"""
        lib.collision_notify(self.obj,enabled)

    def get_contacts(self):
        """returns the bodies that this body is currently in contact with."""
        contacts = lib.get_contacts(self.obj)
        ret = []
        lib.contacts_get_distance.restype = c.c_float
        for x in range(lib.contacts_get_size(contacts)):
            ret.append([all_objects[str(lib.body_get_data(lib.contacts_get_body_one(contacts,x)))],
                      all_objects[str(lib.body_get_data(lib.contacts_get_body_two(contacts,x)))],
                      lib.contacts_get_distance(contacts,x)])
        lib.remove_contact(contacts)
        return ret
        
            

    @property
    def mass():
        """the mass of the object"""
        pass
