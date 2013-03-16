class Impulse():
    def __init__(body,pos,direction,impulse=None):
        """
        applies an impulse to a body
        
    	body: The body to connect the actuator to
	    pos: The x position of the actuator's center
	    direction: The unit vector which supplies the direction of the actuator's impulse.
	    impulse: the impulse for the actuator to apply, if none is set the actuator will do nothing
        """
        pass

    def set_impulse(impulse):
        """sets the impulse of the actuator"""

    def run():
        """ensures the actuator will be running for this step."""
        pass

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
