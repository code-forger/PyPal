from pypal import private_globals as _pal
import ctypes as c
import weakref
class Material(_pal.PalObject):
    def  __new__(cls, *args, **kwargs):
        o = super(_pal.PalObject,cls).__new__(cls)
        o.__init__(*args, **kwargs)
        _pal.materials[o.name] = o
        return weakref.proxy(o)

    def __init__(self, name, static_friction, kinetic_friction, restitution):
        self.obj = _pal.lib.pal_add_material(c.c_float(static_friction),
                                        c.c_float(kinetic_friction),
                                        c.c_float(restitution))
        self.name = name
