import pypalgame as pal

import unittest
import weakref
class TestBoxFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()

    def tearDown(self):
        pal.cleanup()

    def test_box_create(self):
        pal.body.Box((0,0,0,1,1,1),mass=1)
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_box_delete(self):
        box = pal.body.Box((0,0,0,1,1,1),mass=1)
        box.delete()
        self.assertEqual(len(pal._pal.all_objects),0)

    def test_box_weakref(self):
        box = pal.body.Box((0,0,0,1,1,1),mass=1)
        self.assertTrue(isinstance(box,weakref.ProxyType))

    def test_box_get_position(self):
        box = pal.body.Box((0,0,0,1,1,1),mass=1)
        self.assertEqual(box.get_position(), [0,0,0])

    def test_box_get_distance_to(self):
        box = pal.body.Box((0,0,0,1,1,1),mass=1)
        box1 = pal.body.Box((10,0,0,1,1,1),mass=1)
        self.assertEqual(box.get_distance_to(box1), 10)

    def test_box_get_location(self):
        box = pal.body.Box((0,0,0,1,1,1),mass=1)
        self.assertEqual(box.get_location(), [0,0,0,0.0,0.0,0.0])

    def test_box_get_group(self):
        box = pal.body.Box((0,0,0,1,1,1),mass=1)
        self.assertEqual(box.get_group(), 0)

    def test_box_set_group(self):
        box = pal.body.Box((0,0,0,1,1,1),mass=1)
        box.set_group(10)
        self.assertEqual(box.get_group(), 10)

    # NOT SUPPORTED WITH BULLET!
    #def test_box_get_skin_width(self):
    #    box = pal.body.Box((0,0,0,1,1,1),mass=1)
    #    self.assertEqual(box.get_skin_width(), 10)

    #def test_box_set_skin_width(self):
    #    box = pal.body.Box((0,0,0,1,1,1),mass=1)
    #    box.set_skin_width(10)
    #    self.assertEqual(box.get_skin_width(), 10)

    def test_box_set_position(self):
        box = pal.body.Box((0,0,0,1,1,1),mass=1)
        box.set_position((10,10,10))
        self.assertEqual(box.get_position(), [10,10,10])

    def test_box_set_orientation(self):
        box = pal.body.Box((0,0,0,1,1,1),mass=1)
        box.set_orientation((10,10,10))
        self.assertEqual(box.get_location(), [0,0,0,0.5752220749855042, 5.707963466644287, 0.5752220749855042])#TODO

    def test_box_get_size(self):
        box = pal.body.Box((0,0,0,1,1,1),mass=1)
        self.assertEqual(box.get_size(),[1.,1.,1.])

    def test_box_set_position(self):
        box = pal.body.Box((0,0,0,1,1,1),mass=1)
        box.set_position((10,10,10))
        self.assertEqual(box.get_position(),[10,10,10])

    #def apply_impulse(self,impulse):
    #    """Applies an impulse to the object for a single step at an optional offset in world coordinates."""
    #    pal.lib.box_apply_impulse(self.obj,c.c_float(impulse[0]),c.c_float(impulse[1]),c.c_float(impulse[2]))

    def test_box_get_size(self):
        box = pal.body.Box((0,0,0,1,1,1),mass=1)
        self.assertEqual(box.get_size(), [1,1,1])

    def test_box_is_active(self):
        box = pal.body.Box((0,0,0,1,1,1),mass=1)
        self.assertTrue(box.is_active())

    def test_box_set_active(self):
        box = pal.body.Box((0,0,0,1,1,1),mass=1)
        box.set_active(False)
        self.assertTrue(not box.is_active())

    #####These functions are hard to test their output;
    #####So I simply test that the call to the function works
    def test_box_get_velocity(self):
        box = pal.body.Box((0,0,0,1,1,1),mass=1)
        box.get_velocity()

    def test_box_get_angular_velocity(self):
        box = pal.body.Box((0,0,0,1,1,1),mass=1)
        box.get_angular_velocity()

    def test_box_apply_impulse(self):
        box = pal.body.Box((0,0,0,1,1,1),mass=1)
        box.apply_impulse((1,1,1))

    def test_box_apply_impulse_pos(self):
        box = pal.body.Box((0,0,0,1,1,1),mass=1)
        box.apply_impulse((1,1,1),pos=(1,1,1))

    def test_box_apply_angular_impulse_pos(self):
        box = pal.body.Box((0,0,0,1,1,1),mass=1)
        box.apply_angular_impulse((1,1,1))

    def test_box_apply_force(self):
        box = pal.body.Box((0,0,0,1,1,1),mass=1)
        box.apply_force((1,1,1))

    def test_box_apply_force_pos(self):
        box = pal.body.Box((0,0,0,1,1,1),mass=1)
        box.apply_force((1,1,1),pos=(1,1,1))

    def test_box_apply_torque(self):
        box = pal.body.Box((0,0,0,1,1,1),mass=1)
        box.apply_torque((1,1,1))


class TestSphereFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()

    def tearDown(self):
        pal.cleanup()

    def test_sphere_create(self):
        pal.body.Sphere((0,0,0,1),mass=1)
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_sphere_delete(self):
        sphere = pal.body.Sphere((0,0,0,1,1),mass=1)
        sphere.delete()
        self.assertEqual(len(pal._pal.all_objects),0)

    def test_sphere_weakref(self):
        sphere = pal.body.Sphere((0,0,0,1,1),mass=1)
        self.assertTrue(isinstance(sphere,weakref.ProxyType))

    def test_sphere_get_position(self):
        sphere = pal.body.Sphere((0,0,0,1,1),mass=1)
        self.assertEqual(sphere.get_position(), [0,0,0])

    def test_sphere_get_location(self):
        sphere = pal.body.Sphere((0,0,0,1,1),mass=1)
        self.assertEqual(sphere.get_location(), [0,0,0,0.0,0.0,0.0])

    def test_sphere_get_group(self):
        sphere = pal.body.Sphere((0,0,0,1,1),mass=1)
        self.assertEqual(sphere.get_group(), 0)

    def test_sphere_set_group(self):
        sphere = pal.body.Sphere((0,0,0,1,1),mass=1)
        sphere.set_group(10)
        self.assertEqual(sphere.get_group(), 10)

    # NOT SUPPORTED WITH BULLET!
    #def test_sphere_get_skin_width(self):
    #    sphere = pal.body.Sphere((0,0,0,1,1),mass=1)
    #    self.assertEqual(sphere.get_skin_width(), 10)

    #def test_sphere_set_skin_width(self):
    #    sphere = pal.body.Sphere((0,0,0,1,1),mass=1)
    #    sphere.set_skin_width(10)
    #    self.assertEqual(sphere.get_skin_width(), 10)

    def test_sphere_set_position(self):
        sphere = pal.body.Sphere((0,0,0,1,1),mass=1)
        sphere.set_position((10,10,10))
        self.assertEqual(sphere.get_position(), [10,10,10])

    def test_sphere_set_orientation(self):
        sphere = pal.body.Sphere((0,0,0,1,1),mass=1)
        sphere.set_orientation((10,10,10))
        self.assertEqual(sphere.get_location(), [0,0,0,0.5752220749855042, 5.707963466644287, 0.5752220749855042])#TODO

    def test_sphere_get_size(self):
        sphere = pal.body.Sphere((0,0,0,1,1),mass=1)
        self.assertEqual(sphere.get_size(),[1.,1.,1.])

    def test_sphere_set_position(self):
        sphere = pal.body.Sphere((0,0,0,1,1),mass=1)
        sphere.set_position((10,10,10))
        self.assertEqual(sphere.get_position(),[10,10,10])

    #def apply_impulse(self,impulse):
    #    """Applies an impulse to the object for a single step at an optional offset in world coordinates."""
    #    pal.lib.sphere_apply_impulse(self.obj,c.c_float(impulse[0]),c.c_float(impulse[1]),c.c_float(impulse[2]))

    def test_sphere_get_size(self):
        sphere = pal.body.Sphere((0,0,0,1,1),mass=1)
        self.assertEqual(sphere.get_size(), 1)

    def test_sphere_is_active(self):
        sphere = pal.body.Sphere((0,0,0,1,1),mass=1)
        self.assertTrue(sphere.is_active())

    def test_sphere_set_active(self):
        sphere = pal.body.Sphere((0,0,0,1,1),mass=1)
        sphere.set_active(False)
        self.assertTrue(not sphere.is_active())

    #####These functions are hard to test their output;
    #####So I simply test that the call to the function works
    def test_sphere_get_velocity(self):
        sphere = pal.body.Sphere((0,0,0,1,1),mass=1)
        sphere.get_velocity()

    def test_sphere_get_angular_velocity(self):
        sphere = pal.body.Sphere((0,0,0,1,1),mass=1)
        sphere.get_angular_velocity()

    def test_sphere_apply_impulse(self):
        sphere = pal.body.Sphere((0,0,0,1,1),mass=1)
        sphere.apply_impulse((1,1,1))

    def test_sphere_apply_impulse_pos(self):
        sphere = pal.body.Sphere((0,0,0,1,1),mass=1)
        sphere.apply_impulse((1,1,1),pos=(1,1,1))

    def test_sphere_apply_angular_impulse_pos(self):
        sphere = pal.body.Sphere((0,0,0,1,1),mass=1)
        sphere.apply_angular_impulse((1,1,1))

    def test_sphere_apply_force(self):
        sphere = pal.body.Sphere((0,0,0,1,1),mass=1)
        sphere.apply_force((1,1,1))

    def test_sphere_apply_force_pos(self):
        sphere = pal.body.Sphere((0,0,0,1,1),mass=1)
        sphere.apply_force((1,1,1),pos=(1,1,1))

    def test_sphere_apply_torque(self):
        sphere = pal.body.Sphere((0,0,0,1,1),mass=1)
        sphere.apply_torque((1,1,1))


class TestCapsuleFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()

    def tearDown(self):
        pal.cleanup()

    def test_capsule_create(self):
        pal.body.Capsule((0,0,0,1,1),mass=1)
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_capsule_delete(self):
        capsule = pal.body.Capsule((0,0,0,1,1),mass=1)
        capsule.delete()
        self.assertEqual(len(pal._pal.all_objects),0)

    def test_capsule_weakref(self):
        capsule = pal.body.Capsule((0,0,0,1,1),mass=1)
        self.assertTrue(isinstance(capsule,weakref.ProxyType))

    def test_capsule_get_position(self):
        capsule = pal.body.Capsule((0,0,0,1,1),mass=1)
        self.assertEqual(capsule.get_position(), [0,0,0])

    def test_capsule_get_location(self):
        capsule = pal.body.Capsule((0,0,0,1,1),mass=1)
        self.assertEqual(capsule.get_location(), [0,0,0,0.0,0.0,0.0])

    def test_capsule_get_group(self):
        capsule = pal.body.Capsule((0,0,0,1,1),mass=1)
        self.assertEqual(capsule.get_group(), 0)

    def test_capsule_set_group(self):
        capsule = pal.body.Capsule((0,0,0,1,1),mass=1)
        capsule.set_group(10)
        self.assertEqual(capsule.get_group(), 10)

    # NOT SUPPORTED WITH BULLET!
    #def test_capsule_get_skin_width(self):
    #    capsule = pal.body.Capsule((0,0,0,1,1),mass=1)
    #    self.assertEqual(capsule.get_skin_width(), 10)

    #def test_capsule_set_skin_width(self):
    #    capsule = pal.body.Capsule((0,0,0,1,1),mass=1)
    #    capsule.set_skin_width(10)
    #    self.assertEqual(capsule.get_skin_width(), 10)

    def test_capsule_set_position(self):
        capsule = pal.body.Capsule((0,0,0,1,1),mass=1)
        capsule.set_position((10,10,10))
        self.assertEqual(capsule.get_position(), [10,10,10])

    def test_capsule_set_orientation(self):
        capsule = pal.body.Capsule((0,0,0,1,1),mass=1)
        capsule.set_orientation((10,10,10))
        self.assertEqual(capsule.get_location(), [0,0,0,0.5752220749855042, 5.707963466644287, 0.5752220749855042])#TODO

    def test_capsule_get_size(self):
        capsule = pal.body.Capsule((0,0,0,1,1),mass=1)
        self.assertEqual(capsule.get_size(),[1.,1.,1.])

    def test_capsule_set_position(self):
        capsule = pal.body.Capsule((0,0,0,1,1),mass=1)
        capsule.set_position((10,10,10))
        self.assertEqual(capsule.get_position(),[10,10,10])

    #def apply_impulse(self,impulse):
    #    """Applies an impulse to the object for a single step at an optional offset in world coordinates."""
    #    pal.lib.capsule_apply_impulse(self.obj,c.c_float(impulse[0]),c.c_float(impulse[1]),c.c_float(impulse[2]))

    def test_capsule_get_size(self):
        capsule = pal.body.Capsule((0,0,0,1,1),mass=1)
        self.assertEqual(capsule.get_size(), [1,1])

    def test_capsule_is_active(self):
        capsule = pal.body.Capsule((0,0,0,1,1),mass=1)
        self.assertTrue(capsule.is_active())

    def test_capsule_set_active(self):
        capsule = pal.body.Capsule((0,0,0,1,1),mass=1)
        capsule.set_active(False)
        self.assertTrue(not capsule.is_active())

    #####These functions are hard to test their output;
    #####So I simply test that the call to the function works
    def test_capsule_get_velocity(self):
        capsule = pal.body.Capsule((0,0,0,1,1),mass=1)
        capsule.get_velocity()

    def test_capsule_get_angular_velocity(self):
        capsule = pal.body.Capsule((0,0,0,1,1),mass=1)
        capsule.get_angular_velocity()

    def test_capsule_apply_impulse(self):
        capsule = pal.body.Capsule((0,0,0,1,1),mass=1)
        capsule.apply_impulse((1,1,1))

    def test_capsule_apply_impulse_pos(self):
        capsule = pal.body.Capsule((0,0,0,1,1),mass=1)
        capsule.apply_impulse((1,1,1),pos=(1,1,1))

    def test_capsule_apply_angular_impulse_pos(self):
        capsule = pal.body.Capsule((0,0,0,1,1),mass=1)
        capsule.apply_angular_impulse((1,1,1))

    def test_capsule_apply_force(self):
        capsule = pal.body.Capsule((0,0,0,1,1),mass=1)
        capsule.apply_force((1,1,1))

    def test_capsule_apply_force_pos(self):
        capsule = pal.body.Capsule((0,0,0,1,1),mass=1)
        capsule.apply_force((1,1,1),pos=(1,1,1))

    def test_capsule_apply_torque(self):
        capsule = pal.body.Capsule((0,0,0,1,1),mass=1)
        capsule.apply_torque((1,1,1))


class TestConvexFunctions(unittest.TestCase):
    def setUp(self):
        self.points = ((1,1,1),
                       (0,1,1),
                       (1,0,1),
                       (1,1,0),
                       (0,0,1),
                       (0,1,0),
                       (1,0,0),
                       (0,0,0))
        pal.init()

    def tearDown(self):
        pal.cleanup()

    def test_convex_create(self):
        pal.body.Convex((0,0,0),self.points,mass=1)
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_convex_delete(self):
        convex = pal.body.Convex((0,0,0),self.points,mass=1)
        convex.delete()
        self.assertEqual(len(pal._pal.all_objects),0)


suite = [unittest.TestLoader().loadTestsFromTestCase(TestBoxFunctions),
        unittest.TestLoader().loadTestsFromTestCase(TestSphereFunctions),
        unittest.TestLoader().loadTestsFromTestCase(TestCapsuleFunctions),
        unittest.TestLoader().loadTestsFromTestCase(TestConvexFunctions)]

if __name__ == "__main__":
    suite = unittest.TestSuite(suite)
    unittest.TextTestRunner(verbosity=3).run(suite)
