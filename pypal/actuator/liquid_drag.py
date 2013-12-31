from pypal import private_globals as pal
import ctypes as c
import weakref
from actuatorbase import ActuatorBase
class LiquidDrag(ActuatorBase):
    def __init__(self,body,area,drag,density):
        """
        applies a torque to a revolute link
        
        body: The body to which the drag is applied.
    	area: The frontal area of the body to which the drag is applied
    	drag: The drag coefficient
    	density: The fluid density 
        """
        self.obj = pal.lib.create_liqid_drag(body.obj,c.c_char(body.typechar),
                                             c.c_float(area), c.c_float(drag),
                                             c.c_float(density))

    def run(self):
        """ensures the actuator will be running for this step."""
        pal.lib.liquid_drag_run(self.obj)
