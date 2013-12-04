import pypal as pal

import unittest
import weakref
class TestMaterialFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()

    def tearDown(self):
        pal.cleanup()

    def test_material_create(self):
        pal.material.Material("name",0,0,1)
        self.assertEqual(len(pal.material.Material.materials),1)

    def test_material_assign(self):
        material = pal.material.Material("name",0,0,1)
        box = pal.body.Box((0,5,0,1,1,1),mass=1)
        box.set_material(material)

suite = [unittest.TestLoader().loadTestsFromTestCase(TestMaterialFunctions)]

if __name__ == "__main__":
    suite = unittest.TestSuite(suite)
    unittest.TextTestRunner(verbosity=3).run(suite)
