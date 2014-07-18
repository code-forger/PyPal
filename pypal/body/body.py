from pypal import private_globals as _pal
import ctypes as c
import weakref
from bodybase import BodyBase
class Body(BodyBase):
    def set_position(self, pos, rot=(0, 0, 0)):
        """
        Sets the position of the object and its orientation.

        Parameters:
          pos: ``float[3]`` The x, y, z, position of the body.
          rot: ``float[3]`` The rx, ry, rz, rotation of the body.
        """
        _pal.lib.body_set_position(self._body, c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]), c.c_float(rot[0]), c.c_float(rot[1]), c.c_float(rot[2]))

    def set_orientation(self, rot):
        """
        Sets the rotation of the object.

        Parameters:
          rot: ``float[3]`` The rx, ry, rz, rotation of the body.
        """
        _pal.lib.body_set_orientation(self._body, c.c_float(rot[0]), c.c_float(rot[1]), c.c_float(rot[2]))

    def apply_force(self, force, pos=None):
        """
        Applies a force to the object for a single step at an optional offset in world coordinates.

        Parameters:
          force: ``float[3]`` The x, y, z, force vector to be applied body.
          pos: ``float[3]`` The optional x, y, z, offset to apply the force at.
        """
        if pos:
            _pal.lib.body_apply_force_at_position(self._body, c.c_float(force[0]), c.c_float(force[1]), c.c_float(force[2]),
                                                          c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]))
        else:
            _pal.lib.body_apply_force(self._body, c.c_float(force[0]), c.c_float(force[1]), c.c_float(force[2]))

    def apply_torque(self, force):
        """Applies a torque to the object for a single step."""
        _pal.lib.body_apply_torque(self._body, c.c_float(force[0]), c.c_float(force[1]), c.c_float(force[2]))

    def apply_impulse(self, impulse, pos=None):
        """
        Applies an impulse to the object for a single step at an optional offset in world coordinates.

        Parameters:
          impulse: ``float[3]`` The x, y, z, imulse vector to be applied body.
          pos: ``float[3]`` The optional x, y, z, offset to apply the impulse at.
        """
        if pos:
            _pal.lib.body_apply_impulse_at_position(self._body, c.c_float(impulse[0]), c.c_float(impulse[1]), c.c_float(impulse[2]),
                                                                 c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]))
        else:
            _pal.lib.body_apply_impulse(self._body, c.c_float(impulse[0]), c.c_float(impulse[1]), c.c_float(impulse[2]))

    def apply_angular_impulse(self, impulse):
        """Applies an angular impulse to the object for a single step at an optional offset in world coordinates."""
        _pal.lib.body_apply_angular_impulse(self._body, c.c_float(impulse[0]), c.c_float(impulse[1]), c.c_float(impulse[2]))


    def get_linear_velocity(self):
        """Returns the linear velocity of the body."""
        ret = _pal.Vec3()
        _pal.lib.body_get_linear_velocity(self._body, ret)
        return [x for x in ret]

    def get_angular_velocity(self):
        """Returns the linear velocity of the body."""
        ret = _pal.Vec3()
        _pal.lib.body_get_angular_velocity(self._body, ret)
        return [x for x in ret]

    def set_linear_velocity(self, velocity):
        """sets the linear velocity og the object"""
        vec = _pal.Vec3()
        for i in range(3):
            vec[i] = velocity[i]
        _pal.lib.body_set_linear_velocity(self._body, vec)

    def set_angular_velocity(self, velocity):
        """sets the angular velocity og the object"""
        vec = _pal.Vec3()
        for i in range(3):
            vec[i] = velocity[i]
        _pal.lib.body_set_angular_velocity(self._body, vec)
        
    def is_active(self):
        """Returns true if the body is not asleep."""
        _pal.lib.body_is_active.restype = c.c_bool
        return _pal.lib.body_is_active(self._body)

    def set_active(self,active):
        """Sets the body to active or not."""
        _pal.lib.body_set_active(self._body, c.c_bool(active))