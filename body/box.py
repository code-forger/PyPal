from pypalgame import private_globals as pal
import ctypes as c
import weakref
from bodybase import BodyBase
class Box(BodyBase):
    def __init__(self,rect,mass = None, density = None):
        """
        constructs a box and adds it to the world
        
        rect: a 6 part tuple with x,y,z,width,height,depth.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        static: used to create this object static, if static is true, mass will be ignored
        """
        self.obj = pal.lib.create_box(c.c_float(rect[0]),c.c_float(rect[1]),c.c_float(rect[2]),c.c_float(rect[3]),c.c_float(rect[4]),c.c_float(rect[5]),c.c_float(mass))

    def get_size(self):
        """returns the size of the object in a 3 part tuple"""
        size = [c.c_float() for x in range(3)]
        pal.lib.box_get_size(self.obj,c.byref(size[0]),c.byref(size[1]),c.byref(size[2]))
        return [p.value for p in size]

    def is_active(self):
        """Returns true if the body is not asleep."""
        pal.lib.box_is_active.restype = c.c_bool
        return pal.lib.box_is_active(self.obj)

    def set_active(self,active):
        """Sets the body to active or not."""
        pal.lib.box_set_active(self.obj,c.c_bool(active))

    def apply_impulse(self,impulse):
        """Applies an impulse to the object for a single step at an optional offset in world coordinates."""
        pal.lib.box_apply_impulse(self.obj,c.c_float(impulse[0]),c.c_float(impulse[1]),c.c_float(impulse[2]))

    def get_velocity(self):
        """Returns the linear velocity of the body."""
        pal.lib.box_get_velocity_x.restype = c.c_float
        pal.lib.box_get_velocity_y.restype = c.c_float
        pal.lib.box_get_velocity_z.restype = c.c_float
        return [pal.lib.box_get_velocity_x(self.obj),pal.lib.box_get_velocity_y(self.obj),pal.lib.box_get_velocity_z(self.obj)]

    def get_angular_velocity(self):
        """Returns the linear velocity of the body."""
        pal.lib.box_get_angular_velocity_x.restype = c.c_float
        pal.lib.box_get_angular_velocity_y.restype = c.c_float
        pal.lib.box_get_angular_velocity_z.restype = c.c_float
        return [pal.lib.box_get_angular_velocity_x(self.obj),pal.lib.box_get_angular_velocity_y(self.obj),pal.lib.box_get_angular_velocity_z(self.obj)]

    def apply_impulse(self, impulse,pos=None):
        """Applies an impulse to the object for a single step at an optional offset in world coordinates."""
        if pos:
            pal.lib.box_apply_impulse_at_pos(self.obj,c.c_float(impulse[0]),c.c_float(impulse[1]),c.c_float(impulse[2])
                                                   ,c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]))
        else:
            pal.lib.box_apply_impulse(self.obj,c.c_float(impulse[0]),c.c_float(impulse[1]),c.c_float(impulse[2]))

    def apply_angular_impulse(self, impulse):
        """Applies an angular impulse to the object for a single step at an optional offset in world coordinates."""
        pal.lib.box_apply_angular_impulse(self.obj,c.c_float(impulse[0]),c.c_float(impulse[1]),c.c_float(impulse[2]))

    def apply_force(self, force,pos=None):
        """Applies a force to the object for a single step at an optional offset in world coordinates."""
        if pos:
            pal.lib.box_apply_force_at_pos(self.obj,c.c_float(force[0]),c.c_float(force[1]),c.c_float(force[2])
                                                   ,c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]))
        else:
            pal.lib.box_apply_force(self.obj,c.c_float(force[0]),c.c_float(force[1]),c.c_float(force[2]))

    def apply_torque(self, force):
        """Applies a torque to the object for a single step."""
        pal.lib.box_apply_torque(self.obj,c.c_float(force[0]),c.c_float(force[1]),c.c_float(force[2]))


    def delete(self):
        pal.lib.box_remove(self.obj)
        del pal.all_objects[str(self.obj)]


class StaticBox(BodyBase):
    def __init__(self,rect):#TESTED
        self.obj = pal.lib.create_static_box(c.c_float(rect[0]),c.c_float(rect[1]),c.c_float(rect[2]),c.c_float(rect[3]),c.c_float(rect[4]),c.c_float(rect[5]))
        self.size = rect[3:]

    def get_size(self):
        """returns the size of the object in a 3 part tuple"""
        return self.size

    def delete(self):
        print "delete"
        pal.lib.static_box_remove(self.obj)
        del pal.all_objects[str(self.obj)]
