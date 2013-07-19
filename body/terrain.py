import private_globals as pal
import ctypes as c
import weakref
from bodybase import BodyBase
class Terrain(BodyBase):
    """ a simple terrain object """
    def __new__(cls,pos,min_size):
        """
        pos: position of the plane
        min_size: the minimumsize of the plane
        """
        terrain = super(Terrain,cls).__new__(cls)
        terrain._create(pos,min_size)
        pal.all_objects[str(terrain.obj)] = terrain
        return weakref.proxy(terrain)

    def _create(self,pos,min_size):#TESTED
        self.obj = pal.lib.create_terrain_plane(c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),c.c_float(min_size))

    def delete(self):
        pal.lib.terrain_remove(self.obj)
        del pal.all_objects[str(self.obj)]
