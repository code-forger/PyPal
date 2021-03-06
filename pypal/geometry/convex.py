from pypal import private_globals as _pal
import ctypes as c
import weakref
from geometry import Geometry
class Convex(Geometry):
    """ A Convex Geometry. """
    def __init__(self, pos, points, triangles=None, mass = 1.):
        """
        Parameters:
          pos: ``float[3]`` The x, y, z position for the Convex Geometry.
          points: ``float[x][3]`` The points from which the Convex hull will be calculated.
          triangles: ``float[x][3]`` the triangles to be used when forming the Convex Geometry.
            Note: The triangles might be ignored by the internal physics engine.
          mass: ``float`` The mass of the Convex Geometry.
        """
        CPoints = c.c_float * (len(points) * 3)
        cpoints = CPoints()
        for i in xrange(len(points)):
            for j in xrange(3):
                cpoints[(i*3)+j] = points[i][j]
        if triangles==None:
            self.obj = _pal.lib.geometry_convex_create_no_triangles(c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]),
                                  c.pointer(cpoints),len(points),c.c_float(mass))
        else:
            CTris = c.c_int * len(triangles*3)
            ctris = CTris()
            for i in xrange(len(triangles)):
                for j in xrange(3):
                    ctris[(i*3)+j] = triangles[i][j]

            self.obj = _pal.lib.geometry_convex_create_triangles(c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]),
                                  c.pointer(cpoints),len(points)*3, c.pointer(ctris), len(triangles)*3,c.c_float(mass))

        self.points = points

        self._geometry = _pal.lib.cast_convex_geometry(self.obj)

        self.set_mass(mass)

    def delete(self):
        _pal.lib.geometry_convex_remove(self.obj)
        del _pal.all_objects[str(self.obj)]