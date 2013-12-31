from pypal import private_globals as pal
import ctypes as c
import weakref
from actuatorbase import ActuatorBase
class Force(ActuatorBase):
    def __init__(self,body,pos,direction,force=None):
        """
        applies an force to a body
        
        body: The body to connect the actuator to
        pos: The x position of the actuator's center
        direction: The unit vector which supplies the direction of the actuator's impulse.
        force: the force for the actuator to apply, if none is set the actuator will do nothing
        """
        self.obj = pal.lib.create_force(body.obj,c.c_char(body.typechar),c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),
                                         c.c_float(direction[0]),c.c_float(direction[1]),c.c_float(direction[2]))
        if force:
            self.set_force(force)

    def set_force(self,force):
        """sets the force of the actuator"""
        pal.lib.force_set_force(self.obj,c.c_float(force))

    def run(self):
        """ensures the actuator will be running for this step."""
        pal.lib.force_run(self.obj)
