from pypal import private_globals as _pal
import ctypes as c
import weakref
class StaticSphere(_pal.PalObject):
    def __init__(self, pos, size):
        """
        constructs a static sphere and adds it to the world
        
        pos: a 3 part tuple with x,y,z.
        size: a 3 part tuple with width, height, depth
        """
        self._size = size
        self.obj = _pal.lib.body_static_sphere_create(c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),c.c_float(size[0]))

    def get_location(self):
        ret = _pal.Mat4x4()
        _pal.lib.body_static_sphere_get_location(self.obj, ret)
        return [x for x in ret]

    def get_position(self):
        ret = _pal.Vec3()
        _pal.lib.body_static_sphere_get_position(self.obj, ret)
        return [x for x in ret]

    def set_material(self, material):
        _pal.lib.body_static_sphere_set_material(self.obj, material.obj)

    def get_group(self):
        return _pal.lib.body_static_sphere_get_group(self.obj)

    def set_group(self, group):
        return _pal.lib.body_static_sphere_set_group(self.obj, c.c_int(group))

    def __str__(self):
        x, y, z = self.get_position()
        return "A Static Sphere at : %.2f, %.2f, %.2f" % (x, y, z)

    def get_size(self):
        """returns the size of the object in a 3 part tuple"""
        return self._size