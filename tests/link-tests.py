import pypalgame as pal

import unittest
import weakref
class TestRigidFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()
        self.box1 = pal.body.Box((0,0,0,1,1,1),mass=1)
        self.box2 = pal.body.Box((10,10,10,1,1,1),mass=1)

    def tearDown(self):
        pal.cleanup()

    def test_rigid_create(self):
        link = pal.link.Rigid(self.box1, self.box2, True)
        self.assertTrue(str(link.obj) in pal._pal.all_objects)

    def test_rigid_delete(self):
        link = pal.link.Rigid(self.box1, self.box2, True)
        link.delete()
        self.assertEqual(len(pal._pal.all_objects), 2)

    def test_rigid_weakref(self):
        link = pal.link.Rigid(self.box1, self.box2, True)
        self.assertTrue(isinstance(link,weakref.ProxyType))

class TestPrismaticFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()
        self.box1 = pal.body.Box((0,0,0,1,1,1),mass=1)
        self.box2 = pal.body.Box((10,10,10,1,1,1),mass=1)

    def tearDown(self):
        pal.cleanup()

    def test_prismatic_create(self):
        link = pal.link.Prismatic(self.box1, self.box2, self.box1.get_position(),(1,0,0), True)
        self.assertTrue(str(link.obj) in pal._pal.all_objects)

    def test_prismatic_delete(self):
        link = pal.link.Prismatic(self.box1, self.box2, self.box1.get_position(),(1,0,0), True)
        self.box1.delete()
        self.box2.delete()
        link.delete()
        self.assertEqual(len(pal._pal.all_objects), 0)

    def test_prismatic_weakref(self):
        link = pal.link.Prismatic(self.box1, self.box2, self.box1.get_position(),(1,0,0), True)
        self.assertTrue(isinstance(link,weakref.ProxyType))

    def test_prismatic_set_limits(self):
        link = pal.link.Prismatic(self.box1, self.box2, self.box1.get_position(),(1,0,0), True)
        link.set_limits(10,1)

class TestRevoluteFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()
        self.box1 = pal.body.Box((0,0,0,1,1,1),mass=1)
        self.box2 = pal.body.Box((10,10,10,1,1,1),mass=1)

    def tearDown(self):
        pal.cleanup()

    def test_revolute_create(self):
        link = pal.link.Revolute(self.box1, self.box2, self.box1.get_position(),(1,0,0), True)
        self.assertTrue(str(link.obj) in pal._pal.all_objects)

    def test_revolute_delete(self):
        link = pal.link.Revolute(self.box1, self.box2, self.box1.get_position(),(1,0,0), True)
        self.box1.delete()
        self.box2.delete()
        link.delete()
        self.assertEqual(len(pal._pal.all_objects), 0)

    def test_revolute_weakref(self):
        link = pal.link.Revolute(self.box1, self.box2, self.box1.get_position(),(1,0,0), True)
        self.assertTrue(isinstance(link,weakref.ProxyType))

    def test_revolute_set_limits(self):
        link = pal.link.Revolute(self.box1, self.box2, self.box1.get_position(),(1,0,0), True)
        link.set_limits(10,1)

    def test_revolute_get_position(self):
        link = pal.link.Revolute(self.box1, self.box2, self.box1.get_position(),(1,0,0), True)
        self.assertEqual(link.get_position(), [0,0,0])

    def test_revolute_get_angle(self):
        link = pal.link.Revolute(self.box1, self.box2, self.box1.get_position(),(1,0,0), True)
        self.assertEqual(link.get_angle(), 0)

    def test_revolute_get_angular_velocity(self):
        link = pal.link.Revolute(self.box1, self.box2, self.box1.get_position(),(1,0,0), True)
        self.assertEqual(link.get_angular_velocity(), 0)

    def test_revolute_get_axis(self):
        axis = [1,0,0]
        link = pal.link.Revolute(self.box1, self.box2, self.box1.get_position(),axis, True)
        self.assertEqual(link.get_axis(), axis)

    def test_revolute_apply_torque(self):
        link = pal.link.Revolute(self.box1, self.box2, self.box1.get_position(),(1,0,0), True)
        link.apply_torque(1)

    def test_revolute_apply_angular_impulse(self):
        link = pal.link.Revolute(self.box1, self.box2, self.box1.get_position(),(1,0,0), True)
        link.apply_angular_impulse(1)

unittest.main()
