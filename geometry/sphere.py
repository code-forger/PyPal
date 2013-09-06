from pypalgame import private_globals as pal
import ctypes as c
import weakref
from geometry_base import GeometryBase
class Sphere(GeometryBase):
    def __init__(self,rect, rotation = [0,0,0],mass = 1):
        """
        constructs a Sphere
        
        rect: a 4 part tuple with x,y,z,radius.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        """
        self.obj = pal.lib.create_geometry_sphere(c.c_float(rect[0]),c.c_float(rect[1]),c.c_float(rect[2]),c.c_float(rotation[0]),c.c_float(rotation[1]),c.c_float(rotation[2]),c.c_float(rect[3]),c.c_float(mass))

    def delete(self):
        pal.lib.sphere_geometry_remove(self.obj)
        del pal.all_objects[str(self.obj)]
