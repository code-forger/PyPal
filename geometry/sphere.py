from geometry_base import GeometryBase
class Sphere(GeometryBase):
    """a geometry that represents a Sphere"""
    def __init__(rect,mass = None, density = None):
        """
        constructs a Sphere
        
        rect: a 5 part tuple with x,y,z,radius.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        """
        pass
