import private_globals as pal
import ctypes as c
import weakref
class Revolute():
    """a link that connects two objects rotationally"""
    @classmethod
    def create(self,parent,child,pos,direction):
        """
        constructs a revolate link and adds it to the world
        
        rect: a 6 part tuple with x,y,z,width,height,depth.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        static: used to create this object static, if static is true, mass will be ignored
        """
        link = Revolute(parent,child,pos,direction)
        pal.all_objects[str(pal.all_next)] = link
        pal.lib.body_set_data(link.obj,pal.all_next)
        pal.all_next += 1
        return weakref.proxy(link)

    def __init__(self,parent,child,pos,direction):
        """
        connects two objects together

        parent: the parent body
        child: the child body
        pos: a 3 part tuple for the position of the link
        direction: a 3 part unit vector of the driection of the link
        """
        self.obj = pal.lib.create_revolute(parent.obj,child.obj,c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),c.c_float(direction[0]),c.c_float(direction[1]),c.c_float(direction[2]),)

    def set_limits(lower,upper):
        """
        sets the maximum and the minimum rotational angle of the link in radians
        lower: the minimum angle
        upper: the maximum angle
        """
        pass

    def get_position():
        """
        returns the position of the link
        """

    def get_angle():
        """
        returns the angle of the link
        """
        pass

    def get_angular_velocity():
        """
        returns the angular velocity of the link
        """
        pass

    def apple_torque(torque):
        """
        applies a torque to the childabout the link
        torque: a floating point value
        """
        pass

    def apply_angular_impulse(torque):
        """
        applies a torque to the childabout the link
        torque: a floating point value
        """
        pass
