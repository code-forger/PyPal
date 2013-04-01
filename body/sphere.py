import private_globals as pal
import ctypes as c
import weakref
from bodybase import BodyBase
class Sphere(BodyBase):
    @classmethod
    def create(self,rect,mass = None, density = None, static = False):
        """
        constructs a sphere and adds it to the world
        
        rect: a 6 part tuple with x,y,z,width,height,depth.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        static: used to create this object static, if static is true, mass will be ignored
        """
        sphere = Sphere(rect,mass,density,static)
        pal.all_objects[str(pal.all_next)] = sphere
        pal.lib.body_set_data(sphere.obj,pal.all_next)
        pal.all_next += 1
        self.size = rect[3]
        return weakref.proxy(sphere)

    def __init__(self,rect,mass = None, density = None, static = False):
        """
        THIS METHOD IS PRIVATE: to create a sphere use the create class method
        constructs a sphere and adds it to the world
        
        rect: a 4 part tuple with x,y,z,radius.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        static: used to create this object static, if static is true, mass will be ignored
        """
        self.obj = pal.lib.create_sphere(c.c_float(rect[0]),c.c_float(rect[1]),c.c_float(rect[2]),c.c_float(rect[3]),c.c_float(mass))

    def get_size(self):
        """returns the radius of the sphere"""
        return self.size

    def set_position(self,pos):
        """Sets the position of the object and/or its orientation."""
        pal.lib.sphere_set_position(self.obj,c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]))


    def delete(self):
        x = pal.lib.body_get_data(self.obj)
        pal.lib.sphere_remove(self.obj)
        del pal.all_objects[str(x)]
