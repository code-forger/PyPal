from pypal import private_globals as _pal
import ctypes as c
import weakref
class Box(_pal.PalObject):
    def __init__(self,pos, size, rotation = [0,0,0],mass = 1):
        self.obj = _pal.lib.geometry_box_create(c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),c.c_float(rotation[0]),c.c_float(rotation[1]),c.c_float(rotation[2]),c.c_float(size[0]),c.c_float(size[1]),c.c_float(size[2]),c.c_float(mass))

    def get_location(self):
        ret = _pal.Mat4x4()
        _pal.lib.geometry_box_get_location(self.obj, ret)
        return [x for x in ret]

    def get_offsett(self):
        ret = _pal.Mat4x4()
        _pal.lib.geometry_box_get_offsett(self.obj, ret)
        return [x for x in ret]

    def get_position(self):
        ret = _pal.Vec3()
        _pal.lib.geometry_box_get_position(self.obj, ret)
        return [x for x in ret]

    def set_margin(self, margin):
        _pal.lib.geometry_box_set_margin(self.obj, c.c_float(margin))

    def get_margin(self):
        _pal.lib.geometry_box_get_margin.restype = c.c_float
        return _pal.lib.geometry_box_get_margin(self.obj)

    def set_mass(self, mass):
        _pal.lib.geometry_box_set_mass(self.obj, c.c_float(mass))

    def get_mass(self):
        _pal.lib.geometry_box_get_mass.restype = c.c_float
        return _pal.lib.geometry_box_get_mass(self.obj)

