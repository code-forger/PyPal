from pypal import private_globals as _pal
import ctypes as c
import weakref
class Capsule(_pal.PalObject):
    def __init__(self, pos, size, mass = 1.):
        """
        constructs a capsule and adds it to the world
        
        pos: a 3 part tuple with x,y,z.
        size: a 3 part tuple with width, height, depth
        mass: the mass of the object, if mass is specified it will be used.
        """
        self._size = size
        self.obj = _pal.lib.body_capsule_create(c.c_float(pos[0]),c.c_float(pos[1]),c.c_float(pos[2]),c.c_float(size[0]),c.c_float(size[1]),c.c_float(mass))

    def get_location(self):
        ret = _pal.Mat4x4()
        _pal.lib.body_capsule_get_location(self.obj, ret)
        return [x for x in ret]

    def get_position(self):
        ret = _pal.Vec3()
        _pal.lib.body_capsule_get_position(self.obj, ret)
        return [x for x in ret]

    def set_material(self, material):
        _pal.lib.body_capsule_set_material(self.obj, material.obj)

    def get_group(self):
        return _pal.lib.body_capsule_get_group(self.obj)

    def set_group(self, group):
        return _pal.lib.body_capsule_set_group(self.obj, c.c_int(group))

    def __str__(self):
        x, y, z = self.get_position()
        return "A Capsule at : %.2f, %.2f, %.2f" % (x, y, z)

    def set_position(self, pos, rot=(0, 0, 0)):
        """Sets the position of the object and its orientation."""
        _pal.lib.body_capsule_set_position(self.obj, c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]), c.c_float(rot[0]), c.c_float(rot[1]), c.c_float(rot[2]))

    def set_orientation(self, rot):
        """Sets the position of the object and/or its orientation."""
        _pal.lib.body_capsule_set_orientation(self.obj, c.c_float(rot[0]), c.c_float(rot[1]), c.c_float(rot[2]))

    def apply_force(self, force, pos=None):
        """Applies a force to the object for a single step at an optional offset in world coordinates."""
        if pos:
            _pal.lib.body_capsule_apply_force_at_position(self.obj, c.c_float(force[0]), c.c_float(force[1]), c.c_float(force[2]),
                                                          c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]))
        else:
            _pal.lib.body_capsule_apply_force(self.obj, c.c_float(force[0]), c.c_float(force[1]), c.c_float(force[2]))

    def apply_torque(self, force):
        """Applies a torque to the object for a single step."""
        _pal.lib.body_capsule_apply_torque(self.obj, c.c_float(force[0]), c.c_float(force[1]), c.c_float(force[2]))

    def apply_impulse(self, impulse,pos=None):
        """Applies an impulse to the object for a single step at an optional offset in world coordinates."""
        if pos:
            _pal.lib.body_capsule_apply_impulse_at_position(self.obj, c.c_float(impulse[0]), c.c_float(impulse[1]), c.c_float(impulse[2]),
                                                                 c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]))
        else:
            _pal.lib.body_capsule_apply_impulse(self.obj, c.c_float(impulse[0]), c.c_float(impulse[1]), c.c_float(impulse[2]))

    def apply_angular_impulse(self, impulse):
        """Applies an angular impulse to the object for a single step at an optional offset in world coordinates."""
        _pal.lib.body_capsule_apply_angular_impulse(self.obj, c.c_float(impulse[0]), c.c_float(impulse[1]), c.c_float(impulse[2]))


    def get_linear_velocity(self):
        """Returns the linear velocity of the body."""
        ret = _pal.Vec3()
        _pal.lib.body_capsule_get_linear_velocity(self.obj, ret)
        return [x for x in ret]

    def get_angular_velocity(self):
        """Returns the linear velocity of the body."""
        ret = _pal.Vec3()
        _pal.lib.body_capsule_get_angular_velocity(self.obj, ret)
        return [x for x in ret]

    def set_linear_velocity(self, velocity):
        """sets the linear velocity og the object"""
        vec = _pal.Vec3()
        for i in range(3):
            vec[i] = velocity[i]
        _pal.lib.body_capsule_set_linear_velocity(self.obj, vec)

    def set_angular_velocity(self, velocity):
        """sets the angular velocity og the object"""
        vec = _pal.Vec3()
        for i in range(3):
            vec[i] = velocity[i]
        _pal.lib.body_capsule_set_angular_velocity(self.obj, vec)
        
    def is_active(self):
        """Returns true if the body is not asleep."""
        _pal.lib.body_capsule_is_active.restype = c.c_bool
        return _pal.lib.body_capsule_is_active(self.obj)

    def set_active(self,active):
        """Sets the body to active or not."""
        _pal.lib.body_capsule_set_active(self.obj, c.c_bool(active))

    def get_size(self):
        """returns the size of the object in a 3 part tuple"""
        return self._size