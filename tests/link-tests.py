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

unittest.main()
