class Sphere(BodyBase):
    def __init__(rect,mass = None, density = None, static = False):
        """
        constructs a box and adds it to the world
        
        rect: a 4 part tuple with x,y,z,radius.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        static: used to create this object static, if static is true, mass will be ignored
        """
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
