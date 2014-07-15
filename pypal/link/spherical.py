from pypal import private_globals as _pal
import ctypes as c
import weakref
class Spherical(_pal.PalObject):
    """a link that connects two objects rotationally"""
    def __init__(self,parent,child,pos,collide):
        self.obj = _pal.lib.link_spherical_create(parent.obj,child.obj,c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),c.c_bool(collide))


    def set_limits(self,cone,twist):
        """
        sets the movement limits of the link
        
        cone: limits the rotational movement to a cone specified in radiens
        twist: limits the twisting of the link specified in radiens
        """
        _pal.lib.link_spherical_set_limits(self.obj,c.c_float(cone),c.c_float(twist))

    def get_feedback():
        _pal.lib.link_spherical_get_feedback.restype = c.c_float
        return _pal.lib.link_spherical_get_feedback(self.obj)