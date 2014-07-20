from pypal import private_globals as _pal
import ctypes as c
import weakref
class BodyBase(_pal.PalObject):
    def get_location(self):
        """ Return the location of the body as a ``float[16]`` matrix. """
        ret = _pal.Mat4x4()
        _pal.lib.body_base_get_location(self._body_base, ret)
        return [x for x in ret]

    def get_position(self):
        """ Return position of the body as the ``float[3]`` x, y, z components. """
        ret = _pal.Vec3()
        _pal.lib.body_base_get_position(self._body_base, ret)
        return [x for x in ret]

    def set_material(self, material):
        """ 
        Sets the collision material of the body.

        Parameters:
          material: ``pypal.material.Material`` The material to be set for collisions.
        """
        _pal.lib.body_base_set_material(self._body_base, material.obj)

    def get_group(self):
        """ Return collision group of the body as a ``float``. """
        return _pal.lib.body_base_get_group(self._body_base)

    def set_group(self, group):
        """
        Set the collision group of the body

        Parameters:
          group: ``int`` The group to be set.
        """
        return _pal.lib.body_base_set_group(self._body_base, c.c_int(group))
