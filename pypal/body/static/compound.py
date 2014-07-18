from pypal import private_globals as _pal
import ctypes as c
import weakref
from ..bodybase import BodyBase
class StaticCompound(BodyBase):
    def __init__(self, pos):
        """
        constructs a static compound and adds it to the world
        
        pos: a 3 part tuple with x,y,z.
        size: a 3 part tuple with width, height, depth
        """
        self.obj = _pal.lib.body_static_compound_create(c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]))
        self._body_base = _pal.lib.cast_static_compound_body_base(self.obj)

    def __str__(self):
        x, y, z = self.get_position()
        return "A Static Compound Body at : %.2f, %.2f, %.2f" % (x, y, z)

    def add_box(self,pos,mass,rotation=(0,0,0)):
        """adds a box geometry to the compound body"""
        _pal.lib.body_static_compound_add_box(self.obj, c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]), c.c_float(rotation[0]), c.c_float(rotation[1]), c.c_float(rotation[2]), c.c_float(pos[3]), c.c_float(pos[4]), c.c_float(pos[5]),c.c_float(mass))

    def add_sphere(self,pos,mass,rotation=(0,0,0)):
        """adds a sphere geometry to the compound body"""
        _pal.lib.body_static_compound_add_sphere(self.obj, c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]), c.c_float(rotation[0]), c.c_float(rotation[1]), c.c_float(rotation[2]), c.c_float(pos[3]),c.c_float(mass))

    def add_capsule(self,pos,mass,rotation=(0,0,0)):
        """adds a sphere geometry to the compound body"""
        _pal.lib.body_static_compound_add_capsule(self.obj, c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]), c.c_float(rotation[0]), c.c_float(rotation[1]), c.c_float(rotation[2]), c.c_float(pos[3]), c.c_float(pos[4]),c.c_float(mass))

    def add_convex(self,pos,points,mass,rotation=(0,0,0)):
        """adds a sphere geometry to the compound body"""
        CPoints = c.c_float * (len(points) * 3)
        cpoints = CPoints()
        for i in xrange(len(points)):
            for j in xrange(3):
                cpoints[(i*3)+j] = points[i][j]
        _pal.lib.body_static_compound_add_convex(self.obj, c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]), c.c_float(rotation[0]), c.c_float(rotation[1]), c.c_float(rotation[2]), c.pointer(cpoints),len(points)*3,c.c_float(mass))

    def finalize(self):
        _pal.lib.body_static_compound_finalize(self.obj)
