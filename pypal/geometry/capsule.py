from pypal import private_globals as _pal
import ctypes as c
import weakref
from geometry import Geometry
class Capsule(Geometry):
    """ A Capsule Geometry. """
    def __init__(self, pos, size, rotation=[0,0,0], mass=1):
        """
        Parameters:
          pos: ``float[3]`` The x, y, z, position of the Capsule.
          size: ``float[2]`` The radius, height of the Capsule.
          rotation: ``float[3]`` The rx, ry, rz rotation of the Capsule.
          mass: ``float`` The mass of the Capsule.
        """
        self.obj = _pal.lib.geometry_capsule_create(c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),c.c_float(rotation[0]),c.c_float(rotation[1]),c.c_float(rotation[2]),c.c_float(size[0]),c.c_float(size[1]),c.c_float(mass))
        self._geometry = _pal.lib.cast_capsule_geometry(self.obj)