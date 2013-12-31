from pypal import private_globals as pal
import ctypes as c
import weakref
from actuatorbase import ActuatorBase
class Hydrofoil(ActuatorBase):
    def __init__(self,body,pos,direction,lift_vector,area,qa,qb,qc,density):
        """
        applies an hydrofoil to a body
        
    	body: The body to connect the actuator to
	    pos: The x position of the actuator's center
	    direction: The unit vector which supplies the orientation of the actuator.
	    lift_vector: the direction in which the lift force is applied
	    area 	The frontal area of the hydrofoil.
	    a 	The quadratic term of the lift coefficient
	    b 	The linear term of the lift coefficient
	    c 	The constant term of the lift coefficient
	    density 	The density of the liquid. 
        """
        self.obj = pal.lib.create_hydrofoil(body.obj, c.c_char(body.typechar),
                                            c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]),
                                            c.c_float(direction[0]), c.c_float(direction[1]), c.c_float(direction[2]),
                                            c.c_float(lift_vector[0]), c.c_float(lift_vector[1]), c.c_float(lift_vector[2]),
                                            c.c_float(area),c.c_float(qa),c.c_float(qb),c.c_float(qc), c.c_float(density))

    def set_angle(self,angle):
        """sets the angle of attack of the actuator in range-pi/2 to pi/2"""
        pal.lib.hydrofoil_set_angle(self.obj, c.c_float(angle))

    def run(self):
        """ensures the actuator will be running for this step."""
        pal.lib.hydrofoil_run(self.obj)
