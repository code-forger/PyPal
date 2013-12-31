import pypal as pal

import unittest
import weakref
class TestBoxFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()

    def tearDown(self):
        pal.cleanup()

    def test_box_create(self):
        pal.geometry.Box((0,0,0,1,1,1))
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_box_delete(self):
        box = pal.geometry.Box((0,0,0,1,1,1))
        box.delete()
        self.assertEqual(len(pal._pal.all_objects),0)

class TestCapsuleFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()

    def tearDown(self):
        pal.cleanup()

    def test_capsule_create(self):
        pal.geometry.Capsule((0,0,0,1,1))
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_capsule_delete(self):
        capsule = pal.geometry.Capsule((0,0,0,1,1))
        capsule.delete()
        self.assertEqual(len(pal._pal.all_objects),0)

class TestSphereFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()

    def tearDown(self):
        pal.cleanup()

    def test_sphere_create(self):
        pal.geometry.Sphere((0,0,0,1))
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_sphere_delete(self):
        sphere = pal.geometry.Sphere((0,0,0,1))
        sphere.delete()
        self.assertEqual(len(pal._pal.all_objects),0)

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
        pal.geometry.Convex((0,0,0),points = self.points)
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_convex_delete(self):
        convex  = pal.geometry.Convex((0,0,0),points = self.points)
        convex.delete()
        self.assertEqual(len(pal._pal.all_objects),0)

suite = [unittest.TestLoader().loadTestsFromTestCase(TestBoxFunctions),
        unittest.TestLoader().loadTestsFromTestCase(TestSphereFunctions),
        unittest.TestLoader().loadTestsFromTestCase(TestCapsuleFunctions),
        unittest.TestLoader().loadTestsFromTestCase(TestConvexFunctions)]

if __name__ == "__main__":
    suite = unittest.TestSuite(suite)
    unittest.TextTestRunner(verbosity=3).run(suite)
