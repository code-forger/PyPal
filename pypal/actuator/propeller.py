from pypal import private_globals as _pal
import ctypes as c
import weakref
from actuatorbase import ActuatorBase
class Propeller(ActuatorBase):
    """ Simulates a propeller for a body """
    def __init__(self,body,pos,direction,lumped):
        """
        Parameters:
    	  body: ``pypal.body`` The body to connect the actuator to.
	      pos: ``float[3]`` The x, y, z position of the actuator's center.
	      direction: ``float[3]`` The unit vector which supplies the orientation of the actuator.
	      lumped: ``float`` The lumped parameter.
        """
        self.obj = _pal.lib.actuator_propeller_create(body._body,
                                            c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]),
                                            c.c_float(direction[0]), c.c_float(direction[1]), c.c_float(direction[2]),
                                            c.c_float(lumped))


    def set_voltage(self,voltage):
        """
        Sets the voltage of the actuator.

        Parameters:
          voltage: ``float`` The voltage to be applied to the propeller
        """
        _pal.lib.actuator_propeller_set_voltage(self.obj, c.c_float(voltage))

    def apply(self):
        """ Ensures the actuator will be running for this step. """
        _pal.lib.actuator_propeller_apply(self.obj)
