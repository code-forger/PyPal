from pypal import private_globals as _pal
import ctypes as c
import weakref
class Prismatic(_pal.PalObject):
    """a link that connects two objects telescopically"""
    def __init__(self,parent,child,pos,direction,collide):
        self.obj = _pal.lib.link_prismatic_create(parent.obj,child.obj,c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),c.c_float(direction[0]),c.c_float(direction[1]),c.c_float(direction[2]),c.c_bool(collide))

    def set_limits(self, min_limit, max_limit):
        """
        Sets limits on the link

        maX_limit: the maximum distance the child body can be from the link
        min_limit: the minimum distance the child body can be from the link
        """
        _pal.lib.link_prismatic_set_limits(self.obj, c.c_float(min_limit), c.c_float(max_limit))

    def get_feedback():
        _pal.lib.link_prismatic_get_feedback.restype = c.c_float
        return _pal.lib.link_prismatic_get_feedback(self.obj)