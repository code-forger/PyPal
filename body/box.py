from private_globals import *
from bodybase import BodyBase
class Box(BodyBase):
    def __init__(self,rect,mass = None, density = None,static = False):
        """
        constructs a box and adds it to the world
        
        rect: a 6 part tuple with x,y,z,width,height,depth.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        static: used to create this object static, if static is true, mass will be ignored
        """
        self.obj = lib.create_box(c.c_float(rect[0]),c.c_float(rect[1]),c.c_float(rect[2]),c.c_float(rect[3]),c.c_float(rect[4]),c.c_float(rect[5]),c.c_float(mass))

        pass

    def get_width():
        """returns the width of the object"""
        pass

    def get_height():
        """returns the height of the object"""
        pass

    def get_width():
        """returns the depth of the object"""
        pass

    def get_size():
        """returns the size of the object in a 3 part tuple"""
        pass

    def get_metrics():
        """returns the pos and size of the object in a 6 part tuple"""
        pass
