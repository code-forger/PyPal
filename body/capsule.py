from bodybase import BodyBase
class Capsule(BodyBase):
    def __init__(rect,mass = None, density = None, static = False):
        """
        constructs a box and adds it to the world
        
        rect: a 5 part tuple with x,y,z,radius,length.
        Note: if a 6 part rect is passed in, the width will be taken as the
        radius and the height as the length, the depth will be ignored.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        static: used to create this object static, if static is true, mass will be ignored
        """
        pass

    def get_radius():
        """returns the radius of the object"""
        pass

    def get_length():
        """returns the length of the object"""
        pass

    def get_size():
        """returns the size of the object in a 2 part tuple"""
        pass

    def get_metrics():
        """returns the pos and size of the object in a 5 part tuple"""
        pass
