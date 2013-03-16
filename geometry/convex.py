from geometry_base import GeometryBase
class Convex(GeometryBase):
    """a geometry that represents a convex shape"""
    def __init__(points,mass = None, density = None):
        """
        constructs a convex shape
        
        points: A set of vertices, which describe the location of corners in an object.
        rect: a 6 part tuple with x,y,z,width,height,depth.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        """
        pass
