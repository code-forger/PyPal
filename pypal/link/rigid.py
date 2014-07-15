from pypal import private_globals as _pal
import ctypes as c
import weakref
class Rigid(_pal.PalObject):
    def __init__(self,parent,child,collide):
        self.obj = _pal.lib.link_rigid_create(parent.obj,child.obj,c.c_bool(collide))

    def get_feedback():
        _pal.lib.link_rigid_get_feedback.restype = c.c_float
        return _pal.lib.link_rigid_get_feedback(self.obj)