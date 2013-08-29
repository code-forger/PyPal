import private_globals as pal
import ctypes as c
import weakref
class Rigid(pal.PalObject):
    def __init__(self,parent,child,collide):
        self.obj = pal.lib.create_rigid(parent.obj,child.obj,c.c_bool(collide))

    def delete(self):
        pal.lib.rigid_link_remove(self.obj)
        del pal.all_objects[str(self.obj)]
