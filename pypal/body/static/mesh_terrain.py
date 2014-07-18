from pypal import private_globals as _pal
import ctypes as c
import weakref
class MeshTerrain(_pal.PalObject):
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

    def get_location(self):
        """ Return the location of the body as a ``float[16]`` matrix. """
        ret = _pal.Mat4x4()
        _pal.lib.body_static_mesh_terrain_get_location(self.obj, ret)
        return [x for x in ret]

    def get_position(self):
        """ Return position of the body as the ``float[3]`` x, y, z components. """
        ret = _pal.Vec3()
        _pal.lib.body_static_mesh_terrain_get_position(self.obj, ret)
        return [x for x in ret]

    def set_material(self, material):
        _pal.lib.body_static_mesh_terrain_set_material(self.obj, material.obj)

    def get_group(self):
        """ Return collision group of the body as a ``float``. """
        return _pal.lib.body_static_mesh_terrain_get_group(self.obj)

    def set_group(self, group):
        return _pal.lib.body_static_mesh_terrain_set_group(self.obj, c.c_int(group))

    def __str__(self):
        x, y, z = self.get_position()
        return "A Mesh Terrain at : %.2f, %.2f, %.2f" % (x, y, z)

    def get_size(self):
        """returns the size of the object in a 3 part tuple"""
        return self._size