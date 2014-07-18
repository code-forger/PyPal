from pypal import private_globals as _pal
import ctypes as c
import weakref
from actuatorbase import ActuatorBase
from pypal import body
class LiquidDrag(ActuatorBase):
    """ Simulates LiquidDrag for a body. """
    def __init__(self,body,area,drag,density):
        """
        Parameters:
          body: ``pypal.body`` The body to which the drag is applied.
    	  area: ``float`` The frontal area of the body to which the drag is applied.
    	  drag: ``float`` The drag coefficient.
    	  density: ``float`` The fluid density Note: setting this to a low enough value can be used to simulate air drag.
        """
        self.obj = _pal.lib.actuator_liquid_drag_create(body._body,
                                             c.c_float(area), c.c_float(drag),
                                             c.c_float(density))

    def apply(self):
        """ Ensures the actuator will be running for this step. """
        _pal.lib.actuator_liquid_drag_apply(self.obj)
