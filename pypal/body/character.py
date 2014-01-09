from pypal import private_globals as pal
import ctypes as c
import weakref
from bodybase import BodyBase
class Character(pal.PalObject):
    typechar = 'C'
    def __init__(self,rect,mass=1):
        """
        constructs a box and adds it to the world
        
        rect: a 5 part tuple with x,y,z,radius,height
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        static: used to create this object static, if static is true, mass will be ignored
        """
        self.obj = pal.lib.create_character(c.c_float(rect[0]),c.c_float(rect[1]),c.c_float(rect[2]),c.c_float(rect[3]),c.c_float(rect[4]))


    def get_location_matrix(self):
        """Returns position as a 6 part tuple:(x,y,z,rx,ry,rz)."""
        mat = [c.c_float() for x in range(16)]
        pal.lib.character_get_matrix_location(self.obj,c.byref(mat[0]),c.byref(mat[1]),c.byref(mat[2]),c.byref(mat[3]),
                                                                         c.byref(mat[4]),c.byref(mat[5]),c.byref(mat[6]),c.byref(mat[7]),
                                                                         c.byref(mat[8]),c.byref(mat[9]),c.byref(mat[10]),c.byref(mat[11]),
                                                                         c.byref(mat[12]),c.byref(mat[13]),c.byref(mat[14]),c.byref(mat[15]))
        return [m.value for m in mat]

    def get_location(self):
        """Returns position as a 6 part tuple:(x,y,z,rx,ry,rz)."""
        pos = [c.c_float() for x in range(6)]
        pal.lib.character_get_primative_location(self.obj,c.byref(pos[0]),c.byref(pos[1]),c.byref(pos[2]),c.byref(pos[3]),c.byref(pos[4]),c.byref(pos[5]))
        return [p.value for p in pos]

    def walk(self, direction, duration):
        pal.lib.character_walk(self.obj,c.c_float(direction[0]),c.c_float(direction[1]),c.c_float(direction[2]),c.c_float(duration))

    def warp(self, vector):
        pal.lib.character_warp(self.obj,c.c_float(vector[0]),c.c_float(vector[1]),c.c_float(vector[2]))

