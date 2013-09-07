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

class Hydrofoil(Impulse):
    def __init__(body,pos,direction,lift_vector,area,a,b,c,density):
        """
        applies an hydrofoil to a body
        
    	body: The body to connect the actuator to
	    pos: The x position of the actuator's center
	    direction: The unit vector which supplies the orientation of the actuator.
	    lift_vector: the direction in which the lift force is applied
	    area 	The frontal area of the hydrofoil.
	    a 	The quadratic term of the lift coefficient
	    b 	The linear term of the lift coefficient
	    c 	The constant term of the lift coefficient
	    density 	The density of the liquid. 
        """
        pass

    def set_angle(angle):
        """sets the angle of attack of the actuator in range-pi/2 to pi/2"""

    def run():
        """ensures the actuator will be running for this step."""
        pass

class Propeller(Impulse):
    def __init__(body,pos,direction,lumped):
        """
        applies an propeller to a body
        
    	body: The body to connect the actuator to
	    pos: The x position of the actuator's center
	    direction: The unit vector which supplies the orientation of the actuator.
	    lumped: The lumped parameter 
        """
        pass

    def set_voltage(voltage):
        """sets the voltage of the actuator"""

    def run():
        """ensures the actuator will be running for this step."""
        pass
