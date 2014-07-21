from pypal import private_globals as _pal
import ctypes as c
import weakref
class Inclinometer(_pal.PalObject):
    """ An Inclinometer Sensor. """
    def __init__(self, body, axis, up, gravity):
        """
        Parameters:
          body: ``pypal.body`` The dynamic body to connect the Inclinometer to.
          axis: ``float[3]`` The axis which the angle is measured about.
          up: ``float[3]`` The up axis w.r.t the body.
          gravity: ``float[3]`` The gravity axis or the world.
        """
        self.obj = _pal.lib.sensor_inclinometer_create(body._body, c.c_float(axis[0]), c.c_float(axis[1]), c.c_float(axis[2])
                                                       , c.c_float(up[0]), c.c_float(up[1]), c.c_float(up[2])
                                                       , c.c_float(gravity[0]), c.c_float(gravity[1]), c.c_float(gravity[2]))

    def get_angle(self):
        """ Returns the inclination of the current body. """
        _pal.lib.sensor_inclinometer_get_angle.restype = c.c_float
        return _pal.lib.sensor_inclinometer_get_angle(self.obj)
