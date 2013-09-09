from pypalgame import private_globals as pal
import ctypes as c
import weakref
class Rigid(pal.PalObject):
    def __init__(self,parent,child,collide):
        self.obj = pal.lib.create_rigid(parent.obj,child.obj,c.c_bool(collide))
