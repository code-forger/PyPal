from pypal import private_globals as _pal
import ctypes as c
import weakref
class Concave(_pal.PalObject):
    def __init__(self, pos, points, triangles, mass = 1.):
        CPoints = c.c_float * (len(points) * 3)
        cpoints = CPoints()
        for i in xrange(len(points)):
            for j in xrange(3):
                cpoints[(i*3)+j] = points[i][j]

        CTris = c.c_int * len(triangles*3)
        ctris = CTris()
        for i in xrange(len(triangles)):
            for j in xrange(3):
                ctris[(i*3)+j] = triangles[i][j]

        self.obj = _pal.lib.geometry_concave_create(c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]),
                              c.pointer(cpoints),len(points)*3, c.pointer(ctris), len(triangles)*3,c.c_float(mass))

        self.points = points

        self.set_mass(mass)

    def delete(self):
        _pal.lib.geometry_concave_remove(self.obj)
        del _pal.all_objects[str(self.obj)]

    def get_location(self):
        """ Return the location of the body as a ``float[16]`` matrix. """
        ret = _pal.Mat4x4()
        _pal.lib.geometry_concave_get_location(self.obj, ret)
        return [x for x in ret]

    def get_offsett(self):
        """ Return the offsett from the body to the geometry as a ``float[16]`` matrix. """
        ret = _pal.Mat4x4()
        _pal.lib.geometry_concave_get_offsett(self.obj, ret)
        return [x for x in ret]

    def get_position(self):
        """ Return position of the body as the ``float[3]`` x, y, z components. """
        ret = _pal.Vec3()
        _pal.lib.geometry_concave_get_position(self.obj, ret)
        return [x for x in ret]

    def set_margin(self, margin):
        _pal.lib.geometry_concave_set_margin(self.obj, c.c_float(margin))

    def get_margin(self):
        _pal.lib.geometry_concave_get_margin.restype = c.c_float
        return _pal.lib.geometry_concave_get_margin(self.obj)

    def set_mass(self, mass):
        _pal.lib.geometry_concave_set_mass(self.obj, c.c_float(mass))

    def get_mass(self):
        _pal.lib.geometry_concave_get_mass.restype = c.c_float
        return _pal.lib.geometry_concave_get_mass(self.obj)

