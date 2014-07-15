from pypal import private_globals as _pal
import ctypes as c
import weakref
from actuatorbase import ActuatorBase
class Spring(ActuatorBase):
    def __init__(self, body1,body2,spring_desc):
        """
        applies a spring link to a pair of bodies
        
        body1: The body to connect the spring to (1)
        body2: The body to connect the spring to (2)
            rest_length: The resting length of the spring.
            spring: The spring constant.
            dampening: The damping constant. 
        """
        self.obj = _pal.lib.actuator_spring_create(_pal.get_body_pointer(body1),_pal.get_body_pointer(body2),c.c_float(spring_desc[0]),c.c_float(spring_desc[1]),c.c_float(spring_desc[2]))

    def apply(self):
        """ensures the actuator will be running for this step."""
        _pal.lib.actuator_spring_apply(self.obj)