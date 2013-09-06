from pypalgame import private_globals as pal
import ctypes as c
import weakref
class Compass(pal.PalObject):
    def __init__(self, body, north):
        """
        adds a compass to the world
        
        body: The body to connect the compass to
        north: a unit vector describing north
        """
        self.obj = pal.lib.create_compass(body.obj, c.c_float(north[0]), c.c_float(north[1]), c.c_float(north[2]))

    def get_angle(self):
        """returns the angle from north in radiens in the x-y plane"""
        pal.lib.compass_get_angle.restype = c.c_float
        angle = pal.lib.compass_get_angle(self.obj)
        return angle
