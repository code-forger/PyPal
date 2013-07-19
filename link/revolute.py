import private_globals as pal
import ctypes as c
import weakref
class Revolute(object):
    """a link that connects two objects rotationally"""
    def __new__(cls,parent,child,pos,direction,collide):
        """
        constructs a revolate link and adds it to the world
        
        rect: a 6 part tuple with x,y,z,width,height,depth.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        static: used to create this object static, if static is true, mass will be ignored
        """
        link = super(Revolute,cls).__new__(cls)
        link._create(parent,child,pos,direction,collide)
        pal.all_objects[str(link.obj)] = link
        return weakref.proxy(link)

    def _create(self,parent,child,pos,direction,collide):
        self.obj = pal.lib.create_revolute(parent.obj,child.obj,c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),c.c_float(direction[0]),c.c_float(direction[1]),c.c_float(direction[2]),c.c_bool(collide))

    def set_limits(self,lower,upper):
        """
        sets the maximum and the minimum rotational angle of the link in radians
        lower: the minimum angle
        upper: the maximum angle
        """
        pal.lib.revolute_set_limits(self.obj,c.c_float(lower),c.c_float(upper))

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

    def delete(self):
        pal.lib.revolute_link_remove(self.obj)
        del pal.all_objects[str(self.obj)]
