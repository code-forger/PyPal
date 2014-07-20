from pypal import private_globals as _pal
import ctypes as c
import weakref
from body import Body
class Convex(Body):
    def __init__(self, pos, points, triangles=None, mass = 1.):
        """
        constructs a convex and adds it to the world
        
        pos: a 3 part tuple with x,y,z.
        size: a 3 part tuple with width, height, depth
        mass: the mass of the object, if mass is specified it will be used.
        """
        CPoints = c.c_float * (len(points) * 3)
        cpoints = CPoints()
        for i in xrange(len(points)):
            for j in xrange(3):
                cpoints[(i*3)+j] = points[i][j]
        if triangles==None:
            self.obj = _pal.lib.body_convex_create_no_triangles(c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]),
                                  c.pointer(cpoints),len(points),c.c_float(mass))
        else:
            CTris = c.c_int * len(triangles*3)
            ctris = CTris()
            for i in xrange(len(triangles)):
                for j in xrange(3):
                    ctris[(i*3)+j] = triangles[i][j]

            self.obj = _pal.lib.body_convex_create_triangles(c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]),
                                  c.pointer(cpoints),len(points), c.pointer(ctris), len(triangles)*3,c.c_float(mass))

        self.points = points
        self._body_base = _pal.lib.cast_convex_body_base(self.obj)
        self._body = _pal.lib.cast_convex_body(self.obj)

    def delete(self):
        _pal.lib.body_convex_remove(self.obj)
        del _pal.all_objects[str(self.obj)]

    def __str__(self):
        x, y, z = self.get_position()
        return "A ConvexBody at : %.2f, %.2f, %.2f" % (x, y, z)