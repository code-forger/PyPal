from pypalgame import private_globals as pal
import ctypes as c
import weakref
from bodybase import BodyBase
class Convex(BodyBase):
    typechar = 'x'
    def __init__(self,pos,points,mass = 1):
        """
        constructs a box and adds it to the world
        
        rect: a 3 part tuple with x,y,z.
        points: the points to construct the convex hull.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        """

        CPoints = c.c_float * (len(points) * 3)
        cpoints = CPoints()
        for i in xrange(len(points)):
            for j in xrange(3):
                cpoints[(i*3)+j] = points[i][j]

        self.obj = pal.lib.create_convex(c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]),
                              c.pointer(cpoints),len(points)*3,c.c_float(mass))

        self.points = points
    def get_point():
        """returns the points of the object"""
        return points

    def delete(self):
        pal.lib.convex_remove(self.obj,self.typechar)
        del pal.all_objects[str(self.obj)]


class StaticConvex(BodyBase):
    typechar = 'X'
    def __init__(self,pos,points):#TESTED

        CPoints = c.c_float * (len(points) * 3)
        cpoints = CPoints()
        for i in xrange(len(points)):
            for j in xrange(3):
                cpoints[(i*3)+j] = points[i][j]

        self.obj = pal.lib.create_static_convex(c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]),
                              c.pointer(cpoints),len(points)*3)

    def delete(self):
        pal.lib.static_convex_remove(self.obj,self.typechar)
        del pal.all_objects[str(self.obj)]
