from pypalgame import private_globals as pal
import ctypes as c
import weakref
from actuatorbase import ActuatorBase
class Spring(ActuatorBase):
    def __init__(self, body1,body2,rest_length,spring,dampening):
        """
        applies a spring link to a pair of bodies
        
        body1: The body to connect the spring to (1)
        body2: The body to connect the spring to (2)
        rest_length: The resting length of the spring.
        spring: The spring constant.
        dampening: The damping constant. 
        """
        self.obj = pal.lib.create_spring(body1.obj,c.c_char(body1.typechar),body2.obj,c.c_char(body2.typechar),c.c_float(rest_length),c.c_float(spring),c.c_float(dampening))

    def run(self):
        """ensures the actuator will be running for this step."""
        pal.lib.spring_run(self.obj)
