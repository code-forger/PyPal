from pypal import private_globals as _pal
import ctypes as c
import weakref
from actuatorbase import ActuatorBase
class DCMotor(ActuatorBase):
    """ A motor on a revolute link that simulates a DC motor """
    def __init__(self,link,torque,emf,resistance):
        """
        Parameters:
          link: ``pypal.link.Revolute`` The link that the actuator will work upon.
          torque: ``float`` The torque of the motor.
          emf: ``float`` The back emf of the motor.
          resistance: ``float`` The armature resistance.
        """
        self.obj = _pal.lib.actuator_dcmotor_create(link.obj,c.c_float(torque),c.c_float(emf),c.c_float(resistance))

    def set_voltage(self, voltage):
        """
        Sets the voltage of the motor

        Parameters:
          voltage: ``float`` The voltage to apply to the motor.
        """
        _pal.lib.actuator_dcmotor_set_voltage(self.obj,c.c_float(voltage))

    def apply(self):
        """ Ensures the actuator will be running for this step. """
        _pal.lib.actuator_dcmotor_apply(self.obj)
