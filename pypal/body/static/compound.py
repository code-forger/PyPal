from pypal import private_globals as _pal
import ctypes as c
import weakref
from ..bodybase import BodyBase
class StaticCompound(BodyBase):
    """ A Static Rigid Body with no initial geometry """
    def __init__(self, pos):
        """
        Parameters:
          pos: ``float[3]`` The x, y, z position of the Box.
        """
        self.obj = _pal.lib.body_static_compound_create(c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]))
        self._body_base = _pal.lib.cast_static_compound_body_base(self.obj)

    def __str__(self):
        x, y, z = self.get_position()
        return "A Static Compound Body at : %.2f, %.2f, %.2f" % (x, y, z)

    def add_box(self, pos, size, rotation=[0,0,0]):
        """
        Adds a box geometry to the compound body.

        Parameters:
          pos: ``float[3]`` The x, y, z, positional offsett for the new geometry.
          size: ``float[3]`` The width, height, depth, for the new geometry.
          rotation: ``float[3]`` The rx, ry, rz, rotation for the new geometry.
        """
        _pal.lib.body_static_compound_add_box(self.obj, c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]),
                                                        c.c_float(rotation[0]), c.c_float(rotation[1]), c.c_float(rotation[2]),
                                                        c.c_float(size[0]), c.c_float(size[1]), c.c_float(size[2]))

    def add_sphere(self, pos, size, rotation=(0,0,0)):
        """
        Adds a sphere geometry to the compound body.

        Parameters:
          pos: ``float[3]`` The x, y, z, positional offsett for the new geometry.
          size: ``float[1]`` The radius for the new geometry.
          rotation: ``float[3]`` The rx, ry, rz, rotation for the new geometry.
        """
        _pal.lib.body_static_compound_add_sphere(self.obj, c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]),
                                                           c.c_float(rotation[0]), c.c_float(rotation[1]), c.c_float(rotation[2]), 
                                                           c.c_float(size[0]))

    def add_capsule(self, pos, size, rotation=(0,0,0)):
        """
        Adds a sphere geometry to the compound body.

        Parameters:
          pos: ``float[3]`` The x, y, z, positional offsett for the new geometry.
          size: ``float[2]`` The radius, height, for the new geometry.
          rotation: ``float[3]`` The rx, ry, rz, rotation for the new geometry.
        """
        _pal.lib.body_static_compound_add_capsule(self.obj, c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]),
                                                            c.c_float(rotation[0]), c.c_float(rotation[1]), c.c_float(rotation[2]),
                                                            c.c_float(size[0]), c.c_float(size[1]))

    def add_convex(self, pos, points, rotation=(0,0,0), mass=1.):
        """
        Adds a sphere geometry to the compound body.

        Parameters:
          pos: ``float[3]`` The x, y, z, positional offsett for the new geometry.
          points: ``float[x][3]`` The points from which the convex hull will be calculated.
          rotation: ``float[3]`` The rx, ry, rz rotation for the new geometry.
        """
        CPoints = c.c_float * (len(points) * 3)
        cpoints = CPoints()
        for i in xrange(len(points)):
            for j in xrange(3):
                cpoints[(i*3)+j] = points[i][j]
        _pal.lib.body_static_compound_add_convex(self.obj, c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]), c.c_float(rotation[0]), c.c_float(rotation[1]), c.c_float(rotation[2]), c.pointer(cpoints),len(points)*3)

    def finalize(self):
        """
        Finalize the body.

        You must call this function after all geometries have been added and before the physics engine is updated.
        """
        _pal.lib.body_static_compound_finalize(self.obj)
