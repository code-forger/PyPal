from pypal import private_globals as _pal
import ctypes as c
import weakref
from actuatorbase import ActuatorBase
class Impulse(ActuatorBase):
    """ Applies an impulse to a body. """
    def __init__(self,body,pos,direction,impulse=None):
        """
        Paramters:
          body: ``float`` The body to connect the actuator to.
          pos: ``float[3]`` The x, y, z position of the actuator's center.
          direction: ``float[3]`` The unit vector which supplies the direction of the actuator's impulse.
          impulse: ``float`` the impulse for the actuator to apply, if none is set the actuator will do nothing.
        """
        self.obj = _pal.lib.actuator_impulse_create(body.obj,c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),
                                         c.c_float(direction[0]),c.c_float(direction[1]),c.c_float(direction[2]))
        if impulse:
            self.set_impulse(impulse)

    def set_impulse(self,impulse):
        """
        Sets the impulse of the actuator.

        Paramters:
          impulse: ``float`` the impulse for the actuator to apply, if none is set the actuator will do nothing.
        """
        _pal.lib.actuator_impulse_set_impulse(self.obj,c.c_float(impulse))

    def apply(self):
        """ Ensures the actuator will be running for this step. """
        _pal.lib.actuator_impulse_apply (self.obj)
