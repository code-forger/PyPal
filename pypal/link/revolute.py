from pypal import private_globals as _pal
import ctypes as c
import weakref
class Revolute(_pal.PalObject):
    """a link that connects two objects rotationally"""
    def __init__(self,parent,child,pos,direction,collide):
        self.obj = _pal.lib.link_revolute_create(parent.obj,child.obj,c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),c.c_float(direction[0]),c.c_float(direction[1]),c.c_float(direction[2]),c.c_bool(collide))

    def set_limits(self,lower,upper):
        """
        sets the maximum and the minimum rotational angle of the link in radians
        lower: the minimum angle
        upper: the maximum angle
        """
        _pal.lib.link_revolute_set_limits(self.obj,c.c_float(lower),c.c_float(upper))

    def get_position(self):
        """
        returns the position of the link
        """
        ret = _pal.Vec3()
        _pal.lib.link_revolute_get_position(self.obj, ret)
        return [x for x in ret]

    def get_angle(self):
        """
        returns the angle of the link
        """
        _pal.lib.link_revolute_get_angle.restype = c.c_float
        return _pal.lib.link_revolute_get_angle(self.obj)
        

    def get_angular_velocity(self):
        """
        returns the angular velocity of the link
        """
        _pal.lib.link_revolute_get_angular_velocity.restype = c.c_float
        return _pal.lib.link_revolute_get_angular_velocity(self.obj)

    def apply_torque(self,torque):
        """
        applies a torque to the childabout the link
        torque: a floating point value
        """
        _pal.lib.link_revolute_apply_torque(self.obj, c.c_float(torque))

    def apply_angular_impulse(self,torque):
        """
        applies a torque to the childabout the link
        torque: a floating point value
        """
        _pal.lib.link_revolute_apply_angular_impulse(self.obj, c.c_float(torque))

    def get_axis(self):
        """
        returns the position of the link
        """
        ret = _pal.Vec3()
        _pal.lib.link_revolute_get_axis(self.obj, ret)
        return [x for x in ret]