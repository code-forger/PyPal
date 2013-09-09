from pypalgame import private_globals as pal
import ctypes as c
import weakref
from geometry_base import GeometryBase
class Box(GeometryBase):
    def __init__(self,rect, rotation = [0,0,0],mass = 1):
        self.obj = pal.lib.create_geometry_box(c.c_float(rect[0]),c.c_float(rect[1]),c.c_float(rect[2]),c.c_float(rotation[0]),c.c_float(rotation[1]),c.c_float(rotation[2]),c.c_float(rect[3]),c.c_float(rect[4]),c.c_float(rect[5]),c.c_float(mass))
