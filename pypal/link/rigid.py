from pypal import private_globals as _pal
import ctypes as c
import weakref
class Rigid(_pal.PalObject):
    """ A link that connects two objects rigidly. """
    def __init__(self,parent,child,collide):
        """
        Parameters:
          parent: ``pypal.body`` The first body who is part of the link.
          child: ``pypal.body`` The second body who is part of the link.
          collide: ``bool`` Weather or not the bodies involved in the link should coolide with each other.
        """
        self.obj = _pal.lib.link_rigid_create(parent.obj,child.obj,c.c_bool(collide))

    def get_feedback():
        """ Returns the magnitude of the force on the link. """
        _pal.lib.link_rigid_get_feedback.restype = c.c_float
        return _pal.lib.link_rigid_get_feedback(self.obj)