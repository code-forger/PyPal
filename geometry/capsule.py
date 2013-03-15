class Capsule(GeometryBase):
    """a geometry that represents a capsule"""
    def __init__(points,triangles,mass = None, density = None):
        """
        constructs a capsule
        
        rect: a 5 part tuple with x,y,z,radius,length.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        """
        pass
