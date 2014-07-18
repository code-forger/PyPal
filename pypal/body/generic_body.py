from pypal import private_globals as _pal
import ctypes as c
import weakref
import pypal.geometry as libgeometry
class GenericBody(_pal.PalObject):
    typechar = 'g'
    def __init__(self, pos, rotation=[0,0,0]):
        """
        constructs a generic and adds it to the world
        
        rect: a 3 part tuple with x,y,z.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        """
        self.obj = _pal.lib.body_create_generic(c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]),
                                          c.c_float(rotation[0]), c.c_float(rotation[1]), c.c_float(rotation[2]))
        self._geometries = []

    def get_location(self):
        """ Return the location of the body as a ``float[16]`` matrix. """
        ret = _pal.Mat4x4()
        _pal.lib.body_generic_get_location(self.obj, ret)
        return [x for x in ret]

    def get_position(self):
        """ Return position of the body as the ``float[3]`` x, y, z components. """
        ret = _pal.Vec3()
        _pal.lib.body_generic_get_position(self.obj, ret)
        return [x for x in ret]

    def set_material(self, material):
        _pal.lib.body_generic_set_material(self.obj, material.obj)

    def get_group(self):
        """ Return collision group of the body as a ``float``. """
        return _pal.lib.body_generic_get_group(self.obj)

    def set_group(self, group):
        return _pal.lib.body_generic_set_group(self.obj, c.c_int(group))

    def __str__(self):
        x, y, z = self.get_position()
        return "A Generic at : %.2f, %.2f, %.2f" % (x, y, z)

    def set_position(self, pos, rot=(0, 0, 0)):
        """
        Sets the position of the object and its orientation.

        Parameters:
          pos: ``float[3]`` The x, y, z, position of the body.
          rot: ``float[3]`` The rx, ry, rz, rotation of the body.
        """
        _pal.lib.body_generic_set_position(self.obj, c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]), c.c_float(rot[0]), c.c_float(rot[1]), c.c_float(rot[2]))

    def set_orientation(self, rot):
        """
        Sets the rotation of the object.

        Parameters:
          rot: ``float[3]`` The rx, ry, rz, rotation of the body.
        """
        _pal.lib.body_generic_set_orientation(self.obj, c.c_float(rot[0]), c.c_float(rot[1]), c.c_float(rot[2]))

    def apply_force(self, force, pos=None):
        """
        Applies a force to the object for a single step at an optional offset in world coordinates.

        Parameters:
          force: ``float[3]`` The x, y, z, force vector to be applied body.
          pos: ``float[3]`` The optional x, y, z, offset to apply the force at.
        """
        if pos:
            _pal.lib.body_generic_apply_force_at_position(self.obj, c.c_float(force[0]), c.c_float(force[1]), c.c_float(force[2]),
                                                          c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]))
        else:
            _pal.lib.body_generic_apply_force(self.obj, c.c_float(force[0]), c.c_float(force[1]), c.c_float(force[2]))

    def apply_torque(self, force):
        """Applies a torque to the object for a single step."""
        _pal.lib.body_generic_apply_torque(self.obj, c.c_float(force[0]), c.c_float(force[1]), c.c_float(force[2]))

    def apply_impulse(self, impulse, pos=None):
        """
        Applies an impulse to the object for a single step at an optional offset in world coordinates.

        Parameters:
          impulse: ``float[3]`` The x, y, z, imulse vector to be applied body.
          pos: ``float[3]`` The optional x, y, z, offset to apply the impulse at.
        """
        if pos:
            _pal.lib.body_generic_apply_impulse_at_position(self.obj, c.c_float(impulse[0]), c.c_float(impulse[1]), c.c_float(impulse[2]),
                                                                 c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]))
        else:
            _pal.lib.body_generic_apply_impulse(self.obj, c.c_float(impulse[0]), c.c_float(impulse[1]), c.c_float(impulse[2]))

    def apply_angular_impulse(self, impulse):
        """Applies an angular impulse to the object for a single step at an optional offset in world coordinates."""
        _pal.lib.body_generic_apply_angular_impulse(self.obj, c.c_float(impulse[0]), c.c_float(impulse[1]), c.c_float(impulse[2]))


    def get_linear_velocity(self):
        """Returns the linear velocity of the body."""
        ret = _pal.Vec3()
        _pal.lib.body_generic_get_linear_velocity(self.obj, ret)
        return [x for x in ret]

    def get_angular_velocity(self):
        """Returns the linear velocity of the body."""
        ret = _pal.Vec3()
        _pal.lib.body_generic_get_angular_velocity(self.obj, ret)
        return [x for x in ret]

    def set_linear_velocity(self, velocity):
        """sets the linear velocity og the object"""
        vec = _pal.Vec3()
        for i in range(3):
            vec[i] = velocity[i]
        _pal.lib.body_generic_set_linear_velocity(self.obj, vec)

    def set_angular_velocity(self, velocity):
        """sets the angular velocity og the object"""
        vec = _pal.Vec3()
        for i in range(3):
            vec[i] = velocity[i]
        _pal.lib.body_generic_set_angular_velocity(self.obj, vec)
        
    def is_active(self):
        """Returns true if the body is not asleep."""
        _pal.lib.body_generic_is_active.restype = c.c_bool
        return _pal.lib.body_generic_is_active(self.obj)

    def set_active(self,active):
        """Sets the body to active or not."""
        _pal.lib.body_generic_set_active(self.obj, c.c_bool(active))

    @property
    def dynamics_type(self):
        return self._dynamics_type

    @dynamics_type.setter
    def dynamics_type(self,dyn_type):
        """
        Sets the body to dynamic, static, or kinematic
        
        dynType: "dynamic", "static" or "kinematic"
        """
        char = {"dynamic":'d', "static":'c', "kinematic":'k'}[dyn_type]
        _pal.lib.body_generic_set_dynamics_type(self.obj, c.c_char(char))
        self._dynamics_type = dyn_type

    @property
    def gravity_enabled(self):
        return self._gravity_enabled

    @gravity_enabled.setter
    def gravity_enabled(self,enabled):
        """
        enables or dissables gravity for this body

        enabled: True, False
        """
        if enabled in [True, False]:
            _pal.lib.body_generic_set_gravity_enabled(self.obj, c.c_bool(enabled))
            self._gravity_enabled = enabled

    @property
    def collision_response(self):
        return self._collision_response_enabled

    @collision_response.setter
    def collision_response(self,enabled):
        """
        enables or dissables collision_response for this body

        enabled: True, False
        """
        if enabled in [True, False]:
            _pal.lib.body_generic_set_collision_response_enabled(self.obj, c.c_bool(enabled))
            self._collision_response_enabled = enabled

    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, mass):
        _pal.lib.body_generic_set_mass(self.obj, c.c_float(mass))
        self._mass = mass

    @property
    def inertia(self):
        inertia = [c.c_float() for x in range(3)]
        _pal.lib.body_generic_get_inertia(self.obj,c.byref(inertia[0]),c.byref(inertia[1]),c.byref(inertia[2]))
        return [p.value for p in inertia]

    @inertia.setter
    def inertia(self, inertia):
        """
        Sets the inertia of the body

        inertia: sequence of 3 floats
        """
        _pal.lib.body_generic_set_inertia(self.obj,c.c_float(inertia[0]),c.c_float(inertia[1]),c.c_float(inertia[2]))

    @property
    def linear_damping(self):
        _pal.lib.body_generic_get_linear_damping.restype = c.c_float
        return _pal.lib.body_generic_get_linear_damping(self.obj)

    @linear_damping.setter
    def linear_damping(self, damping):
        """
        Sets the linear damping of the body

        damping: float
        """
        _pal.lib.body_generic_set_linear_damping(self.obj, c.c_float(damping))

    @property
    def angular_damping(self):
        _pal.lib.body_generic_get_angular_damping.restype = c.c_float
        return _pal.lib.body_generic_get_angular_damping(self.obj)

    @angular_damping.setter
    def angular_damping(self, damping):
        """
        Sets the angular damping of the body

        damping: float
        """
        _pal.lib.body_generic_set_angular_damping(self.obj, c.c_float(damping))

    def connect_geometry(self, geometry):
        """
        Connects a geometry to the body

        geometry: a pre initialised geometry
        """
        if (isinstance(geometry, libgeometry.Box)):
            _pal.lib.body_generic_connect_box_geometry(self.obj, geometry.obj)
        elif (isinstance(geometry, libgeometry.Capsule)):
            _pal.lib.body_generic_connect_capsule_geometry(self.obj, geometry.obj)
        elif (isinstance(geometry, libgeometry.Convex)):
            _pal.lib.body_generic_connect_convex_geometry(self.obj, geometry.obj)
        elif (isinstance(geometry, libgeometry.Concave)):
            _pal.lib.body_generic_connect_concave_geometry(self.obj, geometry.obj)
        elif (isinstance(geometry, libgeometry.Sphere)):
            _pal.lib.body_generic_connect_sphere_geometry(self.obj, geometry.obj)
        self._geometries.append(geometry)

    def remove_geometry(self, geometry):
        """
        removes a geometry from the body

        geometry: a geometry that has been added
        """
        if geometry in self._geometries:
            _pal.lib.body_generic_remove_geometry(self.obj, geometry.obj)
            self._geometries.remove(geometry)

    def get_geometries(self):
        """
        returns a copy of the geometry list

        Note: as it is a copy this cannot be used to modify the bodies
              geometries, please use connect_geometry() or remove_geometry()
        """
        return list(self._geometries)

    
