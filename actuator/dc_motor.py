import private_globals as pal
import ctypes as c
import weakref
class DCMotor(object):
    def __new__(cls,link,torque,emf,resistance):
        """
        constructs a revolate link and adds it to the world
        
        rect: a 6 part tuple with x,y,z,width,height,depth.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        static: used to create this object static, if static is true, mass will be ignored
        """
        motor = super(DCMotor,cls).__new__(cls)
        motor._create(link,torque,emf,resistance)
        pal.all_objects[str(motor.obj)] = motor
        return weakref.proxy(motor)

    def _create(self,link,torque,emf,resistance):
        self.obj = pal.lib.create_dcmotor(link.obj,c.c_float(torque),c.c_float(emf),c.c_float(resistance))

    def set_voltage(self,voltage):
        """sets the voltage of the motor"""
        pal.lib.dcmotor_set_voltage(self.obj,c.c_float(voltage))

    def run(self):
        """ensures the actuator will be running for this step."""
        pal.lib.dcmotor_run(self.obj)

    def delete(self):
        pal.lib.dcmotor_remove(self.obj)
        del pal.all_objects[str(obj)]
