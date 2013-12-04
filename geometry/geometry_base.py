from pypal import private_globals as pal
import ctypes as c
import weakref
class GeometryBase(pal.PalObject):
    
    """The base class for the bodyless geometies."""
    def get_location():
        """Returns position as a 6 part tuple:(x,y,z)."""

    def getMesh():
        """returns a structure of [points,triangle] consistent to the rest of the engine"""

    def getBody():
        """returns the body this geometry is attachet to, if any"""

