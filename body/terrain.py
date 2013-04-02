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
        pal.all_objects[str(pal.all_next)] = terrain
        pal.lib.body_set_data(terrain.obj,pal.all_next)
        pal.all_next += 1
        return weakref.proxy(terrain)

    def _create(self,pos,min_size):#TESTED
        """
        pos: position of the plane
        min_size: the minimumsize of the plane
        """
        self.obj = pal.lib.create_terrain_plane(c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),c.c_float(min_size))

    def delete(self):
        x = pal.lib.body_get_data(self.obj)
        pal.lib.body_clear_data(self.obj)
        pal.lib.terrain_remove(self.obj)
        del pal.all_objects[str(x)]
