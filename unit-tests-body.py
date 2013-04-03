import pypalgame as pal

import unittest
import weakref
class TestSequenceFunctions(unittest.TestCase):
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

    def set_active(self,active):
        box = pal.body.Box((0,0,0,1,1,1,1),mass=1)
        box.set_active(False)
        self.assertTrue(not box.is_active())
        


unittest.main()

