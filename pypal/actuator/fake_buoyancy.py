from pypal import private_globals as _pal
import ctypes as c
import weakref
from actuatorbase import ActuatorBase
class FakeBuoyancy(ActuatorBase):
    """ Fakes Buoyancy for a dynamic body. """
    def __init__(self, body, density=998.29):
        """
        Parameters:
          body: ``pypal.body`` The body to connect the actuator to.
          density: ``float`` The density of the liquid.
        """
        self.obj = _pal.lib.actuator_fake_buoyancy_create(body.obj,c.c_float(density))

    def apply(self):
        """ Ensures the actuator will be running for this step."""
        _pal.lib.actuator_fake_buoyancy_apply(self.obj)
