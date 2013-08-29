import private_globals as pal
import ctypes as c
import weakref
class Inclinometer(pal.PalObject):
    def __init__(self, body, axis, up, gravity):
        """
        adds a Inclinometer to the world
        
        body: The body to connect the Inclinometer to
        axis: The axis which the angle is measured about w.r.t. the body
        up: The up axis w.r.t the body (x)
        g: The gravity axis w.r.t the world (x)
        """
        self.obj = pal.lib.create_inclinometer(body.obj, c.c_float(axis[0]), c.c_float(axis[1]), c.c_float(axis[2])
                                                       , c.c_float(up[0]), c.c_float(up[1]), c.c_float(up[2])
                                                       , c.c_float(gravity[0]), c.c_float(gravity[1]), c.c_float(gravity[2]))

    def get_angle(self):
        """returns the angle from north in radiens in the x-y plane"""
        pal.lib.inclinometer_get_angle.restype = c.c_float
        angle = pal.lib.inclinometer_get_angle(self.obj)
        return angle
