from pypal import private_globals as _pal
import ctypes as c
import weakref
class Character(_pal.PalObject):
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

    def get_location(self):
        """ Return the location of the body as a ``float[16]`` matrix. """
        ret = _pal.Mat4x4()
        _pal.lib.body_character_get_location(self.obj, ret)
        return [x for x in ret]

    def get_position(self):
        """ Return position of the body as the ``float[3]`` x, y, z components. """
        ret = _pal.Vec3()
        _pal.lib.body_character_get_position(self.obj, ret)
        return [x for x in ret]

    def get_group(self):
        """ Return collision group of the body as a ``float``. """
        return _pal.lib.body_character_get_group(self.obj)

    def set_group(self, group):
        return _pal.lib.body_character_set_group(self.obj, c.c_int(group))

    def __str__(self):
        x, y, z = self.get_position()
        return "A Character at : %.2f, %.2f, %.2f" % (x, y, z)

    def walk(self, direction, duration):
        _pal.lib.body_character_walk(self.obj,c.c_float(direction[0]),c.c_float(direction[1]),c.c_float(direction[2]),c.c_float(duration))

    def warp(self, vector):
        _pal.lib.body_character_warp(self.obj,c.c_float(vector[0]),c.c_float(vector[1]),c.c_float(vector[2]))

