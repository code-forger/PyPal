from pypal import private_globals as _pal
import ctypes as c
import weakref
class PSD(_pal.PalObject):
    def __init__(self, body, pos, axis):
        """
        adds a PSD to the world
        
        body: The body to connect the Inclinometer to
        pos: The position of the ray
        axis:  The axis which the angle is measured about w.r.t. the body
        """
        self.obj = _pal.lib.sensor_psd_create(body.obj, c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2])
                                                       , c.c_float(axis[0]), c.c_float(axis[1]), c.c_float(axis[2]))

    def get_distance(self):
        """returns the angle from north in radiens in the x-y plane"""
        _pal.lib.sensor_psd_get_distance.restype = c.c_float
        return _pal.lib.sensor_psd_get_distance(self.obj)
