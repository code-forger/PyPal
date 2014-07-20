from pypal import private_globals as _pal
import ctypes as c
import weakref
from generic_body import GenericBody
from ..geometry import Capsule
class Character(GenericBody):
    def __init__(self, pos, size, rotation=[0,0,0], mass=1.):
        """
        constructs a character and adds it to the world
        
        rect: a 5 part tuple with x,y,z,radius,height
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        static: used to create this object static, if static is true, mass will be ignored
        """
        GenericBody.__init__(self, pos, rotation)
        self.dynamic_type = "dynamic"
        self.mass = mass
        self.collision_response = True
        self.geom = Capsule([0,0,0], size)
        self.connect_geometry(self.geom)
        self.angular_damping = 100000
        
    def __str__(self):
        x, y, z = self.get_position()
        return "A Character at : %.2f, %.2f, %.2f" % (x, y, z)

    def walk(self, d):
        x, y, z = self.get_position()
        self.set_position((x + d[0]/100., y + d[1]/100., z + d[2]/100.))
        #_pal.lib.body_character_walk(self.obj,c.c_float(direction[0]),c.c_float(direction[1]),c.c_float(direction[2]),c.c_float(duration))

    def warp(self, vector):
        pass
        #_pal.lib.body_character_warp(self.obj,c.c_float(vector[0]),c.c_float(vector[1]),c.c_float(vector[2]))

