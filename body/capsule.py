import private_globals as pal
import ctypes as c
import weakref
from bodybase import BodyBase
class Capsule(BodyBase):
    @classmethod
    def create(self,rect,mass = None, density = None, static = False):
        """
        constructs a box and adds it to the world
        
        rect: a 5 part tuple with x,y,z,radius,length.
        Note: if a 6 part rect is passed in, the width will be taken as the
        radius and the height as the length, the depth will be ignored.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        static: used to create this object static, if static is true, mass will be ignored
        """
        capsule = Capsule(rect,mass,density,static)
        pal.all_objects[str(pal.all_next)] = capsule
        pal.lib.body_set_data(capsule.obj,pal.all_next)
        pal.all_next += 1
        self.size = rect[3:5]
        return weakref.proxy(capsule)

    def __init__(self,rect,mass = None, density = None, static = False):
        """
        THIS METHOD IS PRIVATE: to create a capsule use the create class method
        constructs a box and adds it to the world
        
        rect: a 5 part tuple with x,y,z,radius,length.
        Note: if a 6 part rect is passed in, the width will be taken as the
        radius and the height as the length, the depth will be ignored.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        static: used to create this object static, if static is true, mass will be ignored
        """
        self.obj = pal.lib.create_capsule(c.c_float(rect[0]),c.c_float(rect[1]),c.c_float(rect[2]),c.c_float(rect[3]),c.c_float(rect[4]),c.c_float(mass))


    def get_size(self):
        """returns the size of the object in a 2 part tuple"""
        return self.size

    def set_position(self,pos):
        """Sets the position of the object and/or its orientation."""
        pal.lib.capsule_set_position(self.obj,c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]))

    def delete(self):
        x = pal.lib.body_get_data(self.obj)
        pal.lib.capsule_remove(self.obj)
        del pal.all_objects[str(x)]
