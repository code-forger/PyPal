import private_globals as pal
import ctypes as c
import weakref
class GPS(pal.PalObject):
    def __init__(self, body, time, latitude, longitude):
        """
        adds a gps to the world
        
        body: The body to connect the gps to
    	time: The initial UTC time total (hours*60*60 + mins*60 + seconds)
	    latitude: The initial latitude position of the sensor (radians, ie: rad(degrees,minutes,seconds))
	    longitude: The initial longitude position of the sensor (radians, ie: rad(degrees,minutes,seconds)) 
        """
        self.obj = pal.lib.create_gps(body.obj, c.c_int(time), c.c_float(latitude), c.c_float(longitude))

    def get_string(self):
        """returns the angle from north in radiens in the x-y plane"""
        string = pal.lib.gps_create_string()
        pal.lib.gps_get_string(self.obj,string)
        constructed = c.c_char_p(string)
        return constructed.value
