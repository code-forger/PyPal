from pypal import private_globals as _pal
import ctypes as c
import weakref
class Geometry(_pal.PalObject):
    def get_location(self):
        """ Return the location of the body as a ``float[16]`` matrix. """
        ret = _pal.Mat4x4()
        _pal.lib.geometry_get_location(self._geometry, ret)
        return [x for x in ret]

    def get_offsett(self):
        """ Return the offsett from the body to the geometry as a ``float[16]`` matrix. """
        ret = _pal.Mat4x4()
        _pal.lib.geometry_get_offsett(self._geometry, ret)
        return [x for x in ret]

    def get_position(self):
        """ Return position of the body as the ``float[3]`` x, y, z components. """
        ret = _pal.Vec3()
        _pal.lib.geometry_get_position(self._geometry, ret)
        return [x for x in ret]

    def set_margin(self, margin):
        _pal.lib.geometry_set_margin(self._geometry, c.c_float(margin))

    def get_margin(self):
        _pal.lib.geometry_get_margin.restype = c.c_float
        return _pal.lib.geometry_get_margin(self._geometry)

    def set_mass(self, mass):
        _pal.lib.geometry_set_mass(self._geometry, c.c_float(mass))

    def get_mass(self):
        _pal.lib.geometry_get_mass.restype = c.c_float
        return _pal.lib.geometry_get_mass(self._geometry)

