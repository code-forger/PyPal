from private_globals import *

class BodyBase(PalObject):

    """The Base of any body in the world

    Provides a set of basic accessor functions for all bodies.
    """
    def get_position(self):#TESTED
        """Returns position as a 3 part tuple:(x,y,z)."""
        pos = [c.c_float() for x in range(3)]
        lib.body_get_position(self.obj,c.byref(pos[0]),c.byref(pos[1]),c.byref(pos[2]))
        return [p.value for p in pos]

    def get_location(self):#TESTED
        """Returns position as a 3 part tuple:(x,y,z)."""
        pos = [c.c_float() for x in range(6)]
        lib.body_get_primative_location(self.obj,c.byref(pos[0]),c.byref(pos[1]),c.byref(pos[2]),c.byref(pos[3]),c.byref(pos[4]),c.byref(pos[5]))
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

    def set_orientation(rot):
        """Sets the position of the object and/or its orientation."""
        pass

    def apply_force(force,pos=(0,0,0)):
        """Applies a force to the object for a single step at an optional offset in world coordinates."""
        pass

    def apply_angular_impulse(impulse):
        """Applies an angular impulse to the object for a single step."""
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

    #collision detection functions

    def notify_collision(self,enabled):
        """informs the body that it can at any time have its current collision points requested"""
        lib.collision_notify(self.obj,enabled)
        if enabled:
            notified_objects.append(weakref.proxy(self))
        elif self.obj in notified_objects:
            notified_objects.remove(self)

    def get_contacts(self):
        """returns the bodies that this body is currently in contact with."""
        contacts = lib.get_contacts(self.obj)
        ret = []
        lib.contacts_get_distance.restype = c.c_float
        for x in range(lib.contacts_get_size(contacts)):
            ret.append([weakref.proxy(all_objects[str(lib.contacts_get_body_one(contacts,x))]),
                      weakref.proxy(all_objects[str(lib.contacts_get_body_two(contacts,x))])])
        lib.remove_contact(contacts)
        return ret
        
    def get_unique_contacts(self):
        """returns the bodies that this body is currently in contact with."""
        contacts = lib.get_contacts(self.obj)
        ret = []
        lib.contacts_get_distance.restype = c.c_float
        print all_objects
        for x in range(lib.contacts_get_size(contacts)):
            a = weakref.proxy(all_objects[str(lib.contacts_get_body_one(contacts,x))])
            b = weakref.proxy(all_objects[str(lib.contacts_get_body_two(contacts,x))])
            if [a,b] not in ret:
                ret.append([a,b])
        lib.remove_contact(contacts)
        try:
            print ret[0] == ret[1]
        except: pass
        return ret
            

    @property
    def mass():
        """the mass of the object"""
        pass
