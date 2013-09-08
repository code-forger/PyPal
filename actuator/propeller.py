from pypalgame import private_globals as pal
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
        self.obj = pal.lib.create_propeller(body.obj, c.c_char(body.typechar),
                                            c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]),
                                            c.c_float(direction[0]), c.c_float(direction[1]), c.c_float(direction[2]),
                                            c.c_float(lumped))


    def set_voltage(self,voltage):
        """sets the voltage of the actuator"""
        pal.lib.propeller_set_voltage(self.obj, c.c_float(voltage))

    def run(self):
        """ensures the actuator will be running for this step."""
        pal.lib.propeller_run(self.obj)
