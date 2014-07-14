from pypal import private_globals as _pal
import ctypes as c
import weakref
from actuatorbase import ActuatorBase
from pypal import body
class LiquidDrag(ActuatorBase):
    _create_functions = {body.Box:_pal.lib.actuator_liquid_drag_create_on_box,
                        body.Sphere:_pal.lib.actuator_liquid_drag_create_on_sphere,
                        body.Capsule:_pal.lib.actuator_liquid_drag_create_on_capsule,
                        body.Compound:_pal.lib.actuator_liquid_drag_create_on_compound,
                        body.Convex:_pal.lib.actuator_liquid_drag_create_on_convex,
                        body.GenericBody:_pal.lib.actuator_liquid_drag_create_on_generic}
    def __init__(self,body,area,drag,density):
        """
        applies a torque to a revolute link
        
        body: The body to which the drag is applied.
    	area: The frontal area of the body to which the drag is applied
    	drag: The drag coefficient
    	density: The fluid density 
        """
        self.obj = self._create_functions[body.__class__](body.obj,
                                             c.c_float(area), c.c_float(drag),
                                             c.c_float(density))

    def apply(self):
        """ensures the actuator will be running for this step."""
        _pal.lib.actuator_liquid_drag_apply(self.obj)
