import private_globals as pal
import ctypes as c
import weakref
class PSD(pal.PalObject):
    def __init__(self, body, pos, axis):
        """
        adds a PSD to the world
        
        body: The body to connect the Inclinometer to
        pos: The position of the ray
        axis:  The axis which the angle is measured about w.r.t. the body
        """
        self.obj = pal.lib.create_psd(body.obj, c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2])
                                                       , c.c_float(axis[0]), c.c_float(axis[1]), c.c_float(axis[2]))

    def get_distance(self):
        """returns the angle from north in radiens in the x-y plane"""
        pal.lib.psd_get_distance.restype = c.c_float
        distance = pal.lib.psd_get_distance(self.obj)
        return distance
