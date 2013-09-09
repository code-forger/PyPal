from pypalgame import private_globals as pal
import ctypes as c
import weakref
from geometry_base import GeometryBase
class Convex(GeometryBase):
    """a geometry that represents a convex shape"""
    def __init__(self, rect, rotation = [0,0,0],points=((0,0,0)),mass=1):
        """
        constructs a convex shape
        
        points: A set of vertices, which describe the location of corners in an object.
        rect: a 6 part tuple with x,y,z,width,height,depth.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        """

        CPoints = c.c_float * (len(points) * 3)
        cpoints = CPoints()
        for i in xrange(len(points)):
            for j in xrange(3):
                cpoints[(i*3)+j] = points[i][j]

        self.obj = pal.lib.create_geometry_box(c.c_float(rect[0]),c.c_float(rect[1]),c.c_float(rect[2]),c.c_float(rotation[0]),c.c_float(rotation[1]),c.c_float(rotation[2]),
                                               c.pointer(cpoints),len(points)*3,c.c_float(mass))



    def delete(self):
        pal.lib.box_geometry_remove(self.obj)
        del pal.all_objects[str(self.obj)]
