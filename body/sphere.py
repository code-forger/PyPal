import private_globals as pal
import ctypes as c
import weakref
from bodybase import BodyBase
class Sphere(BodyBase):
    def _create(self,rect,mass = None, density = None):
        self.obj = pal.lib.create_sphere(c.c_float(rect[0]),c.c_float(rect[1]),c.c_float(rect[2]),c.c_float(rect[3]),c.c_float(mass))
        self.size = rect[3]

    def get_size(self):
        """returns the radius of the sphere"""
        return self.size

    def apply_impulse(self,impulse):
        """Applies an impulse to the object for a single step at an optional offset in world coordinates."""
        pal.lib.sphere_apply_impulse(self.obj,c.c_float(impulse[0]),c.c_float(impulse[1]),c.c_float(impulse[2]))

    def is_active(self):
        """Returns true if the body is not asleep."""
        pal.lib.sphere_is_active.restype = c.c_bool
        return pal.lib.sphere_is_active(self.obj)

    def set_active(self,active):
        """Sets the body to active or not."""
        pal.lib.sphere_set_active(self.obj,c.c_bool(active))

    def get_velocity(self):
        """Returns the linear velocity of the body."""
        pal.lib.sphere_get_velocity_x.restype = c.c_float
        pal.lib.sphere_get_velocity_y.restype = c.c_float
        pal.lib.sphere_get_velocity_z.restype = c.c_float
        return [pal.lib.sphere_get_velocity_x(self.obj),pal.lib.sphere_get_velocity_y(self.obj),pal.lib.sphere_get_velocity_z(self.obj)]

    def get_angular_velocity(self):
        """Returns the angular velocity of the body."""
        pal.lib.sphere_get_angular_velocity_x.restype = c.c_float
        pal.lib.sphere_get_angular_velocity_y.restype = c.c_float
        pal.lib.sphere_get_angular_velocity_z.restype = c.c_float
        return [pal.lib.sphere_get_angular_velocity_x(self.obj),pal.lib.sphere_get_angular_velocity_y(self.obj),pal.lib.sphere_get_angular_velocity_z(self.obj)]

    def apply_impulse(self, impulse,pos=None):
        """Applies a impulse to the object for a single step at an optional offset in world coordinates."""
        if pos:
            pal.lib.sphere_apply_impulse_at_pos(self.obj,c.c_float(impulse[0]),c.c_float(impulse[1]),c.c_float(impulse[2])
                                                   ,c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]))
        else:
            pal.lib.sphere_apply_impulse(self.obj,c.c_float(impulse[0]),c.c_float(impulse[1]),c.c_float(impulse[2]))

    def apply_angular_impulse(self, impulse, pos=(0,0,0)):
        """Applies a impulse to the object for a single step at an optional offset in world coordinates."""
        pal.lib.sphere_apply_angular_impulse(self.obj,c.c_float(impulse[0]),c.c_float(impulse[1]),c.c_float(impulse[2]))

    def apply_force(self, force,pos=None):
        """Applies a force to the object for a single step at an optional offset in world coordinates."""
        if pos:
            pal.lib.sphere_apply_force_at_pos(self.obj,c.c_float(force[0]),c.c_float(force[1]),c.c_float(force[2])
                                                   ,c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]))
        else:
            pal.lib.sphere_apply_force(self.obj,c.c_float(force[0]),c.c_float(force[1]),c.c_float(force[2]))

    def apply_torque(self, force, pos=(0,0,0)):
        """Applies a torque to the object for a single step at an optional offset in world coordinates."""
        pal.lib.sphere_apply_torque(self.obj,c.c_float(force[0]),c.c_float(force[1]),c.c_float(force[2]))

    def delete(self):
        pal.lib.sphere_remove(self.obj)
        del pal.all_objects[str(self.obj)]


class StaticSphere(BodyBase):
    def _create(self,rect):#TESTED
        self.obj = pal.lib.create_static_sphere(c.c_float(rect[0]),c.c_float(rect[1]),c.c_float(rect[2]),c.c_float(rect[3]))
        self.size = rect[3:]

    def get_size(self):
        """returns the size of the object in a 3 part tuple"""
        return self.size

    def delete(self):
        pal.lib.static_sphere_remove(self.obj)
        del pal.all_objects[str(self.obj)]
