from pypal import private_globals as _pal
import ctypes as c
import weakref
class GPS(_pal.PalObject):
    """ A GPS Sensor. """
    def __init__(self, body, time, latitude, longitude):
        """
        Parameters:
          body: ``pypal.body`` The dynamic body to connect the gps to.
    	  time: ``float`` The initial UTC time total (hours*60*60 + mins*60 + seconds).
	      latitude: ``float`` The initial latitude position of the sensor (radians, ie: rad(degrees,minutes,seconds)).
	      longitude: ``float`` The initial longitude position of the sensor (radians, ie: rad(degrees,minutes,seconds)) .
        """
        self.obj = _pal.lib.sensor_gps_create(body._body, c.c_int(time), c.c_float(latitude), c.c_float(longitude))

    def get_string(self):
        """ Returns the gps string. """
        string = _pal.lib.sensor_gps_create_string()
        _pal.lib.sensor_gps_get_string(self.obj,string)
        return c.c_char_p(string).value
