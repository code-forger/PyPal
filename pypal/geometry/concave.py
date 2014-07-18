from pypal import private_globals as _pal
import ctypes as c
import weakref
from geometry import Geometry
class Concave(Geometry):
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
        self._geometry = _pal.lib.cast_concave_geometry(self.obj)

        self.set_mass(mass)

    def delete(self):
        _pal.lib.geometry_concave_remove(self.obj)
        del _pal.all_objects[str(self.obj)]