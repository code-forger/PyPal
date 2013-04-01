import private_globals as pal
import ctypes as c
import weakref
from bodybase import BodyBase
class HeightMapTerrain(BodyBase):
    """ an height map terrain object """
    @classmethod
    def create(self,pos,size,chunks,height_map):
        """
        pos: position of the plane
        min_size: the minimumsize of the plane
        """
        terrain = HeightMapTerrain(pos,size,chunks,height_map)
        pal.all_objects[str(pal.all_next)] = terrain
        pal.lib.body_set_data(terrain.obj,pal.all_next)
        pal.all_next += 1
        return weakref.proxy(terrain)

    def __init__(self,pos,size,chunks,height_map):#TESTED
        """
        pos: position of the plane
        min_size: the minimumsize of the plane
        """
        points = c.c_float * (chunks[0] * chunks[1])
        points = points()
        for x in range(chunks[0]):
            for y in range(chunks[1]):
                points[(x*chunks[0])+(y)] = c.c_float(height_map[x][y])
        self.obj = pal.lib.create_terrain_heightmap(c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),
                                                    c.c_float(size[0]),c.c_float(size[1]),
                                                    c.c_int(chunks[0]),c.c_int(chunks[1]),
                                                    c.pointer(points))

    def delete(self):
        x = pal.lib.body_get_data(self.obj)
        if self in notified_objects:
            notify_objects.remove(self)
        pal.lib.terrain_heightmap_remove(self.obj)
        del pal.all_objects[str(x)]
