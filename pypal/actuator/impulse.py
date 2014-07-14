from pypal import private_globals as _pal
import ctypes as c
import weakref
from actuatorbase import ActuatorBase
class Impulse(ActuatorBase):
    def __init__(self,body,pos,direction,impulse=None):
        """
        applies an impulse to a body
        
        body: The body to connect the actuator to
        pos: The x position of the actuator's center
        direction: The unit vector which supplies the direction of the actuator's impulse.
        impulse: the impulse for the actuator to apply, if none is set the actuator will do nothing
        """
        self.obj = _pal.lib.actuator_impulse_create(body.obj,c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),
                                         c.c_float(direction[0]),c.c_float(direction[1]),c.c_float(direction[2]))
        if impulse:
            self.set_impulse(impulse)

    def set_impulse(self,impulse):
        """sets the impulse of the actuator"""
        _pal.lib.actuator_impulse_set_impulse(self.obj,c.c_float(impulse))

    def apply(self):
        """ensures the actuator will be running for this step."""
        _pal.lib.actuator_impulse_apply (self.obj)
