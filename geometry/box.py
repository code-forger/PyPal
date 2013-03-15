class Box(GeometryBase):
    """a geometry that represents a cuboid"""
    def __init__(rect,mass = None, density = None):
        """
        constructs a box
        
        rect: a 6 part tuple with x,y,z,width,height,depth.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        """
        pass
