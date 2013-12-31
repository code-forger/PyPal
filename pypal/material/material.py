from pypal import private_globals as pal
import ctypes as c
import weakref
class Material(object):
    materials = {}
    def  __new__(cls, *args, **kwargs):
        print "here"
        o = super(Material,cls).__new__(cls)
        o.__init__(*args, **kwargs)
        Material.materials[o.name] = o
        return weakref.proxy(o)

    def __init__(self, name, static_friction, kinetic_friction, restitution):
        self.obj = pal.lib.add_material(c.c_float(static_friction),
                                        c.c_float(kinetic_friction),
                                        c.c_float(restitution))
        self.name = name
