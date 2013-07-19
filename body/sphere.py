import private_globals as pal
import ctypes as c
import weakref
from bodybase import BodyBase
class Sphere(BodyBase):
    def __new__(cls,rect,mass = None, density = None):
        """
        constructs a sphere and adds it to the world
        
        rect: a 6 part tuple with x,y,z,width,height,depth.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        static: used to create this object static, if static is true, mass will be ignored
        """
        sphere = super(Sphere,cls).__new__(cls)
        sphere._create(rect,mass,density)
        pal.all_objects[str(sphere.obj)] = sphere
        sphere.size = rect[3]
        return weakref.proxy(sphere)

    def _create(self,rect,mass = None, density = None):
        self.obj = pal.lib.create_sphere(c.c_float(rect[0]),c.c_float(rect[1]),c.c_float(rect[2]),c.c_float(rect[3]),c.c_float(mass))

    def get_size(self):
        """returns the radius of the sphere"""
        return self.size

    def set_position(self,pos):
        """Sets the position of the object and/or its orientation."""
        pal.lib.sphere_set_position(self.obj,c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]))

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

    def delete(self):
        pal.lib.sphere_remove(self.obj)
        del pal.all_objects[str(self.obj)]
