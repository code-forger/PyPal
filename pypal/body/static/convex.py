from pypal import private_globals as _pal
import ctypes as c
import weakref
from ..bodybase import BodyBase
class StaticConvex(BodyBase):
    """ A Static Rigid Convex Hull """
    def __init__(self, pos, rot, points, triangles=None):
        """
        Parameters:
          pos: ``float[3]`` The x, y, z position for the Convex Body.
          points: ``float[x][3]`` The points from which the convex hull will be calculated.
          triangles: ``float[x][3]`` the triangles to be used when forming the Convex Hull.
            Note: The triangles might be ignored by the internal physics engine.
        """

        CPoints = c.c_float * (len(points) * 3)
        cpoints = CPoints()
        for i in xrange(len(points)):
            for j in xrange(3):
                cpoints[(i*3)+j] = points[i][j]
        if triangles==None:
            self.obj = _pal.lib.body_static_convex_create_no_triangles(c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]),c.c_float(rot[0]), c.c_float(rot[1]), c.c_float(rot[2]),
                                  c.pointer(cpoints),len(points))
        else:
            CTris = c.c_int * len(triangles*3)
            ctris = CTris()
            for i in xrange(len(triangles)):
                for j in xrange(3):
                    ctris[(i*3)+j] = triangles[i][j]

            self.obj = _pal.lib.body_static_convex_create_triangles(c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]),c.c_float(rot[0]), c.c_float(rot[1]), c.c_float(rot[2]),
                                  c.pointer(cpoints),len(points), c.pointer(ctris), len(triangles)*3)

        self.points = points
        self._body_base = _pal.lib.cast_static_convex_body_base(self.obj)


    def delete(self):
        _pal.lib.body_static_convex_remove(self.obj)
        del _pal.all_objects[str(self.obj)]

    def __str__(self):
        x, y, z = self.get_position()
        return "A Static Convex at : %.2f, %.2f, %.2f" % (x, y, z)

    def get_size(self):
        """ Returns the size of the object in a 3 part tuple. """
        return self._size