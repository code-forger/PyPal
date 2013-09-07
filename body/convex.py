from bodybase import BodyBase
class Convex(BodyBase):
    typechar = 'x'
    def __init__(pos,points,mass = None, density = None):
        """
        constructs a box and adds it to the world
        
        rect: a 3 part tuple with x,y,z.    
        points: the points to construct the convex hull.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        """
        pass

    def get_point():
        """returns the points of the object"""
        pass

    def get_metrics():
        """returns the pos of the object in a 3 part tuple"""
        pass
