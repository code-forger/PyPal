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
        pal.all_objects[str(compound.obj)] = compound
        return weakref.proxy(compound)

    def _create(self,pos):
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

    def get_velocity(self):
        """Returns the linear velocity of the body."""
        pal.lib.compound_get_velocity_x.restype = c.c_float
        pal.lib.compound_get_velocity_y.restype = c.c_float
        pal.lib.compound_get_velocity_z.restype = c.c_float
        return [pal.lib.compound_get_velocity_x(self.obj),pal.lib.compound_get_velocity_y(self.obj),pal.lib.compound_get_velocity_z(self.obj)]


    def delete(self):
        pal.lib.compound_remove(self.obj)
        del pal.all_objects[str(self.obj)]
