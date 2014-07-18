from pypal import private_globals as _pal
import ctypes as c
import weakref
from actuatorbase import ActuatorBase
from pypal import body
class Hydrofoil(ActuatorBase):
    """ A hydrofoil that simulates the lift from an underwater fin. """
    def __init__(self, body, pos, direction, lift_vector, lift_params, density):
        """
        Parameters:
          body: ``pypal.body`` The body to connect the actuator to.
          pos: ``float[3] The x, y, z position of the actuator's center.
          direction: ``float[3]`` The unit vector which supplies the orientation of the actuator.
          lift_vector: ``float[3]`` The unit vector direction in which the lift force is applied
          lift_params: ``float(4)`` The parameters of the lift function as follows:
                                0: The frontal area of the hydrofoil.
                                1: The quadratic term of the lift coefficient.
                                2: The linear term of the lift coefficient.
                                3: The constant term of the lift coefficient.
          density: ``float`` The density of the liquid. 
        """
        self.obj = _pal.lib.actuator_hydrofoil_create(body._body,
                                            c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]),
                                            c.c_float(direction[0]), c.c_float(direction[1]), c.c_float(direction[2]),
                                            c.c_float(lift_vector[0]), c.c_float(lift_vector[1]), c.c_float(lift_vector[2]),
                                            c.c_float(lift_params[0]),c.c_float(lift_params[1]),c.c_float(lift_params[2]),c.c_float(lift_params[3]), c.c_float(density))

    def set_angle(self,angle):
        """
        Sets the angle of attack of the actuator.

        Parameters:
          angle: ``float` The angle of attack in range-pi/2 to pi/2.
        """
        _pal.lib.actuator_hydrofoil_set_angle(self.obj, c.c_float(angle))

    def apply(self):
        """ Ensures the actuator will be running for this step."""
        _pal.lib.actuator_hydrofoil_apply(self.obj)
