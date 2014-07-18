from pypal import private_globals as _pal
import ctypes as c
import weakref
class Capsule(_pal.PalObject):
    def __init__(self,pos, size, rotation = [0,0,0],mass = 1):
        self.obj = _pal.lib.geometry_capsule_create(c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),c.c_float(rotation[0]),c.c_float(rotation[1]),c.c_float(rotation[2]),c.c_float(size[0]),c.c_float(size[1]),c.c_float(mass))

    def get_location(self):
        """ Return the location of the body as a ``float[16]`` matrix. """
        ret = _pal.Mat4x4()
        _pal.lib.geometry_capsule_get_location(self.obj, ret)
        return [x for x in ret]

    def get_offsett(self):
        """ Return the offsett from the body to the geometry as a ``float[16]`` matrix. """
        ret = _pal.Mat4x4()
        _pal.lib.geometry_capsule_get_offsett(self.obj, ret)
        return [x for x in ret]

    def get_position(self):
        """ Return position of the body as the ``float[3]`` x, y, z components. """
        ret = _pal.Vec3()
        _pal.lib.geometry_capsule_get_position(self.obj, ret)
        return [x for x in ret]

    def set_margin(self, margin):
        _pal.lib.geometry_capsule_set_margin(self.obj, c.c_float(margin))

    def get_margin(self):
        _pal.lib.geometry_capsule_get_margin.restype = c.c_float
        return _pal.lib.geometry_capsule_get_margin(self.obj)

    def set_mass(self, mass):
        _pal.lib.geometry_capsule_set_mass(self.obj, c.c_float(mass))

    def get_mass(self):
        _pal.lib.geometry_capsule_get_mass.restype = c.c_float
        return _pal.lib.geometry_capsule_get_mass(self.obj)

