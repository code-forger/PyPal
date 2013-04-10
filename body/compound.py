import private_globals as pal
import ctypes as c
import weakref
from bodybase import BodyBase
class Compound(BodyBase):
    def __new__(cls,pos):
        """
        constructs a sphere and adds it to the world
        
        rect: a 6 part tuple with x,y,z,width,height,depth.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        static: used to create this object static, if static is true, mass will be ignored
        """
        compound = super(Compound,cls).__new__(cls)
        compound._create(pos)
        pal.all_objects[str(pal.all_next)] = compound
        pal.lib.body_set_data(compound.obj,pal.all_next)
        pal.all_next += 1
        return weakref.proxy(compound)

    def _create(self,pos):
        """
        THIS METHOD IS PRIVATE: to create a sphere use the create class method
        constructs a sphere and adds it to the world
        
        rect: a 4 part tuple with x,y,z,radius.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        static: used to create this object static, if static is true, mass will be ignored
        """
        self.obj = pal.lib.create_compound(c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]))

    def set_position(self,pos):
        """Sets the position of the object and/or its orientation."""
        pal.lib.compound_set_position(self.obj,c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]))

    def apply_impulse(self,impulse):
        """Applies an impulse to the object for a single step at an optional offset in world coordinates."""
        pal.lib.compound_apply_impulse(self.obj,c.c_float(impulse[0]),c.c_float(impulse[1]),c.c_float(impulse[2]))

    def is_active(self):
        """Returns true if the body is not asleep."""
        pal.lib.compound_is_active.restype = c.c_bool
        return pal.lib.compound_is_active(self.obj)

    def set_active(self,active):
        """Sets the body to active or not."""
        pal.lib.compound_set_active(self.obj,c.c_bool(active))

    def add_box(self,pos,mass):
        """adds a box geometry to the compound body"""
        pal.lib.compound_add_box(self.obj, c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]), c.c_float(pos[3]), c.c_float(pos[4]), c.c_float(pos[5]),c.c_float(mass))

    def add_sphere(self,pos,mass):
        """adds a sphere geometry to the compound body"""
        pal.lib.compound_add_sphere(self.obj, c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]), c.c_float(pos[3]),c.c_float(mass))

    def add_capsule(self,pos,mass):
        """adds a sphere geometry to the compound body"""
        pal.lib.compound_add_capsule(self.obj, c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]), c.c_float(pos[3]), c.c_float(pos[4]),c.c_float(mass))

    def finalize(self):
        pal.lib.compound_finalize(self.obj)

    def delete(self):
        x = pal.lib.body_get_data(self.obj)
        pal.lib.body_clear_data(self.obj)
        pal.lib.compound_remove(self.obj)
        del pal.all_objects[str(x)]
