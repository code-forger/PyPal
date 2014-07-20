from pypal import private_globals as _pal
import ctypes as c
import weakref
from body import Body
class Sphere(Body):
    """ A Ridgid Dynamic Sphere. """
    def __init__(self, pos, size, mass = 1.):
        """
        Parameters:
          pos: ``float[3]`` The x, y, z, position of the body.
          size: ``float[1]`` Radius of the body.
          mass: ``float`` The mass of the object.
        """
        self._size = size
        self.obj = _pal.lib.body_sphere_create(c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),c.c_float(size[0]),c.c_float(mass))
        self._body_base = _pal.lib.cast_sphere_body_base(self.obj)
        self._body = _pal.lib.cast_sphere_body(self.obj)

    def __str__(self):
        x, y, z = self.get_position()
        return "A Sphere at : %.2f, %.2f, %.2f" % (x, y, z)

    def get_size(self):
        """ Returns the size of the object in a 3 part tuple. """
        return self._size