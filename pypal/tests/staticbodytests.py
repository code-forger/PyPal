import pypal as pal

import unittest
import weakref
class TestStaticBoxFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()

    def tearDown(self):
        pal.cleanup()

    def test_box_create(self):
        pal.body.StaticBox((0,0,0,1,1,1))
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_box_delete(self):
        box = pal.body.StaticBox((0,0,0,1,1,1))
        box.delete()
        self.assertEqual(len(pal._pal.all_objects),0)

    def test_box_weakref(self):
        box = pal.body.StaticBox((0,0,0,1,1,1))
        self.assertTrue(isinstance(box,weakref.ProxyType))

    def test_box_get_position(self):
        box = pal.body.StaticBox((0,0,0,1,1,1))
        self.assertEqual(box.get_position(), [0,0,0])

    def test_box_get_distance_to(self):
        box = pal.body.StaticBox((0,0,0,1,1,1))
        box1 = pal.body.Box((10,0,0,1,1,1),mass=1)
        self.assertEqual(box.get_distance_to(box1), 10)

    def test_box_get_location(self):
        box = pal.body.StaticBox((0,0,0,1,1,1))
        self.assertEqual(box.get_location(), [0,0,0,0.0,0.0,0.0])

    def test_box_get_group(self):
        box = pal.body.StaticBox((0,0,0,1,1,1))
        self.assertEqual(box.get_group(), 0)

    def test_box_set_group(self):
        box = pal.body.StaticBox((0,0,0,1,1,1))
        box.set_group(10)
        self.assertEqual(box.get_group(), 10)

    # NOT SUPPORTED WITH BULLET!
    #def test_box_get_skin_width(self):
    #    box = pal.body.StaticBox((0,0,0,1,1,1))
    #    self.assertEqual(box.get_skin_width(), 10)

    #def test_box_set_skin_width(self):
    #    box = pal.body.StaticBox((0,0,0,1,1,1))
    #    box.set_skin_width(10)
    #    self.assertEqual(box.get_skin_width(), 10)

    def test_box_set_position(self):
        box = pal.body.StaticBox((0,0,0,1,1,1))
        box.set_position((10,10,10))
        self.assertEqual(box.get_position(), [10,10,10])

    def test_box_set_orientation(self):
        box = pal.body.StaticBox((0,0,0,1,1,1))
        box.set_orientation((10,10,10))
        self.assertEqual(box.get_location(), [0,0,0,0.5752220749855042, 5.707963466644287, 0.5752220749855042])#TODO

    def test_box_get_size(self):
        box = pal.body.StaticBox((0,0,0,1,1,1))
        self.assertEqual(box.get_size(),[1.,1.,1.])

    def test_box_set_position(self):
        box = pal.body.StaticBox((0,0,0,1,1,1))
        box.set_position((10,10,10))
        self.assertEqual(box.get_position(),[10,10,10])

    #def apply_impulse(self,impulse):
    #    """Applies an impulse to the object for a single step at an optional offset in world coordinates."""
    #    pal.lib.box_apply_impulse(self.obj,c.c_float(impulse[0]),c.c_float(impulse[1]),c.c_float(impulse[2]))

    def test_box_get_size(self):
        box = pal.body.StaticBox((0,0,0,1,1,1))
        self.assertEqual(box.get_size(), (1,1,1))


class TestStaticSphereFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()

    def tearDown(self):
        pal.cleanup()

    def test_sphere_create(self):
        pal.body.StaticSphere((0,0,0,1))
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_sphere_delete(self):
        sphere = pal.body.StaticSphere((0,0,0,1,1))
        sphere.delete()
        self.assertEqual(len(pal._pal.all_objects),0)

    def test_sphere_weakref(self):
        sphere = pal.body.StaticSphere((0,0,0,1,1))
        self.assertTrue(isinstance(sphere,weakref.ProxyType))

    def test_sphere_get_position(self):
        sphere = pal.body.StaticSphere((0,0,0,1,1))
        self.assertEqual(sphere.get_position(), [0,0,0])

    def test_sphere_get_location(self):
        sphere = pal.body.StaticSphere((0,0,0,1,1))
        self.assertEqual(sphere.get_location(), [0,0,0,0.0,0.0,0.0])

    def test_sphere_get_group(self):
        sphere = pal.body.StaticSphere((0,0,0,1,1))
        self.assertEqual(sphere.get_group(), 0)

    def test_sphere_set_group(self):
        sphere = pal.body.StaticSphere((0,0,0,1,1))
        sphere.set_group(10)
        self.assertEqual(sphere.get_group(), 10)

    # NOT SUPPORTED WITH BULLET!
    #def test_sphere_get_skin_width(self):
    #    sphere = pal.body.StaticSphere((0,0,0,1,1))
    #    self.assertEqual(sphere.get_skin_width(), 10)

    #def test_sphere_set_skin_width(self):
    #    sphere = pal.body.StaticSphere((0,0,0,1,1))
    #    sphere.set_skin_width(10)
    #    self.assertEqual(sphere.get_skin_width(), 10)

    def test_sphere_set_position(self):
        sphere = pal.body.StaticSphere((0,0,0,1,1))
        sphere.set_position((10,10,10))
        self.assertEqual(sphere.get_position(), [10,10,10])

    def test_sphere_set_orientation(self):
        sphere = pal.body.StaticSphere((0,0,0,1,1))
        sphere.set_orientation((10,10,10))
        self.assertEqual(sphere.get_location(), [0,0,0,0.5752220749855042, 5.707963466644287, 0.5752220749855042])#TODO

    def test_sphere_get_size(self):
        sphere = pal.body.StaticSphere((0,0,0,1,1))
        self.assertEqual(sphere.get_size(),(1.,1.,1.))

    def test_sphere_set_position(self):
        sphere = pal.body.StaticSphere((0,0,0,1,1))
        sphere.set_position((10,10,10))
        self.assertEqual(sphere.get_position(),[10,10,10])

    #def apply_impulse(self,impulse):
    #    """Applies an impulse to the object for a single step at an optional offset in world coordinates."""
    #    pal.lib.sphere_apply_impulse(self.obj,c.c_float(impulse[0]),c.c_float(impulse[1]),c.c_float(impulse[2]))

    def test_sphere_get_size(self):
        sphere = pal.body.StaticSphere((0,0,0,1,1))
        self.assertEqual(sphere.get_size(), 1)


class TestStaticCapsuleFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()

    def tearDown(self):
        pal.cleanup()

    def test_capsule_create(self):
        pal.body.StaticCapsule((0,0,0,1,1))
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_capsule_delete(self):
        capsule = pal.body.StaticCapsule((0,0,0,1,1))
        capsule.delete()
        self.assertEqual(len(pal._pal.all_objects),0)

    def test_capsule_weakref(self):
        capsule = pal.body.StaticCapsule((0,0,0,1,1))
        self.assertTrue(isinstance(capsule,weakref.ProxyType))

    def test_capsule_get_position(self):
        capsule = pal.body.StaticCapsule((0,0,0,1,1))
        self.assertEqual(capsule.get_position(), [0,0,0])

    def test_capsule_get_location(self):
        capsule = pal.body.StaticCapsule((0,0,0,1,1))
        self.assertEqual(capsule.get_location(), [0,0,0,0.0,0.0,0.0])

    def test_capsule_get_group(self):
        capsule = pal.body.StaticCapsule((0,0,0,1,1))
        self.assertEqual(capsule.get_group(), 0)

    def test_capsule_set_group(self):
        capsule = pal.body.StaticCapsule((0,0,0,1,1))
        capsule.set_group(10)
        self.assertEqual(capsule.get_group(), 10)

    # NOT SUPPORTED WITH BULLET!
    #def test_capsule_get_skin_width(self):
    #    capsule = pal.body.StaticCapsule((0,0,0,1,1))
    #    self.assertEqual(capsule.get_skin_width(), 10)

    #def test_capsule_set_skin_width(self):
    #    capsule = pal.body.StaticCapsule((0,0,0,1,1))
    #    capsule.set_skin_width(10)
    #    self.assertEqual(capsule.get_skin_width(), 10)

    def test_capsule_set_position(self):
        capsule = pal.body.StaticCapsule((0,0,0,1,1))
        capsule.set_position((10,10,10))
        self.assertEqual(capsule.get_position(), [10,10,10])

    def test_capsule_set_orientation(self):
        capsule = pal.body.StaticCapsule((0,0,0,1,1))
        capsule.set_orientation((10,10,10))
        self.assertEqual(capsule.get_location(), [0,0,0,0.5752220749855042, 5.707963466644287, 0.5752220749855042])#TODO

    def test_capsule_get_size(self):
        capsule = pal.body.StaticCapsule((0,0,0,1,1))
        self.assertEqual(capsule.get_size(),(1.,1.,1.))

    def test_capsule_set_position(self):
        capsule = pal.body.StaticCapsule((0,0,0,1,1))
        capsule.set_position((10,10,10))
        self.assertEqual(capsule.get_position(),[10,10,10])

    #def apply_impulse(self,impulse):
    #    """Applies an impulse to the object for a single step at an optional offset in world coordinates."""
    #    pal.lib.capsule_apply_impulse(self.obj,c.c_float(impulse[0]),c.c_float(impulse[1]),c.c_float(impulse[2]))

    def test_capsule_get_size(self):
        capsule = pal.body.StaticCapsule((0,0,0,1,1))
        self.assertEqual(capsule.get_size(), (1,1))

class TestStaticConvexFunctions(unittest.TestCase):
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
        pal.body.StaticConvex((0,0,0),self.points)
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_convex_delete(self):
        convex = pal.body.StaticConvex((0,0,0),self.points)
        convex.delete()
        self.assertEqual(len(pal._pal.all_objects),0)

suite = [unittest.TestLoader().loadTestsFromTestCase(TestStaticBoxFunctions),
        unittest.TestLoader().loadTestsFromTestCase(TestStaticSphereFunctions),
        unittest.TestLoader().loadTestsFromTestCase(TestStaticCapsuleFunctions),
        unittest.TestLoader().loadTestsFromTestCase(TestStaticConvexFunctions)]

if __name__ == "__main__":
    suite = unittest.TestSuite(suite)
    unittest.TextTestRunner(verbosity=3).run(suite)
