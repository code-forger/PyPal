from pypal import private_globals as _pal
import ctypes as c
import weakref
from ..bodybase import BodyBase
class OrientatedTerrainPlane(BodyBase):
    """ A Static Terrain Plane perpendicular to the given vector. """
    def __init__(self, pos, rot, min_size):
        """
        Parameters:
          pos: ``float[3]`` The x, y, z, position of the terrain.
          rot: ``float[3]`` The rx, ry, rz rotation of the terrain.
          min_size: ``float`` The minimum size for the terrain.
        """
        self._size = min_size
        self.obj = _pal.lib.body_static_orientated_terrain_plane_create(c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),c.c_float(rot[0]),c.c_float(rot[1]),c.c_float(rot[2]),c.c_float(min_size))
        self._body_base = _pal.lib.cast_static_orientated_terrain_plane_body_base(self.obj)

    def __str__(self):
        x, y, z = self.get_position()
        return "An Orientated Terrain Plane at : %.2f, %.2f, %.2f" % (x, y, z)

    def get_size(self):
        """ Returns the size of the object. """
        return self._size