from pypal import private_globals as _pal
import ctypes as c
import weakref
from ..bodybase import BodyBase
class TerrainPlane(BodyBase):
    """ A Static Terrain Plane parralell to the x, z axis. """
    def __init__(self, pos, min_size):
        """
        Parameters:
          pos: ``float[3]`` The x, y, z, position of the terrain.
          min_size: ``float`` The minimum size of the terrain.
        """
        self._size = min_size
        self.obj = _pal.lib.body_static_terrain_plane_create(c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),c.c_float(min_size))
        self._body_base = _pal.lib.cast_static_terrain_plane_body_base(self.obj)

    def __str__(self):
        x, y, z = self.get_position()
        return "A Terrain Plane at : %.2f, %.2f, %.2f" % (x, y, z)

    def get_size(self):
        """ Returns the size of the object. """
        return self._size