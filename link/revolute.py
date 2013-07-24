import private_globals as pal
import ctypes as c
import weakref
class Revolute(pal.PalObject):
    """a link that connects two objects rotationally"""
    def _create(self,parent,child,pos,direction,collide):
        self.obj = pal.lib.create_revolute(parent.obj,child.obj,c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),c.c_float(direction[0]),c.c_float(direction[1]),c.c_float(direction[2]),c.c_bool(collide))

    def set_limits(self,lower,upper):
        """
        sets the maximum and the minimum rotational angle of the link in radians
        lower: the minimum angle
        upper: the maximum angle
        """
        pal.lib.revolute_link_set_limits(self.obj,c.c_float(lower),c.c_float(upper))

    def get_position(self):
        """
        returns the position of the link
        """
        pos = [c.c_float() for x in range(3)]
        pal.lib.revolute_link_get_position(self.obj,c.byref(pos[0]),c.byref(pos[1]),c.byref(pos[2]))
        return [p.value for p in pos]

    def get_angle(self):
        """
        returns the angle of the link
        """
        pal.lib.revolute_link_get_angle.restype = c.c_float
        return pal.lib.revolute_link_get_angle(self.obj)
        

    def get_angular_velocity(self):
        """
        returns the angular velocity of the link
        """
        pal.lib.revolute_link_get_angular_velocity.restype = c.c_float
        return pal.lib.revolute_link_get_angular_velocity(self.obj)

    def apply_torque(self,torque):
        """
        applies a torque to the childabout the link
        torque: a floating point value
        """
        pal.lib.revolute_link_apply_torque(self.obj, c.c_float(torque))

    def apply_angular_impulse(self,torque):
        """
        applies a torque to the childabout the link
        torque: a floating point value
        """
        pal.lib.revolute_link_apply_angular_impulse(self.obj, c.c_float(torque))

    def get_axis(self):
        """
        returns the position of the link
        """
        pos = [c.c_float() for x in range(3)]
        pal.lib.revolute_link_get_axis(self.obj,c.byref(pos[0]),c.byref(pos[1]),c.byref(pos[2]))
        return [p.value for p in pos]

    def delete(self):
        pal.lib.revolute_link_remove(self.obj)
        del pal.all_objects[str(self.obj)]
