from pypal import private_globals as _pal
import ctypes as c
import weakref
from actuatorbase import ActuatorBase
class DCMotor(ActuatorBase):
    def __init__(self,link,torque,emf,resistance):
        self.obj = _pal.lib.actuator_dcmotor_create(link.obj,c.c_float(torque),c.c_float(emf),c.c_float(resistance))

    def set_voltage(self,voltage):
        """sets the voltage of the motor"""
        _pal.lib.actuator_dcmotor_set_voltage(self.obj,c.c_float(voltage))

    def apply(self):
        """ensures the actuator will be running for this step."""
        _pal.lib.actuator_dcmotor_apply(self.obj)
