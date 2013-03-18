from private_globals import *
from bodybase import BodyBase
class Terrain(BodyBase):
    """ a simple terrain object """
    def __init__(self,pos,min_size):
        """
        pos: position of the plane
        min_size: the minimumsize of the plane
        """
        pal_lib.create_terrain_plane(c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),c.c_float(min_size))
    
        pass
