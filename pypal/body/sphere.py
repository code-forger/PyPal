from pypal import private_globals as _pal
import ctypes as c
import weakref
from body import Body
class Sphere(Body):
    def __init__(self, pos, size, mass = 1.):
        """
        constructs a sphere and adds it to the world
        
        pos: a 3 part tuple with x,y,z.
        size: a 3 part tuple with width, height, depth
        mass: the mass of the object, if mass is specified it will be used.
        """
        self._size = size
        self.obj = _pal.lib.body_sphere_create(c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),c.c_float(size[0]),c.c_float(mass))
        self._body_base = _pal.lib.cast_sphere_body_base(self.obj)
        self._body = _pal.lib.cast_sphere_body(self.obj)

    def __str__(self):
        x, y, z = self.get_position()
        return "A Sphere at : %.2f, %.2f, %.2f" % (x, y, z)

    def get_size(self):
        """returns the size of the object in a 3 part tuple"""
        return self._size