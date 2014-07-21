from pypal import private_globals as _pal
import ctypes as c
import weakref
class Compass(_pal.PalObject):
    """ A compass. """
    def __init__(self, body, north):
        """
        Parameters:
          body: ``pypal.body`` The dynamic body to connect the compass to.
          north: ``float[3]`` a unit vector describing north.
        """
        self.obj = _pal.lib.sensor_compass_create(body._body, c.c_float(north[0]), c.c_float(north[1]), c.c_float(north[2]))

    def get_angle(self):
        """ Returns the angle from north in the x-y plane. """
        _pal.lib.sensor_compass_get_angle.restype = c.c_float
        return _pal.lib.sensor_compass_get_angle(self.obj)
