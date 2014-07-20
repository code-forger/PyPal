from pypal import private_globals as _pal
import ctypes as c
import weakref
import pypal.geometry as libgeometry
from body import Body
class GenericBody(Body):
    """
    A Generic Body.

    The Generic body is a very flexible body that supports switching between modes on the fly.

    Note: If you want a generic body to be static, you must set:
      A: The dynamic_type to "static
      B: The mass to 0
      C: The mass of all connected geometries to 0
    """
    def __init__(self, pos, rotation=[0,0,0]):
        """
        Parameters:
          pos: ``float[3]`` The x, y, z, position of the Generic Body.
          rotation: ``float[3]`` The rx, ry, rz, rotation of the Generic Body.
        """
        self.obj = _pal.lib.body_create_generic(c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]),
                                          c.c_float(rotation[0]), c.c_float(rotation[1]), c.c_float(rotation[2]))
        self._geometries = []
        self._body_base = _pal.lib.cast_generic_body_base(self.obj)
        self._body = _pal.lib.cast_generic_body(self.obj)

    def __str__(self):
        x, y, z = self.get_position()
        return "A Generic at : %.2f, %.2f, %.2f" % (x, y, z)

    @property
    def dynamics_type(self):
        """
        A Property to get or set the dynamic type.
        
        Parameters:
          dyn_type: A string with the value: ``"dynamic", "static" or "kinematic"`` This will change the dynamic type of the body.
        """
        return self._dynamics_type

    @dynamics_type.setter
    def dynamics_type(self,dyn_type):
        char = {"dynamic":'d', "static":'c', "kinematic":'k'}[dyn_type]
        _pal.lib.body_generic_set_dynamics_type(self.obj, c.c_char(char))
        self._dynamics_type = dyn_type

    @property
    def gravity_enabled(self):
        """
        A Property to get or set the gravity settings for this body.

        Parameters
           enabled: ``bool`` Enables or dissables gravity for the body.
        """
        return self._gravity_enabled

    @gravity_enabled.setter
    def gravity_enabled(self,enabled):
        if enabled in [True, False]:
            _pal.lib.body_generic_set_gravity_enabled(self.obj, c.c_bool(enabled))
            self._gravity_enabled = enabled

    @property
    def collision_response(self):
        """
        A Property to get or set the collision response for this body.

        Parameters:
          enabled: ``bool`` Enables or dissables collision response for the body.
            Note: Even if the collisions are dissabled, the collision detection will still report the collisions to have happened.
        """
        return self._collision_response_enabled

    @collision_response.setter
    def collision_response(self,enabled):
        if enabled in [True, False]:
            _pal.lib.body_generic_set_collision_response_enabled(self.obj, c.c_bool(enabled))
            self._collision_response_enabled = enabled

    @property
    def mass(self):
        """
        A Property to get or set the mass of the body.

        Parameters:
          mass: ``float`` The mass of the body.
        """
        return self._mass

    @mass.setter
    def mass(self, mass):
        _pal.lib.body_generic_set_mass(self.obj, c.c_float(mass))
        self._mass = mass

    @property
    def inertia(self):
        """
        A Property to get or set the inertia of the body.

        Parameters:
          inertia: ``float[3]`` The x, y, a inertia of the body.
        """
        inertia = [c.c_float() for x in range(3)]
        _pal.lib.body_generic_get_inertia(self.obj,c.byref(inertia[0]),c.byref(inertia[1]),c.byref(inertia[2]))
        return [p.value for p in inertia]

    @inertia.setter
    def inertia(self, inertia):
        _pal.lib.body_generic_set_inertia(self.obj,c.c_float(inertia[0]),c.c_float(inertia[1]),c.c_float(inertia[2]))

    @property
    def linear_damping(self):
        """
        A Property to get or set the the linear damping of the body.

        Parameters:
          damping: ``float`` The linear damping of the body
        """
        _pal.lib.body_generic_get_linear_damping.restype = c.c_float
        return _pal.lib.body_generic_get_linear_damping(self.obj)

    @linear_damping.setter
    def linear_damping(self, damping):
        _pal.lib.body_generic_set_linear_damping(self.obj, c.c_float(damping))

    @property
    def angular_damping(self):
        """
        A Property to get or set the angular damping of the body.

        Paramters:
          damping: ``float`` The angular damping of the body.
        """
        _pal.lib.body_generic_get_angular_damping.restype = c.c_float
        return _pal.lib.body_generic_get_angular_damping(self.obj)

    @angular_damping.setter
    def angular_damping(self, damping):
        _pal.lib.body_generic_set_angular_damping(self.obj, c.c_float(damping))

    def connect_geometry(self, geometry):
        """
        Connects a geometry to the body.

        Parameters:
          geometry: ``pypal.geometry`` a pre initialised geometry.
        """
        _pal.lib.body_generic_connect_geometry(self.obj, geometry._geometry)
        self._geometries.append(geometry)

    def remove_geometry(self, geometry):
        """
        Removes a geometry from the body.

        Parameters:
          geometry: ``papal.geometry`` A geometry that has been added that should be removed.
        """
        if geometry in self._geometries:
            _pal.lib.body_generic_remove_geometry(self.obj, geometry.obj)
            self._geometries.remove(geometry)

    def get_geometries(self):
        """
        Returns a copy of the geometry list.

        Note: This is a copy of the geometry list, it cannot be used to modify the body, please use :func:`remove_geometry` and :func:`connect_geometry` to modify the geometries.
        """
        return list(self._geometries)

    
