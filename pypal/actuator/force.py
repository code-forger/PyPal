from pypal import private_globals as _pal
import ctypes as c
import weakref
from actuatorbase import ActuatorBase
class Force(ActuatorBase):
    """ Applies a force to a body. """
    def __init__(self,body,pos,direction,force=None):
        """
        Parameters:
          body: ``pypal.body`` The body to connect the actuator to.
          pos: ``float[3]`` The x, y, z position of the actuator's center.
          direction: ``float[3]`` The unit vector which supplies the direction of the actuator's force.
          force: ``float`` The force for the actuator to apply, if none is set the actuator will do nothing.
        """
        self.obj = _pal.lib.actuator_force_create(body.obj,c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),
                                         c.c_float(direction[0]),c.c_float(direction[1]),c.c_float(direction[2]))
        if force:
            self.set_force(force)

    def set_force(self,force):
        """ 
        Sets the force of the actuator.

        Parameters:
          force: ``float`` The force for the actuator to apply, if none is set the actuator will do nothing.ctuator to.
        """
        _pal.lib.actuator_force_set_force(self.obj,c.c_float(force))

    def apply(self):
        """ Ensures the actuator will be running for this step."""
        _pal.lib.actuator_force_apply(self.obj)
