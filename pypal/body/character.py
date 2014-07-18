from pypal import private_globals as _pal
import ctypes as c
import weakref
from body import Body
class Character(Body):
    def __init__(self,rect,mass=1):
        """
        constructs a character and adds it to the world
        
        rect: a 5 part tuple with x,y,z,radius,height
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        static: used to create this object static, if static is true, mass will be ignored
        """
        self.obj = _pal.lib.body_character_create(c.c_float(rect[0]),c.c_float(rect[1]),c.c_float(rect[2]),c.c_float(rect[3]),c.c_float(rect[4]))
        self._body_base = _pal.lib.cast_character_body_base(self.obj)
        self._body = _pal.lib.cast_character_body(self.obj)

    def __str__(self):
        x, y, z = self.get_position()
        return "A Character at : %.2f, %.2f, %.2f" % (x, y, z)

    def walk(self, direction, duration):
        _pal.lib.body_character_walk(self.obj,c.c_float(direction[0]),c.c_float(direction[1]),c.c_float(direction[2]),c.c_float(duration))

    def warp(self, vector):
        _pal.lib.body_character_warp(self.obj,c.c_float(vector[0]),c.c_float(vector[1]),c.c_float(vector[2]))

