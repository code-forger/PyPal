from pypal import private_globals as _pal
import ctypes as c
import weakref
from actuatorbase import ActuatorBase
class Propeller(ActuatorBase):
    def __init__(self,body,pos,direction,lumped):
        """
        applies an propeller to a body
        
    	body: The body to connect the actuator to
	    pos: The x position of the actuator's center
	    direction: The unit vector which supplies the orientation of the actuator.
	    lumped: The lumped parameter 
        """
        self.obj = _pal.lib.actuator_propeller_create(body.obj,
                                            c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]),
                                            c.c_float(direction[0]), c.c_float(direction[1]), c.c_float(direction[2]),
                                            c.c_float(lumped))


    def set_voltage(self,voltage):
        """sets the voltage of the actuator"""
        _pal.lib.actuator_propeller_set_voltage(self.obj, c.c_float(voltage))

    def apply(self):
        """ensures the actuator will be running for this step."""
        _pal.lib.actuator_propeller_apply(self.obj)
