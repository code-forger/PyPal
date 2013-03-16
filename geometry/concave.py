from geometry_base import GeometryBase
class Concave(GeometryBase):
    """a geometry that represents a concave shape"""
    def __init__(points,triangles,mass = None, density = None):
        """
        constructs a concave shape
        
        points: A set of vertices, which describe the location of corners in an object.
        triangles: A set of indices, which describes how the corners are connected to form triangle surfaces in an object.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        """
        pass
