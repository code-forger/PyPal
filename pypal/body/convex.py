from pypal import private_globals as _pal
import ctypes as c
import weakref
class Convex(_pal.PalObject):
    def __init__(self, pos, points, triangles=None, mass = 1.):
        """
        constructs a convex and adds it to the world
        
        pos: a 3 part tuple with x,y,z.
        size: a 3 part tuple with width, height, depth
        mass: the mass of the object, if mass is specified it will be used.
        """
        print "DEBUG!", points
        CPoints = c.c_float * (len(points) * 3)
        cpoints = CPoints()
        for i in xrange(len(points)):
            for j in xrange(3):
                cpoints[(i*3)+j] = points[i][j]
        print "DEBUG!", len(cpoints)
        if triangles==None:
            print "DEBUG! creating none triangle object"
            self.obj = _pal.lib.body_convex_create_no_triangles(c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]),
                                  c.pointer(cpoints),len(points)*3,c.c_float(mass))
        else:
            CTris = c.c_int * len(triangles*3)
            ctris = CTris()
            for i in xrange(len(triangles)):
                for j in xrange(3):
                    ctris[(i*3)+j] = triangles[i][j]

            self.obj = _pal.lib.body_convex_create_triangles(c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]),
                                  c.pointer(cpoints),len(points)*3, c.pointer(ctris), len(triangles)*3,c.c_float(mass))

        self.points = points
        print "DEBUG! done creating"

    def get_location(self):
        ret = _pal.Mat4x4()
        _pal.lib.body_convex_get_location(self.obj, ret)
        return [x for x in ret]

    def get_position(self):
        ret = _pal.Vec3()
        _pal.lib.body_convex_get_position(self.obj, ret)
        return [x for x in ret]

    def get_group(self):
        return _pal.lib.body_convex_get_group(self.obj)

    def set_group(self, group):
        return _pal.lib.body_convex_set_group(self.obj, c.c_int(group))

    def __str__(self):
        x, y, z = self.get_position()
        return "A ConvexBody at : %.2f, %.2f, %.2f" % (x, y, z)

    def set_position(self, pos, rot=(0, 0, 0)):
        """Sets the position of the object and its orientation."""
        _pal.lib.body_convex_set_position(self.obj, c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]), c.c_float(rot[0]), c.c_float(rot[1]), c.c_float(rot[2]))

    def set_orientation(self, rot):
        """Sets the position of the object and/or its orientation."""
        _pal.lib.body_convex_set_orientation(self.obj, c.c_float(rot[0]), c.c_float(rot[1]), c.c_float(rot[2]))

    def apply_force(self, force, pos=None):
        """Applies a force to the object for a single step at an optional offset in world coordinates."""
        if pos:
            _pal.lib.body_convex_apply_force_at_position(self.obj, c.c_float(force[0]), c.c_float(force[1]), c.c_float(force[2]),
                                                          c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]))
        else:
            _pal.lib.body_convex_apply_force(self.obj, c.c_float(force[0]), c.c_float(force[1]), c.c_float(force[2]))

    def apply_torque(self, force):
        """Applies a torque to the object for a single step."""
        _pal.lib.body_convex_apply_torque(self.obj, c.c_float(force[0]), c.c_float(force[1]), c.c_float(force[2]))

    def apply_impulse(self, impulse,pos=None):
        """Applies an impulse to the object for a single step at an optional offset in world coordinates."""
        if pos:
            _pal.lib.body_convex_apply_impulse_at_position(self.obj, c.c_float(impulse[0]), c.c_float(impulse[1]), c.c_float(impulse[2]),
                                                                 c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]))
        else:
            _pal.lib.body_convex_apply_impulse(self.obj, c.c_float(impulse[0]), c.c_float(impulse[1]), c.c_float(impulse[2]))

    def apply_angular_impulse(self, impulse):
        """Applies an angular impulse to the object for a single step at an optional offset in world coordinates."""
        _pal.lib.body_convex_apply_angular_impulse(self.obj, c.c_float(impulse[0]), c.c_float(impulse[1]), c.c_float(impulse[2]))


    def get_linear_velocity(self):
        """Returns the linear velocity of the body."""
        ret = _pal.Vec3()
        _pal.lib.body_convex_get_linear_velocity(self.obj, ret)
        return [x for x in ret]

    def get_angular_velocity(self):
        """Returns the linear velocity of the body."""
        ret = _pal.Vec3()
        _pal.lib.body_convex_get_angular_velocity(self.obj, ret)
        return [x for x in ret]

    def set_linear_velocity(self, velocity):
        """sets the linear velocity og the object"""
        vec = _pal.Vec3()
        for i in range(3):
            vec[i] = velocity[i]
        _pal.lib.body_convex_set_linear_velocity(self.obj, vec)

    def set_angular_velocity(self, velocity):
        """sets the angular velocity og the object"""
        vec = _pal.Vec3()
        for i in range(3):
            vec[i] = velocity[i]
        _pal.lib.body_convex_set_angular_velocity(self.obj, vec)
        
    def is_active(self):
        """Returns true if the body is not asleep."""
        _pal.lib.body_convex_is_active.restype = c.c_bool
        return _pal.lib.body_convex_is_active(self.obj)

    def set_active(self,active):
        """Sets the body to active or not."""
        _pal.lib.body_convex_set_active(self.obj, c.c_bool(active))



class StaticConvex():
    typechar = 'X'
    def __init__(self,pos,points,matrix,triangles=None):#TESTED

        CPoints = c.c_float * (len(points) * 3)
        cpoints = CPoints()
        for i in xrange(len(points)):
            for j in xrange(3):
                cpoints[(i*3)+j] = points[i][j]

        if triangles==None:
            self.obj = pal.lib.create_static_convex_no_triangles(c.c_float(pos[0]), c.c_float(pos[1]), c.c_float(pos[2]),
                                  c.pointer(cpoints),len(points)*3) 
            pal.lib.body_set_position(self.obj,c.c_char(self.typechar),c.c_float(matrix[12]),c.c_float(matrix[13]),c.c_float(matrix[14]))
        else:
            CTris = c.c_int * len(triangles*3)
            ctris = CTris()
            for i in xrange(len(triangles)):
                for j in xrange(3):
                    ctris[(i*3)+j] = triangles[i][j]
            mat = [c.c_float(x) for x in matrix]
            self.obj = pal.lib.create_static_convex_triangles(mat[0],mat[1],mat[2],mat[3],
                                                                 mat[4],mat[5],mat[6],mat[7],
                                                                 mat[8],mat[9],mat[10],mat[11],
                                                                 mat[12],mat[13],mat[14],mat[15],
                                  c.pointer(cpoints),len(points), c.pointer(ctris), len(triangles)*3) 
    def delete(self):
        pal.lib.static_convex_remove(self.obj,self.typechar)
        del pal.all_objects[str(self.obj)]
