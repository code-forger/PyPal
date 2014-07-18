from pypal import private_globals as _pal
import ctypes as c
import weakref
class StaticCompound(_pal.PalObject):
    def __init__(self, pos):
        """
        constructs a static compound and adds it to the world
        
        pos: a 3 part tuple with x,y,z.
        size: a 3 part tuple with width, height, depth
        """
        self.obj = _pal.lib.body_static_compound_create(c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]))

    def get_location(self):
        """ Return the location of the body as a ``float[16]`` matrix. """
        ret = _pal.Mat4x4()
        _pal.lib.body_static_compound_get_location(self.obj, ret)
        return [x for x in ret]

    def get_position(self):
        """ Return position of the body as the ``float[3]`` x, y, z components. """
        ret = _pal.Vec3()
        _pal.lib.body_static_compound_get_position(self.obj, ret)
        return [x for x in ret]

    def set_material(self, material):
        _pal.lib.body_static_compound_set_material(self.obj, material.obj)

    def get_group(self):
        """ Return collision group of the body as a ``float``. """
        return _pal.lib.body_static_compound_get_group(self.obj)

    def set_group(self, group):
        return _pal.lib.body_static_compound_set_group(self.obj, c.c_int(group))

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
