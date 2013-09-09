from pypalgame import private_globals as pal
import ctypes as c
import weakref
from bodybase import BodyBase
class Compound(BodyBase):
    typechar = 'o'
    def __init__(self,pos):
        self.obj = pal.lib.create_compound(c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]))

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

    def add_box(self,pos,mass,rotation=(0,0,0)):
        """adds a box geometry to the compound body"""
        pal.lib.compound_add_box(self.obj, c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]), c.c_float(rotation[0]), c.c_float(rotation[1]), c.c_float(rotation[2]), c.c_float(pos[3]), c.c_float(pos[4]), c.c_float(pos[5]),c.c_float(mass))

    def add_sphere(self,pos,mass,rotation=(0,0,0)):
        """adds a sphere geometry to the compound body"""
        pal.lib.compound_add_sphere(self.obj, c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]), c.c_float(rotation[0]), c.c_float(rotation[1]), c.c_float(rotation[2]), c.c_float(pos[3]),c.c_float(mass))

    def add_capsule(self,pos,mass,rotation=(0,0,0)):
        """adds a sphere geometry to the compound body"""
        pal.lib.compound_add_capsule(self.obj, c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]), c.c_float(rotation[0]), c.c_float(rotation[1]), c.c_float(rotation[2]), c.c_float(pos[3]), c.c_float(pos[4]),c.c_float(mass))

    def add_convex(self,pos,points,mass,rotation=(0,0,0)):
        """adds a sphere geometry to the compound body"""
        CPoints = c.c_float * (len(points) * 3)
        cpoints = CPoints()
        for i in xrange(len(points)):
            for j in xrange(3):
                cpoints[(i*3)+j] = points[i][j]
        pal.lib.compound_add_convex(self.obj, c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]), c.c_float(rotation[0]), c.c_float(rotation[1]), c.c_float(rotation[2]), c.pointer(cpoints),len(points)*3,c.c_float(mass)))

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
