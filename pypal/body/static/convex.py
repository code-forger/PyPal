from pypal import private_globals as _pal
import ctypes as c
import weakref
class StaticConvex(_pal.PalObject):
    def __init__(self, pos, rot, points, triangles=None):
        """
        constructs a static convex and adds it to the world
        
        pos: a 3 part tuple with x,y,z.
        size: a 3 part tuple with width, height, depth
        """

        CPoints = c.c_float * (len(points) * 3)
        cpoints = CPoints()
        for i in xrange(len(points)):
            for j in xrange(3):
                cpoints[(i*3)+j] = points[i][j]
        if triangles==None:
            self.obj = _pal.lib.body_static_convex_create_no_triangles(c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]),c.c_float(rot[0]), c.c_float(rot[1]), c.c_float(rot[2]),
                                  c.pointer(cpoints),len(points)*3)
        else:
            CTris = c.c_int * len(triangles*3)
            ctris = CTris()
            for i in xrange(len(triangles)):
                for j in xrange(3):
                    ctris[(i*3)+j] = triangles[i][j]

            self.obj = _pal.lib.body_static_convex_create_triangles(c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]),c.c_float(rot[0]), c.c_float(rot[1]), c.c_float(rot[2]),
                                  c.pointer(cpoints),len(points)*3, c.pointer(ctris), len(triangles)*3)

        self.points = points

    def delete(self):
        _pal.lib.body_static_convex_remove(self.obj)
        del _pal.all_objects[str(self.obj)]

    def get_location(self):
        ret = _pal.Mat4x4()
        _pal.lib.body_static_convex_get_location(self.obj, ret)
        return [x for x in ret]

    def get_position(self):
        ret = _pal.Vec3()
        _pal.lib.body_static_convex_get_position(self.obj, ret)
        return [x for x in ret]

    def get_group(self):
        return _pal.lib.body_static_convex_get_group(self.obj)

    def set_group(self, group):
        return _pal.lib.body_static_convex_set_group(self.obj, c.c_int(group))

    def __str__(self):
        x, y, z = self.get_position()
        return "A Static Convex at : %.2f, %.2f, %.2f" % (x, y, z)

    def get_size(self):
        """returns the size of the object in a 3 part tuple"""
        return self._size