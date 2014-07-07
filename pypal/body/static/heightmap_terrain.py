from pypal import private_globals as _pal
import ctypes as c
import weakref
class HeightMapTerrain(_pal.PalObject):
    def __init__(self,pos,size,chunks,height_map):
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

    def get_location(self):
        ret = _pal.Mat4x4()
        _pal.lib.body_static_heightmap_terrain_get_location(self.obj, ret)
        return [x for x in ret]

    def get_position(self):
        ret = _pal.Vec3()
        _pal.lib.body_static_heightmap_terrain_get_position(self.obj, ret)
        return [x for x in ret]

    def get_group(self):
        return _pal.lib.body_static_heightmap_terrain_get_group(self.obj)

    def set_group(self, group):
        return _pal.lib.body_static_heightmap_terrain_set_group(self.obj, c.c_int(group))

    def __str__(self):
        x, y, z = self.get_position()
        return "A Height Map Terrain at : %.2f, %.2f, %.2f" % (x, y, z)

    def get_size(self):
        """returns the size of the object in a 3 part tuple"""
        return self._size