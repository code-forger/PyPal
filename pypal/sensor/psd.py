from pypal import private_globals as _pal
import ctypes as c
import weakref
class PSD(_pal.PalObject):
    """ A PSD Sensor that casts a ray to determin the distance to the closest object in a specific direction. """
    def __init__(self, body, pos, direction):
        """
        Paramters:
          body: ``pypal.body`` The dynamic body to connect the PSD to.
          pos: ``float[3]`` The x, y, z, starting position of the ray.
          direction: ``float[3]`` The rx, ry, rz, direction the ray is to be cast in.
        """
        self.obj = _pal.lib.sensor_psd_create(body._body, c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2])
                                                       , c.c_float(direction[0]), c.c_float(direction[1]), c.c_float(direction[2]))

    def get_distance(self):
        """ Returns the distance to the nearest object. """
        _pal.lib.sensor_psd_get_distance.restype = c.c_float
        return _pal.lib.sensor_psd_get_distance(self.obj)
