from pypal import private_globals as _pal
import ctypes as c
import weakref
from actuatorbase import ActuatorBase
class FakeBuoyancy(ActuatorBase):
    def __init__(self,body,density=998.29):
        """
        applies an impulse to a body
        
        body: The body to connect the actuator to
        pos: The x position of the actuator's center impulse for the actuator to apply, if none is set the actuator will do nothing
        """
        self.obj = _pal.lib.actuator_fake_buoyancy_create(body.obj,c.c_float(density))

    def apply(self):
        """ensures the actuator will be running for this step."""
        _pal.lib.actuator_fake_buoyancy_apply(self.obj)
