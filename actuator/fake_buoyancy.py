from pypalgame import private_globals as pal
import ctypes as c
import weakref
from actuatorbase import ActuatorBase
class FakeBuoyancy(ActuatorBase):
    def __init__(self,body,density=998.29):
        """
        applies an impulse to a body
        
        body: The body to connect the actuator to
        pos: The x position of the actuator's center impulse for the actuator to apply, if none is set the actuator will do nothing
        """
        self.obj = pal.lib.create_fake_buoyancy(body.obj,c.c_char(body.typechar),c.c_float(density))

    def delete(self):
        pal.lib.fake_buoyancy_remove(self.obj)
        del pal.all_objects[str(obj)]

    def run(self):
        """ensures the actuator will be running for this step."""
        pal.lib.fake_buoyancy_run(self.obj)
