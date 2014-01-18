from pypal import private_globals as pal
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
    def __init__(self,pos,points,matrix,triangles=None):#TESTED

        CPoints = c.c_float * (len(points) * 3)
        cpoints = CPoints()
        for i in xrange(len(points)):
            for j in xrange(3):
                cpoints[(i*3)+j] = points[i][j]

        if triangles==None:
            self.obj = pal.lib.create_static_convex_no_triangles(c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]),
                                  c.pointer(cpoints),len(points)*3) 
            pal.lib.body_set_position(self.obj,c.c_char(self.typechar),c.c_float(matrix[12]),c.c_float(matrix[13]),c.c_float(matrix[14]))
        else:
            CTris = c.c_int * len(triangles*3)
            ctris = CTris()
            for i in xrange(len(triangles)):
                for j in xrange(3):
                    ctris[(i*3)+j] = triangles[i][j]
            mat = [c.c_float(x) for x in matrix]
            self.obj = pal.lib.create_static_convex_triangles(mat[0],mat[1],mat[2],mat[3],
                                                                 mat[4],mat[5],mat[6],mat[7],
                                                                 mat[8],mat[9],mat[10],mat[11],
                                                                 mat[12],mat[13],mat[14],mat[15],
                                  c.pointer(cpoints),len(points), c.pointer(ctris), len(triangles)*3) 

    def delete(self):
        pal.lib.static_convex_remove(self.obj,self.typechar)
        del pal.all_objects[str(self.obj)]
