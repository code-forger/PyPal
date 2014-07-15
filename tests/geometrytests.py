import pypal as pal

import unittest
import weakref
class TestBoxFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()

    def tearDown(self):
        pal.cleanup()

    def test_box_create(self):
        pal.geometry.Box((0,0,0),(1,1,1))
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_box_delete(self):
        box = pal.geometry.Box((0,0,0),(1,1,1))
        box.delete()
        self.assertEqual(len(pal._pal.all_objects),0)

    #def test_box_get_location(self):
    #    box = pal.geometry.Box((0,0,0),(1,1,1))
    #    self.assertEqual(box.get_location(), [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1])

    #def test_box_get_position(self):
    #    box = pal.geometry.Box((0,0,0),(1,1,1))
    #    self.assertEqual(box.get_position(), [0,0,0])

    def test_box_get_mass(self):
        box = pal.geometry.Box((0,0,0),(1,1,1))
        self.assertEqual(box.get_mass(), 1)

    def test_box_set_mass(self):
        box = pal.geometry.Box((0,0,0),(1,1,1))
        box.set_mass(10)
        self.assertEqual(box.get_mass(), 10)

    def test_box_get_margin(self):
        box = pal.geometry.Box((0,0,0),(1,1,1))
        self.assertEqual(box.get_margin(), 0.03999999910593033)

    def test_box_set_margin(self):
        box = pal.geometry.Box((0,0,0),(1,1,1))
        box.set_margin(10)
        self.assertEqual(box.get_margin(), 10)


class TestCapsuleFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()

    def tearDown(self):
        pal.cleanup()

    def test_box_create(self):
        pal.geometry.Capsule((0,0,0),(1,1))
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_box_delete(self):
        capsule = pal.geometry.Capsule((0,0,0),(1,1))
        capsule.delete()
        self.assertEqual(len(pal._pal.all_objects),0)

    #def test_capsule_get_location(self):
    #    capsule = pal.geometry.Capsule((0,0,0),(1,1))
    #    self.assertEqual(capsule.get_location(), [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1])

    #def test_capsule_get_position(self):
    #    capsule = pal.geometry.Capsule((0,0,0),(1,1))
    #    self.assertEqual(capsule.get_position(), [0,0,0])

    def test_capsule_get_mass(self):
        capsule = pal.geometry.Capsule((0,0,0),(1,1))
        self.assertEqual(capsule.get_mass(), 1)

    def test_capsule_set_mass(self):
        capsule = pal.geometry.Capsule((0,0,0),(1,1))
        capsule.set_mass(10)
        self.assertEqual(capsule.get_mass(), 10)

    def test_capsule_get_margin(self):
        capsule = pal.geometry.Capsule((0,0,0),(1,1))
        self.assertEqual(capsule.get_margin(), 0.03999999910593033)

    def test_capsule_set_margin(self):
        capsule = pal.geometry.Capsule((0,0,0),(1,1))
        capsule.set_margin(10)
        self.assertEqual(capsule.get_margin(), 10)

class TestSphereFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()

    def tearDown(self):
        pal.cleanup()

    def test_sphere_create(self):
        pal.geometry.Sphere((0,0,0),(1,))
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_sphere_delete(self):
        sphere = pal.geometry.Sphere((0,0,0),(1,))
        sphere.delete()
        self.assertEqual(len(pal._pal.all_objects),0)

    #def test_sphere_get_location(self):
    #    sphere = pal.geometry.Sphere((0,0,0),(1))
    #    self.assertEqual(sphere.get_location(), [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1])

    #def test_sphere_get_position(self):
    #    sphere = pal.geometry.Sphere((0,0,0),(1))
    #    self.assertEqual(sphere.get_position(), [0,0,0])

    def test_sphere_get_mass(self):
        sphere = pal.geometry.Sphere((0,0,0),(1,))
        self.assertEqual(sphere.get_mass(), 1)

    def test_sphere_set_mass(self):
        sphere = pal.geometry.Sphere((0,0,0),(1,))
        sphere.set_mass(10)
        self.assertEqual(sphere.get_mass(), 10)

    def test_sphere_get_margin(self):
        sphere = pal.geometry.Sphere((0,0,0),(1,))
        self.assertEqual(sphere.get_margin(), 1)

    # FAILS TO SET IN PAL
    #def test_sphere_set_margin(self):
    #    sphere = pal.geometry.Sphere((0,0,0),(1,))
    #    self.assertEqual(sphere.get_margin(), 10)

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
        self.triangles = ((0,1,2),
                          (2,3,4),
                          (4,5,6))
        pal.init()

    def tearDown(self):
        pal.cleanup()

    def test_convex_create_no_triangles(self):
        pal.geometry.Convex((0,0,0),self.points)
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_convex_create_triangles(self):
        pal.geometry.Convex((0,0,0),self.points, triangles = self.triangles)
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_convex_delete(self):
        convex  = pal.geometry.Convex((0,0,0),points = self.points)
        convex.delete()
        self.assertEqual(len(pal._pal.all_objects),0)

    def test_convex_get_mass(self):
        convex = pal.geometry.Convex((0,0,0),self.points)
        self.assertEqual(convex.get_mass(), 1)

    def test_convex_set_mass(self):
        convex = pal.geometry.Convex((0,0,0),self.points)
        convex.set_mass(10)
        self.assertEqual(convex.get_mass(), 10)

    def test_convex_get_margin(self):
        convex = pal.geometry.Convex((0,0,0),self.points)
        self.assertEqual(convex.get_margin(), 0.03999999910593033)

    def test_convex_set_margin(self):
        convex = pal.geometry.Convex((0,0,0),self.points)
        convex.set_margin(10)
        self.assertEqual(convex.get_margin(), 10)

class TestConcaveFunctions(unittest.TestCase):
    def setUp(self):
        self.points = ((1,1,1),
                       (0,1,1),
                       (1,0,1),
                       (1,1,0),
                       (0,0,1),
                       (0,1,0),
                       (1,0,0),
                       (0,0,0))
        self.triangles = ((0,1,2),
                          (2,3,4),
                          (4,5,6))
        pal.init()

    def tearDown(self):
        pal.cleanup()

    def test_concave_create_no_triangles(self):
        pal.geometry.Concave((0,0,0),self.points, self.triangles)
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_concave_create_triangles(self):
        pal.geometry.Concave((0,0,0),self.points, self.triangles)
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_concave_delete(self):
        concave = pal.geometry.Concave((0,0,0),self.points, self.triangles)
        concave.delete()
        self.assertEqual(len(pal._pal.all_objects),0)

    def test_concave_get_mass(self):
        concave = pal.geometry.Concave((0,0,0),self.points, self.triangles)
        self.assertEqual(concave.get_mass(), 1)

    def test_concave_set_mass(self):
        concave = pal.geometry.Concave((0,0,0),self.points, self.triangles)
        concave.set_mass(10)
        self.assertEqual(concave.get_mass(), 10)

    def test_concave_get_margin(self):
        concave = pal.geometry.Concave((0,0,0),self.points, self.triangles)
        self.assertEqual(concave.get_margin(), 0.0)

    def test_concave_set_margin(self):
        concave = pal.geometry.Concave((0,0,0),self.points, self.triangles)
        concave.set_margin(10)
        self.assertEqual(concave.get_margin(), 10)

suite = [unittest.TestLoader().loadTestsFromTestCase(TestBoxFunctions),
        unittest.TestLoader().loadTestsFromTestCase(TestCapsuleFunctions),
        unittest.TestLoader().loadTestsFromTestCase(TestSphereFunctions),
        unittest.TestLoader().loadTestsFromTestCase(TestConvexFunctions),
        unittest.TestLoader().loadTestsFromTestCase(TestConcaveFunctions)]

if __name__ == "__main__":
    suite = unittest.TestSuite(suite)
    unittest.TextTestRunner(verbosity=3).run(suite)
