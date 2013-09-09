from pypalgame import private_globals as pal
import ctypes as c
import weakref
from bodybase import BodyBase
class GenericBody(BodyBase):
    typechar = 'g'
    def __init__(self, pos, rotation=[0,0,0]):
        """
        constructs a box and adds it to the world
        
        rect: a 3 part tuple with x,y,z.
        mass: the mass of the object, if mass is specified it will be used.
        density: if no mass is specified and a density is, the mass will be 
        calculated from the density and the volumne.
        """
        self.obj = pal.lib.create_generic(c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]),
                                          c.c_float(rotation[0]), c.c_float(rotation[1]), c.c_float(rotation[2]))
        self._geometries = []

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
        pal.lib.generic_set_dynamics_type(self.obj, c.c_char(char))
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
            pal.lib.generic_set_gravity_enabled(self.obj, c.c_bool(enabled))
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
            pal.lib.generic_set_collision_response_enabled(self.obj, c.c_bool(enabled))
            self._collision_response_enabled = enabled

    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, mass):
        pal.lib.generic_set_mass(self.obj, c.c_float(mass))
        self._mass = mass

    @property
    def inertia(self):
        inertia = [c.c_float() for x in range(3)]
        pal.lib.generic_get_inertia(self.obj,c.byref(inertia[0]),c.byref(inertia[1]),c.byref(inertia[2]))
        return [p.value for p in inertia]

    @inertia.setter
    def inertia(self, inertia):
        """
        Sets the inertia of the body

        inertia: sequence of 3 floats
        """
        pal.lib.generic_set_inertia(self.obj,c.c_float(inertia[0]),c.c_float(inertia[1]),c.c_float(inertia[2]))

    @property
    def linear_damping(self):
        pal.lib.generic_get_linear_damping.restype = c.c_float
        return pal.lib.generic_get_linear_damping(self.obj)

    @linear_damping.setter
    def linear_damping(self, damping):
        """
        Sets the linear damping of the body

        damping: float
        """
        pal.lib.generic_set_linear_damping(self.obj, c.c_float(damping))

    @property
    def angular_damping(self):
        pal.lib.generic_get_angular_damping.restype = c.c_float
        return pal.lib.generic_get_angular_damping(self.obj)

    @angular_damping.setter
    def angular_damping(self, damping):
        """
        Sets the angular damping of the body

        damping: float
        """
        pal.lib.generic_set_angular_damping(self.obj, c.c_float(damping))

    def connect_geometry(self, geometry):
        """
        Connects a geometry to the body

        geometry: a pre initialised geometry
        """
        pal.lib.generic_connect_geometry(self.obj, geometry.obj, c.c_char(geometry.typechar))
        self._geometries.append(geometry)

    def remove_geometry(self, geometry):
        """
        removes a geometry from the body

        geometry: a geometry that has been added
        """
        if geometry in self._geometries:
            pal.lib.generic_remove_geometry(self.obj, geometry.obj, c.c_char(geometry.typechar))
            self._geometries.remove(geometry)

    def get_geometries(self):
        """
        returns a copy of the geometry list

        Note: as it is a copy this cannot be used to modify the bodies
              geometries, please use connect_geometry() or remove_geometry()
        """
        return list(self._geometries)

    
