from pypal import private_globals as _pal
import ctypes as c
import weakref
from actuatorbase import ActuatorBase
import action
class AngularMotor(ActuatorBase):
    """ A motor on a revolute link that maintains a target velocity. """
    def __init__(self, link, max):
        """
        Parameters:
          link: ``pypal.link.Revolute`` The link that the actuator will work upon.
          max: ``float`` The maximum angular velocity this motor should allow.
        """
        self.obj = _pal.lib.actuator_angular_motor_create(link.obj,c.c_float(max))

    def update(self, target_velocity):
        """
        Ensure the actuator will be running for this step.

        Parameters:
          target_velocity: ``float`` The target velocity for this step.
        """
        _pal.lib.actuator_angular_motor_update(self.obj, c.c_float(target_velocity))

    def turn_on(self, target_velocity):
        """
        Ensure this actuator is applied every step.

        Parameters:
          target_velocity: ``float`` The target velocity that should be maintained every step.
        
        """
        self.action = action.Action("Actuator " + str(self.obj),
                                    self.update, target_velocity)
        self.action.run()