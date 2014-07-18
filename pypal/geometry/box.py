from pypal import private_globals as _pal
import ctypes as c
import weakref
from geometry import Geometry
class Box(Geometry):
    def __init__(self,pos, size, rotation = [0,0,0],mass = 1):
        self.obj = _pal.lib.geometry_box_create(c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),c.c_float(rotation[0]),c.c_float(rotation[1]),c.c_float(rotation[2]),c.c_float(size[0]),c.c_float(size[1]),c.c_float(size[2]),c.c_float(mass))
        self._geometry = _pal.lib.cast_box_geometry(self.obj)