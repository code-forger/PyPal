from pypal import private_globals as _pal
import ctypes as c
import weakref
from ..bodybase import BodyBase
class HeightMapTerrain(BodyBase):
    """ A Static Heightmaped Terrain. """
    def __init__(self, pos, size, chunks, height_map):
        """
        Parameters:
          pos: ``float[3]`` The x, y, z, position of the Terrain.
          size: ``float[2]`` The x, z size of the Terrain.
          chunks: ``float[2]`` The number of heightmap points x, z.
          height_map: ``float[chunks[0]][chunks[1]]`` the y values for the center of each chunk.
        """
        self._size = size
        points = c.c_float * (chunks[0] * chunks[1])
        points = points()
        for x in range(chunks[0]):
            for y in range(chunks[1]):
                points[(x*chunks[0])+(y)] = c.c_float(height_map[x][y])
        self.obj = _pal.lib.body_static_heightmap_terrain_create(c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),
                                                    c.c_float(size[0]),c.c_float(size[1]),
                                                    c.c_int(chunks[0]),c.c_int(chunks[1]),
                                                    c.pointer(points))
        self._body_base = _pal.lib.cast_static_heightmap_terrain_body_base(self.obj)

    def __str__(self):
        x, y, z = self.get_position()
        return "A Height Map Terrain at : %.2f, %.2f, %.2f" % (x, y, z)

    def get_size(self):
        """ Returns the size of the object in a 2 part tuple. """
        return self._size