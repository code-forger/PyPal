import private_globals as pal
import ctypes as c
import weakref
class GPS(pal.PalObject):
    def _create(self, body, time, latitude, longitude):
        """
        adds a gps to the world
        
        body: The body to connect the gps to
    	time: The initial UTC time total (hours*60*60 + mins*60 + seconds)
	    latitude: The initial latitude position of the sensor (radians, ie: rad(degrees,minutes,seconds))
	    longitude: The initial longitude position of the sensor (radians, ie: rad(degrees,minutes,seconds)) 
        """
        self.obj = pal.lib.create_gps(body.obj, c.c_int(time), c.c_float(latitude), c.c_float(longitude))
        print self.obj

    def get_string(self):
        """returns the angle from north in radiens in the x-y plane"""
        print "This is a dummy output, this function crashes the engine."
        #string = c.c_char()
        #print string.value,self.obj
        #angle = pal.lib.gps_get_string(self.obj,c.byref(string))
        #print string.value,self.obj
        #return string.value
