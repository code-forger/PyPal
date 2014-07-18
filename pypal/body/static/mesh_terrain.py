from pypal import private_globals as _pal
import ctypes as c
import weakref
from ..bodybase import BodyBase
class MeshTerrain(BodyBase):
    def __init__(self, pos, points, triangles):
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
        CTris = c.c_int * len(triangles*3)
        ctris = CTris()
        for i in xrange(len(triangles)):
            for j in xrange(3):
                ctris[(i*3)+j] = triangles[i][j]

        self.obj = _pal.lib.body_static_mesh_terrain_create(c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]),
                              c.pointer(cpoints),len(points)*3, c.pointer(ctris), len(triangles)*3)

        self.points = points
        self._body_base = _pal.lib.cast_static_mesh_terrain_body_base(self.obj)

    def __str__(self):
        x, y, z = self.get_position()
        return "A Mesh Terrain at : %.2f, %.2f, %.2f" % (x, y, z)

    def get_size(self):
        """returns the size of the object in a 3 part tuple"""
        return self._size