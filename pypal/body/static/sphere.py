from pypal import private_globals as _pal
import ctypes as c
import weakref
from ..bodybase import BodyBase
class StaticSphere(BodyBase):
    """ A Static Rigid Sphere """
    def __init__(self, pos, size):
        """
        Parameters:
          pos: ``float[3]`` The x, y, z position of the Sphere.
          size: ``float[1]`` The radius, of the Sphere.
        """
        self._size = size
        self.obj = _pal.lib.body_static_sphere_create(c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),c.c_float(size[0]))
        self._body_base = _pal.lib.cast_static_sphere_body_base(self.obj)

    def __str__(self):
        x, y, z = self.get_position()
        return "A Static Sphere at : %.2f, %.2f, %.2f" % (x, y, z)

    def get_size(self):
        """ Returns the size of the object in a 3 part tuple. """
        return self._size