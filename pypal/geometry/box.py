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
