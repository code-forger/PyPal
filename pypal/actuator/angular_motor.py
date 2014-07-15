from pypal import private_globals as _pal
import ctypes as c
import weakref
from actuatorbase import ActuatorBase
import action
class AngularMotor(ActuatorBase):
    def __init__(self,link,max):
        self.obj = _pal.lib.actuator_angular_motor_create(link.obj,c.c_float(max))

    def update(self, target_velocity):
        """ensures the actuator will be running for this step."""
        _pal.lib.actuator_dcmotor_apply(self.obj, c.c_int(target_velocity))

    def turn_on(self, target_velocity):
        self.action = action.Action("Actuator " + str(self.obj),
                                    self.update, target_velocity)
        self.action.run()

    def turn_off(self):
        try:
            self.action.pause()
            self.action = None
        except:
            pass
