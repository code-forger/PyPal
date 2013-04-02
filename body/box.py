import private_globals as pal
import ctypes as c
import weakref
from bodybase import BodyBase
class Box(BodyBase):
    @classmethod
    def create(self,rect,mass=None, density = None):
        """
        constructs a box and adds it to the world
        
        rect: a 6 part tuple with x,y,z,width,height,depth.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        static: used to create this object static, if static is true, mass will be ignored
        """
        box = Box(rect,mass,density)
        pal.all_objects[str(pal.all_next)] = box
        pal.lib.body_set_data(box.obj,pal.all_next)
        pal.all_next += 1
        return weakref.proxy(box)

    def __init__(self,rect,mass = None, density = None,static = False):#TESTED
        """
        THIS METHOD IS PRIVATE: to create a box use the create class method
        constructs a box and adds it to the world
        
        rect: a 6 part tuple with x,y,z,width,height,depth.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        static: used to create this object static, if static is true, mass will be ignored
        """
        self.obj = pal.lib.create_box(c.c_float(rect[0]),c.c_float(rect[1]),c.c_float(rect[2]),c.c_float(rect[3]),c.c_float(rect[4]),c.c_float(rect[5]),c.c_float(mass))

    def get_size(self):
        """returns the size of the object in a 3 part tuple"""
        size = [c.c_float() for x in range(3)]
        pal.lib.box_get_size(self.obj,c.byref(size[0]),c.byref(size[1]),c.byref(size[2]))
        return [p.value for p in size]

    def set_position(self,pos):
        """Sets the position of the object and/or its orientation."""
        pal.lib.box_set_position(self.obj,c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]))

    def delete(self):
        x = pal.lib.body_get_data(self.obj)
        pal.lib.box_remove(self.obj)
        del pal.all_objects[str(x)]


class StaticBox(BodyBase):
    @classmethod
    def create(self,rect):
        """
        constructs a box and adds it to the world
        
        rect: a 6 part tuple with x,y,z,width,height,depth.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        static: used to create this object static, if static is true, mass will be ignored
        """
        box = StaticBox(rect)
        pal.all_objects[str(pal.all_next)] = box
        pal.lib.body_set_data(box.obj,pal.all_next)
        pal.all_next += 1
        return weakref.proxy(box)

    def __init__(self,rect):#TESTED
        """
        THIS METHOD IS PRIVATE: to create a box use the create class method
        constructs a box and adds it to the world
        
        rect: a 6 part tuple with x,y,z,width,height,depth.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        static: used to create this object static, if static is true, mass will be ignored
        """
        self.obj = pal.lib.create_static_box(c.c_float(rect[0]),c.c_float(rect[1]),c.c_float(rect[2]),c.c_float(rect[3]),c.c_float(rect[4]),c.c_float(rect[5]))

    def get_size(self):
        """returns the size of the object in a 3 part tuple"""
        size = [c.c_float() for x in range(3)]
        pal.lib.static_box_get_size(self.obj,c.byref(size[0]),c.byref(size[1]),c.byref(size[2]))
        return [p.value for p in size]

    def delete(self):
        x = pal.lib.body_get_data(self.obj)
        pal.lib.body_clear_data(self.obj)
        pal.lib.static_box_remove(self.obj)
        del pal.all_objects[str(x)]
