from pypal import private_globals as _pal
import ctypes as c
import weakref
from actuatorbase import ActuatorBase
from pypal import body
class Hydrofoil(ActuatorBase):
    _create_functions = {body.Box:_pal.lib.actuator_hydrofoil_create_on_box,
                        body.Sphere:_pal.lib.actuator_hydrofoil_create_on_sphere,
                        body.Capsule:_pal.lib.actuator_hydrofoil_create_on_capsule,
                        body.Compound:_pal.lib.actuator_hydrofoil_create_on_compound,
                        body.Convex:_pal.lib.actuator_hydrofoil_create_on_convex,
                        body.GenericBody:_pal.lib.actuator_hydrofoil_create_on_generic}
    def __init__(self,body,pos,direction,lift_vector,lift_params,density):
        """
        applies an hydrofoil to a body
        
    	body: The body to connect the actuator to
	    pos: The x position of the actuator's center
	    direction: The unit vector which supplies the orientation of the actuator.
	    lift_vector: the direction in which the lift force is applied
        lift_params: float(4):
                    	    area 	The frontal area of the hydrofoil.
                    	    a 	The quadratic term of the lift coefficient
                    	    b 	The linear term of the lift coefficient
                    	    c 	The constant term of the lift coefficient
	    density 	The density of the liquid. 
        """
        self.obj = self._create_functions[body.__class__](body.obj,
                                            c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]),
                                            c.c_float(direction[0]), c.c_float(direction[1]), c.c_float(direction[2]),
                                            c.c_float(lift_vector[0]), c.c_float(lift_vector[1]), c.c_float(lift_vector[2]),
                                            c.c_float(lift_params[0]),c.c_float(lift_params[1]),c.c_float(lift_params[2]),c.c_float(lift_params[3]), c.c_float(density))

    def set_angle(self,angle):
        """sets the angle of attack of the actuator in range-pi/2 to pi/2"""
        _pal.lib.actuator_hydrofoil_set_angle(self.obj, c.c_float(angle))

    def apply(self):
        """ensures the actuator will be running for this step."""
        _pal.lib.actuator_hydrofoil_apply(self.obj)
