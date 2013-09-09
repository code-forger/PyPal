from pypalgame import private_globals as pal
import ctypes as c
import weakref
from actuatorbase import ActuatorBase
class DCMotor(ActuatorBase):
    def __init__(self,link,torque,emf,resistance):
        self.obj = pal.lib.create_dcmotor(link.obj,c.c_float(torque),c.c_float(emf),c.c_float(resistance))

    def set_voltage(self,voltage):
        """sets the voltage of the motor"""
        pal.lib.dcmotor_set_voltage(self.obj,c.c_float(voltage))

    def run(self):
        """ensures the actuator will be running for this step."""
        pal.lib.dcmotor_run(self.obj)
