from pypal import private_globals as _pal
import ctypes as c
import weakref
from actuatorbase import ActuatorBase
class Spring(ActuatorBase):
    """ Applies a spring link to a pair of bodies """
    def __init__(self, body1,body2,spring_desc):
        """
        Parameters:
          body1: ``pypal.body`` The body to connect the spring to (1)
          body2: ``pypal.body`` The body to connect the spring to (2)
          rest_length: ``float`` The resting length of the spring.
          spring: ``float`` The spring constant.
          dampening: ``float`` The damping constant. 
        """
        self.obj = _pal.lib.actuator_spring_create(body1._body,body2._body,c.c_float(spring_desc[0]),c.c_float(spring_desc[1]),c.c_float(spring_desc[2]))

    def apply(self):
        """ Ensures the actuator will be running for this step. """
        _pal.lib.actuator_spring_apply(self.obj)