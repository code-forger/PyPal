from pypal import private_globals as _pal
import ctypes as c
import weakref
class Revolute(_pal.PalObject):
    """ A link that connects two objects rotationally. """
    def __init__(self,parent,child,pos,direction,collide):
        """
        Parameters:
          parent: ``pypal.body`` The first body who is part of the link.
          child: ``pypal.body`` The second body who is part of the link.
          pos: ``float[3]`` The center of the link.
          direction: ``float[3]`` The direction unit vector for the movement of the link.
          collide: ``bool`` Weather or not the bodies involved in the link should coolide with each other.
        """
        self.obj = _pal.lib.link_revolute_create(parent.obj,child.obj,c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),c.c_float(direction[0]),c.c_float(direction[1]),c.c_float(direction[2]),c.c_bool(collide))

    def set_limits(self,lower,upper):
        """
        Sets limits on the link

        Parameters:
          max_limit: ``float`` The maximum angle the child body can rotate.
          min_limit: ``float`` The minimum angle the child body can rotate.
        """
        _pal.lib.link_revolute_set_limits(self.obj,c.c_float(lower),c.c_float(upper))

    def get_position(self):
        """ Returns the position of the link. """
        ret = _pal.Vec3()
        _pal.lib.link_revolute_get_position(self.obj, ret)
        return [x for x in ret]

    def get_angle(self):
        """ Returns the angle of the link. """
        _pal.lib.link_revolute_get_angle.restype = c.c_float
        return _pal.lib.link_revolute_get_angle(self.obj)
        

    def get_angular_velocity(self):
        """ Returns the angular velocity of the link. """
        _pal.lib.link_revolute_get_angular_velocity.restype = c.c_float
        return _pal.lib.link_revolute_get_angular_velocity(self.obj)

    def apply_torque(self, torque):
        """
        Applies a torque to the childabout the link.

        Parameters:
          torque: ``float`` The torque to apply rotationally to this link.
        """
        _pal.lib.link_revolute_apply_torque(self.obj, c.c_float(torque))

    def apply_angular_impulse(self,torque):
        """
        Applies an angular impulse to the childabout the link.

        Parameters:
          torque: ``float`` The angular impulse to apply rotationally to this link.
        """
        _pal.lib.link_revolute_apply_angular_impulse(self.obj, c.c_float(torque))

    def get_axis(self):
        """ Returns the axis of the link. """
        ret = _pal.Vec3()
        _pal.lib.link_revolute_get_axis(self.obj, ret)
        return [x for x in ret]