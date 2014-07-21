from pypal import private_globals as _pal
import ctypes as c
import weakref
class Spherical(_pal.PalObject):
    """ A link that connects two objects spherically."""
    def __init__(self,parent,child,pos,collide):
        """
        Parameters:
          parent: ``pypal.body`` The first body who is part of the link.
          child: ``pypal.body`` The second body who is part of the link.
          pos: ``float[3]`` The center of the link.
          collide: ``bool`` Weather or not the bodies involved in the link should coolide with each other.
        """
        self.obj = _pal.lib.link_spherical_create(parent.obj,child.obj,c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),c.c_bool(collide))


    def set_limits(self,cone,twist):
        """
        Sets the movement limits of the link.
        
        Parameters:
          cone: ``float`` Limits the rotational movement to a cone.
          twist: ``float`` Limits the twisting of the link.
        """
        _pal.lib.link_spherical_set_limits(self.obj,c.c_float(cone),c.c_float(twist))

    def get_feedback():
        """ Returns the magnitude of the force on the link. """
        _pal.lib.link_spherical_get_feedback.restype = c.c_float
        return _pal.lib.link_spherical_get_feedback(self.obj)