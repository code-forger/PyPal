from pypalgame import private_globals as pal
import ctypes as c
import weakref
from actuatorbase import ActuatorBase
class Impulse(ActuatorBase):
    def __init__(self,body,pos,direction,impulse=None):
        """
        applies an impulse to a body
        
        body: The body to connect the actuator to
        pos: The x position of the actuator's center
        direction: The unit vector which supplies the direction of the actuator's impulse.
        impulse: the impulse for the actuator to apply, if none is set the actuator will do nothing
        """
        self.obj = pal.lib.create_impulse(body.obj,c.c_char(body.typechar),c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),
                                         c.c_float(direction[0]),c.c_float(direction[1]),c.c_float(direction[2]))
        if impulse:
            self.set_impulse(impulse)

    def set_impulse(self,impulse):
        """sets the impulse of the actuator"""
        pal.lib.impulse_set_impulse(self.obj,c.c_float(impulse))

    def delete(self):
        pal.lib.impulse_remove(self.obj)
        del pal.all_objects[str(obj)]

    def run(self):
        """ensures the actuator will be running for this step."""
        pal.lib.impulse_run(self.obj)
