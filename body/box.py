import private_globals as pal
import ctypes as c
import weakref
from bodybase import BodyBase
class Box(BodyBase):
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
        self.obj = pal.lib.create_box(c.c_float(rect[0]),c.c_float(rect[1]),c.c_float(rect[2]),c.c_float(rect[3]),c.c_float(rect[4]),c.c_float(rect[5]),c.c_float(mass))

    def get_size(self):
        """returns the size of the object in a 3 part tuple"""
        size = [c.c_float() for x in range(3)]
        pal.lib.box_get_size(self.obj,c.byref(size[0]),c.byref(size[1]),c.byref(size[2]))
        return [p.value for p in size]

    def set_position(self,pos):
        """Sets the position of the object and/or its orientation."""
        pal.lib.box_set_position(self.obj,c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]))

    def apply_impulse(self,impulse):
        """Applies an impulse to the object for a single step at an optional offset in world coordinates."""
        pal.lib.box_apply_impulse(self.obj,c.c_float(impulse[0]),c.c_float(impulse[1]),c.c_float(impulse[2]))

    def is_active(self):
        """Returns true if the body is not asleep."""
        pal.lib.box_is_active.restype = c.c_bool
        return pal.lib.box_is_active(self.obj)

    def set_active(self,active):
        """Sets the body to active or not."""
        pal.lib.box_set_active(self.obj,c.c_bool(active))

    def get_velocity(self):
        """Returns the linear velocity of the body."""
        pal.lib.box_get_velocity_x.restype = c.c_float
        pal.lib.box_get_velocity_y.restype = c.c_float
        pal.lib.box_get_velocity_z.restype = c.c_float
        return [pal.lib.box_get_velocity_x(self.obj),pal.lib.box_get_velocity_y(self.obj),pal.lib.box_get_velocity_z(self.obj)]


    def delete(self):
        x = pal.lib.body_get_data(self.obj)
        pal.lib.box_remove(self.obj)
        del pal.all_objects[str(x)]


class StaticBox(BodyBase):
    def __new__(cls,rect):
        """
        constructs a box and adds it to the world
        
        rect: a 6 part tuple with x,y,z,width,height,depth.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        static: used to create this object static, if static is true, mass will be ignored
        """
        box = super(StaticBox,cls).__new__(cls)
        box._create(rect)
        pal.all_objects[str(pal.all_next)] = box
        pal.lib.body_set_data(box.obj,pal.all_next)
        pal.all_next += 1
        return weakref.proxy(box)

    def _create(self,rect):#TESTED
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
