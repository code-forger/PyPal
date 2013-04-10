import private_globals as pal
import ctypes as c
import weakref
from geometry_base import GeometryBase
class Box(GeometryBase):
    def __new__(cls,rect,mass=None, density = None):
        """
        constructs a box and adds it to the world
        
        rect: a 6 part tuple with x,y,z,width,height,depth.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        static: used to create this object static, if static is true, mass will be ignored
        """
        box = super(Box,cls).__new__(cls)
        box._create(rect,mass,density)
        pal.all_objects[str(pal.all_next)] = box
        pal.lib.body_set_data(box.obj,pal.all_next)
        pal.all_next += 1
        return weakref.proxy(box)


    def _create(self,rect,mass = None, density = None):#TESTED
        """
        THIS METHOD IS PRIVATE: to create a box use the create class method
        constructs a box and adds it to the world
        
        rect: a 6 part tuple with x,y,z,width,height,depth.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        static: used to create this object static, if static is true, mass will be ignored
        """
        self.obj = pal.lib.create_geometry_box(c.c_float(rect[0]),c.c_float(rect[1]),c.c_float(rect[2]),c.c_float(rect[3]),c.c_float(rect[4]),c.c_float(rect[5]),c.c_float(mass))


    def delete(self):
        x = pal.lib.body_get_data(self.obj)
        pal.lib.box_remove(self.obj)
        del pal.all_objects[str(x)]

