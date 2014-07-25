from pypal import private_globals as _pal
import ctypes as c
import weakref
from generic_body import GenericBody
from ..geometry import Capsule
class Character(GenericBody):
    """
    A Character.

    The Character class is a convinience wrapper of a Generic body wich a capsule geometry.
    As the angular damping of the body is set to a high number, the character wont fall over!
    """
    def __init__(self, pos, size, rotation=[0,0,0], mass=1.):
        """
        Parameters:
          pos: ``float[3]`` The x, y, z position of the Character.
          size: ``float[2]`` The radius, height of the Character.
          rotation: ``float[3]`` the rx, ry, rz rotation of the body.
            Note: A Character will never rotate on any axis,
          mass: ``float`` The mass of the Character.
        """
        GenericBody.__init__(self, pos, rotation)
        self.dynamic_type = "dynamic"
        self.mass = mass
        self.collision_response = True
        self.geom = Capsule([0,0,0], size, mass=mass)
        self.connect_geometry(self.geom)
        self.angular_damping = 100000
        
    def __str__(self):
        x, y, z = self.get_position()
        return "A Character at : %.2f, %.2f, %.2f" % (x, y, z)

    def walk(self, direction):
        """
        Walk the character forward along the given vector

        Note: The walk function needs to be called every time the physics engine is updated.

        Parameters:
          direction: ``float[3]`` The unit vector the character should walk along.
        """
        x, y, z = self.get_position()
        self.set_position((x + direction[0]/100., y + direction[1]/100., z + direction[2]/100.))
        #_pal.lib.body_character_walk(self.obj,c.c_float(direction[0]),c.c_float(direction[1]),c.c_float(direction[2]),c.c_float(duration))

    def warp(self, vector):
        pass
        #_pal.lib.body_character_warp(self.obj,c.c_float(vector[0]),c.c_float(vector[1]),c.c_float(vector[2]))

