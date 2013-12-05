from ..private_globals import *
import math
class GeometryBase(PalObject):
    
    """The base class for the bodyless geometies."""
    def get_location(self):
        """Returns position as a 6 part tuple:(x,y,z,rx,ry,rz)."""
        pos = [c.c_float() for x in range(6)]
        lib.geometry_get_primative_location(self.obj,c.c_char(self.typechar),c.byref(pos[0]),c.byref(pos[1]),c.byref(pos[2]),c.byref(pos[3]),c.byref(pos[4]),c.byref(pos[5]))
        return [p.value for p in pos]

    def getMesh():
        """returns a structure of [points,triangle] consistent to the rest of the engine"""

    def getBody():
        """returns the body this geometry is attachet to, if any"""

