import pypalgame as pal

import unittest
import weakref
class TestBoxFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()

    def tearDown(self):
        pal.cleanup()

    def test_box_create(self):
        pal.body.Box((0,0,0,1,1,1,1),mass=1)
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_box_delete(self):
        box = pal.body.Box((0,0,0,1,1,1,1),mass=1)
        box.delete()
        self.assertEqual(len(pal._pal.all_objects),0)

    def test_box_weakref(self):
        box = pal.body.Box((0,0,0,1,1,1,1),mass=1)
        self.assertTrue(isinstance(box,weakref.ProxyType))

    def test_box_get_size(self):
        box = pal.body.Box((0,0,0,1,1,1,1),mass=1)
        self.assertEqual(box.get_size(),[1.,1.,1.])

    def test_box_set_position(self):
        box = pal.body.Box((0,0,0,1,1,1,1),mass=1)
        box.set_position((10,10,10))
        self.assertEqual(box.get_position(),[10,10,10])

    #def apply_impulse(self,impulse):
    #    """Applies an impulse to the object for a single step at an optional offset in world coordinates."""
    #    pal.lib.box_apply_impulse(self.obj,c.c_float(impulse[0]),c.c_float(impulse[1]),c.c_float(impulse[2]))

    def test_box_is_active(self):
        box = pal.body.Box((0,0,0,1,1,1,1),mass=1)
        self.assertTrue(box.is_active())

    def test_box_set_active(self):
        box = pal.body.Box((0,0,0,1,1,1,1),mass=1)
        box.set_active(False)
        self.assertTrue(not box.is_active())
##########Sphere####################################################################
    def test_sphere_create(self):
        pal.body.Sphere((0,0,0,1),mass=1)
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_sphere_delete(self):
        sphere = pal.body.Sphere((0,0,0,1),mass=1)
        sphere.delete()
        self.assertEqual(len(pal._pal.all_objects),0)

    def test_sphere_weakref(self):
        sphere = pal.body.Sphere((0,0,0,1),mass=1)
        self.assertTrue(isinstance(sphere,weakref.ProxyType))

    def test_sphere_get_size(self):
        sphere = pal.body.Sphere((0,0,0,1),mass=1)
        self.assertEqual(sphere.get_size(),1.)

    def test_sphere_set_position(self):
        sphere = pal.body.Sphere((0,0,0,1),mass=1)
        sphere.set_position((10,10,10))
        self.assertEqual(sphere.get_position(),[10,10,10])

    #def apply_impulse(self,impulse):
    #    """Applies an impulse to the object for a single step at an optional offset in world coordinates."""
    #    pal.lib.box_apply_impulse(self.obj,c.c_float(impulse[0]),c.c_float(impulse[1]),c.c_float(impulse[2]))

    def test_sphere_is_active(self):
        sphere = pal.body.Sphere((0,0,0,1),mass=1)
        self.assertTrue(sphere.is_active())

    def test_sphere_set_active(self):
        sphere = pal.body.Sphere((0,0,0,1),mass=1)
        sphere.set_active(False)
        self.assertTrue(not sphere.is_active())
##########Capsule####################################################################
    def test_capsule_create(self):
        pal.body.Capsule((0,0,0,1,3),mass=1)
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_capsule_delete(self):
        capsule = pal.body.Capsule((0,0,0,1,3),mass=1)
        capsule.delete()
        self.assertEqual(len(pal._pal.all_objects),0)

    def test_capsule_weakref(self):
        capsule = pal.body.Capsule((0,0,0,1,3),mass=1)
        self.assertTrue(isinstance(capsule,weakref.ProxyType))

    def test_capsule_get_size(self):
        capsule = pal.body.Capsule((0,0,0,1,3),mass=1)
        self.assertEqual(capsule.get_size(),(1.,3.))

    def test_capsule_set_position(self):
        capsule = pal.body.Capsule((0,0,0,1,3),mass=1)
        capsule.set_position((10,10,10))
        self.assertEqual(capsule.get_position(),[10,10,10])

    #def apply_impulse(self,impulse):
    #    """Applies an impulse to the object for a single step at an optional offset in world coordinates."""
    #    pal.lib.box_apply_impulse(self.obj,c.c_float(impulse[0]),c.c_float(impulse[1]),c.c_float(impulse[2]))

    def test_capsule_is_active(self):
        capsule = pal.body.Capsule((0,0,0,1,3),mass=1)
        self.assertTrue(capsule.is_active())

    def test_capsule_set_active(self):
        capsule = pal.body.Capsule((0,0,0,1,3),mass=1)
        capsule.set_active(False)
        self.assertTrue(not capsule.is_active())
        



suite = unittest.TestLoader().loadTestsFromTestCase(TestBoxFunctions)
unittest.TextTestRunner(verbosity=3).run(suite)






