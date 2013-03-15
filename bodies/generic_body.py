class GenericBody(BodyBase):
    def __init__(pos,mass = None, density = None):
        """
        constructs a box and adds it to the world
        
        rect: a 3 part tuple with x,y,z.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        """
        pass

    def setDynamicsType(dynType):
        """
        Sets the body to dynamic, static, or kinematic
        
        dynType: "dynamic", "static" or "kinematic"
        """
        pass

    def setMass(mass = None, density = None):
        """
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        """
        pass

    def setInertia(Ixx,Iyy,Izz):
        """
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        """
        pass

    def connectGeometry(geometry):
        """
        connects a geometry
        """
        pass

    def getGeometrys():
        """
        returns a list of geometries
        """
        pass

    def removeGrometry(geometry):
        """
        removes a geometry if found
        """
        pass
