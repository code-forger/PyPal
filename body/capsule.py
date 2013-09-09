from pypalgame import private_globals as pal
import ctypes as c
import weakref
from bodybase import BodyBase
class Capsule(BodyBase):
    typechar = 'c'
    def __init__(self,rect,mass = None, density = None, static = False):
        """
        constructs a box and adds it to the world
        
        rect: a 5 part tuple with x,y,z,radius,length.
        Note: if a 6 part rect is passed in, the width will be taken as the
        radius and the height as the length, the depth will be ignored.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        """
        self.obj = pal.lib.create_capsule(c.c_float(rect[0]),c.c_float(rect[1]),c.c_float(rect[2]),c.c_float(rect[3]),c.c_float(rect[4]),c.c_float(mass))
        self.size = list(rect[3:])

    def get_size(self):
        """returns the size of the object in a 2 part tuple"""
        return self.size

    def apply_impulse(self,impulse):
        """Applies an impulse to the object for a single step at an optional offset in world coordinates."""
        pal.lib.capsule_apply_impulse(self.obj,c.c_float(impulse[0]),c.c_float(impulse[1]),c.c_float(impulse[2]))

    def is_active(self):
        """Returns true if the body is not asleep."""
        pal.lib.capsule_is_active.restype = c.c_bool
        return pal.lib.capsule_is_active(self.obj)

    def set_active(self,active):
        """Sets the body to active or not."""
        pal.lib.capsule_set_active(self.obj,c.c_bool(active))

    def get_angular_velocity(self):
        """Returns the angular velocity of the body."""
        pal.lib.capsule_get_angular_velocity_x.restype = c.c_float
        pal.lib.capsule_get_angular_velocity_y.restype = c.c_float
        pal.lib.capsule_get_angular_velocity_z.restype = c.c_float
        return [pal.lib.capsule_get_angular_velocity_x(self.obj),pal.lib.capsule_get_angular_velocity_y(self.obj),pal.lib.capsule_get_angular_velocity_z(self.obj)]

    def get_velocity(self):
        """Returns the linear velocity of the body."""
        pal.lib.capsule_get_velocity_x.restype = c.c_float
        pal.lib.capsule_get_velocity_y.restype = c.c_float
        pal.lib.capsule_get_velocity_z.restype = c.c_float
        return [pal.lib.capsule_get_velocity_x(self.obj),pal.lib.capsule_get_velocity_y(self.obj),pal.lib.capsule_get_velocity_z(self.obj)]

    def apply_impulse(self, impulse,pos=None):
        """Applies a impulse to the object for a single step at an optional offset in world coordinates."""
        if pos:
            pal.lib.capsule_apply_impulse_at_pos(self.obj,c.c_float(impulse[0]),c.c_float(impulse[1]),c.c_float(impulse[2])
                                                   ,c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]))
        else:
            pal.lib.capsule_apply_impulse(self.obj,c.c_float(impulse[0]),c.c_float(impulse[1]),c.c_float(impulse[2]))

    def apply_angular_impulse(self, impulse, pos=(0,0,0)):
        """Applies a torque to the object for a single step at an optional offset in world coordinates."""
        pal.lib.capsule_apply_angular_impulse(self.obj,c.c_float(impulse[0]),c.c_float(impulse[1]),c.c_float(impulse[2]))

    def apply_force(self, force,pos=None):
        """Applies a force to the object for a single step at an optional offset in world coordinates."""
        if pos:
            pal.lib.capsule_apply_force_at_pos(self.obj,c.c_float(force[0]),c.c_float(force[1]),c.c_float(force[2])
                                                   ,c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]))
        else:
            pal.lib.capsule_apply_force(self.obj,c.c_float(force[0]),c.c_float(force[1]),c.c_float(force[2]))

    def apply_torque(self, force, pos=(0,0,0)):
        """Applies a torque to the object for a single step at an optional offset in world coordinates."""
        pal.lib.capsule_apply_torque(self.obj,c.c_float(force[0]),c.c_float(force[1]),c.c_float(force[2]))


class StaticCapsule(BodyBase):
    typechar = 'C'
    def __init__(self,rect):#TESTED
        self.obj = pal.lib.create_static_capsule(c.c_float(rect[0]),c.c_float(rect[1]),c.c_float(rect[2]),c.c_float(rect[3]),c.c_float(rect[4]))
        self.size = rect[3:]

    def get_size(self):
        """returns the size of the object in a 3 part tuple"""
        return self.size
