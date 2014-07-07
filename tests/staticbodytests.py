import pypal as pal

import unittest
import weakref

#  ______     __                 __      __                  _______                             ________                      __               
# /      \   |  \               |  \    |  \                |       \                           |        \                    |  \              
#|  $$$$$$\ _| $$_     ______  _| $$_    \$$  _______       | $$$$$$$\  ______   __    __        \$$$$$$$$______    _______  _| $$_     _______ 
#| $$___\$$|   $$ \   |      \|   $$ \  |  \ /       \      | $$__/ $$ /      \ |  \  /  \         | $$  /      \  /       \|   $$ \   /       \
# \$$    \  \$$$$$$    \$$$$$$\\$$$$$$  | $$|  $$$$$$$      | $$    $$|  $$$$$$\ \$$\/  $$         | $$ |  $$$$$$\|  $$$$$$$ \$$$$$$  |  $$$$$$$
# _\$$$$$$\  | $$ __  /      $$ | $$ __ | $$| $$            | $$$$$$$\| $$  | $$  >$$  $$          | $$ | $$    $$ \$$    \   | $$ __  \$$    \ 
#|  \__| $$  | $$|  \|  $$$$$$$ | $$|  \| $$| $$_____       | $$__/ $$| $$__/ $$ /  $$$$\          | $$ | $$$$$$$$ _\$$$$$$\  | $$|  \ _\$$$$$$\
# \$$    $$   \$$  $$ \$$    $$  \$$  $$| $$ \$$     \      | $$    $$ \$$    $$|  $$ \$$\         | $$  \$$     \|       $$   \$$  $$|       $$
#  \$$$$$$     \$$$$   \$$$$$$$   \$$$$  \$$  \$$$$$$$       \$$$$$$$   \$$$$$$  \$$   \$$          \$$   \$$$$$$$ \$$$$$$$     \$$$$  \$$$$$$$ 

class TestStaticBoxFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()

    def tearDown(self):
        pal.cleanup()

    def test_box_create(self):
        pal.body.StaticBox((0,0,0),(1,1,1))
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_box_delete(self):
        box = pal.body.StaticBox((0,0,0),(1,1,1))
        box.delete()
        self.assertEqual(len(pal._pal.all_objects),0)

    def test_box_weakref(self):
        box = pal.body.StaticBox((0,0,0),(1,1,1))
        self.assertTrue(isinstance(box,weakref.ProxyType))

    def test_box_get_location(self):
        box = pal.body.StaticBox((0,0,0),(1,1,1))
        self.assertEqual(box.get_location(), [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1])

    def test_box_get_position(self):
        box = pal.body.StaticBox((0,0,0),(1,1,1))
        self.assertEqual(box.get_position(), [0,0,0])

    def test_box_get_group(self):
        box = pal.body.StaticBox((0,0,0),(1,1,1))
        self.assertEqual(box.get_group(), 0)

    def test_box_set_group(self):
        box = pal.body.StaticBox((0,0,0),(1,1,1))
        box.set_group(10)
        self.assertEqual(box.get_group(), 10)

    def test_box_to_string(self):
        box = pal.body.StaticBox((0,0,0),(1,1,1))
        self.assertEqual(box.__str__(), "A Static Box at : 0.00, 0.00, 0.00")

    def test_box_get_size(self):
        box = pal.body.StaticBox((0,0,0),(1,1,1))
        self.assertEqual(box.get_size(),(1.,1.,1.))

class TestStaticSphereFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()

    def tearDown(self):
        pal.cleanup()

    def test_sphere_create(self):
        pal.body.StaticSphere((0,0,0),(1,))
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_sphere_delete(self):
        sphere = pal.body.StaticSphere((0,0,0),(1,))
        sphere.delete()
        self.assertEqual(len(pal._pal.all_objects),0)

    def test_sphere_weakref(self):
        sphere = pal.body.StaticSphere((0,0,0),(1,))
        self.assertTrue(isinstance(sphere,weakref.ProxyType))

    def test_sphere_get_location(self):
        sphere = pal.body.StaticSphere((0,0,0),(1,))
        self.assertEqual(sphere.get_location(), [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1])

    def test_sphere_get_position(self):
        sphere = pal.body.StaticSphere((0,0,0),(1,))
        self.assertEqual(sphere.get_position(), [0,0,0])

    def test_sphere_get_group(self):
        sphere = pal.body.StaticSphere((0,0,0),(1,))
        self.assertEqual(sphere.get_group(), 0)

    def test_sphere_set_group(self):
        sphere = pal.body.StaticSphere((0,0,0),(1,))
        sphere.set_group(10)
        self.assertEqual(sphere.get_group(), 10)

    def test_sphere_to_string(self):
        sphere = pal.body.StaticSphere((0,0,0),(1,))
        self.assertEqual(sphere.__str__(), "A Static Sphere at : 0.00, 0.00, 0.00")

    def test_sphere_get_size(self):
        sphere = pal.body.StaticSphere((0,0,0),(1.,))
        self.assertEqual(sphere.get_size(),(1.,))


class TestStaticCapsuleFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()

    def tearDown(self):
        pal.cleanup()

    def test_capsule_create(self):
        pal.body.StaticCapsule((0,0,0),(1,1))
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_capsule_delete(self):
        capsule = pal.body.StaticCapsule((0,0,0),(1,1))
        capsule.delete()
        self.assertEqual(len(pal._pal.all_objects),0)

    def test_capsule_weakref(self):
        capsule = pal.body.StaticCapsule((0,0,0),(1,1))
        self.assertTrue(isinstance(capsule,weakref.ProxyType))

    def test_capsule_get_location(self):
        capsule = pal.body.StaticCapsule((0,0,0),(1,1))
        self.assertEqual(capsule.get_location(), [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1])

    def test_capsule_get_position(self):
        capsule = pal.body.StaticCapsule((0,0,0),(1,1))
        self.assertEqual(capsule.get_position(), [0,0,0])

    def test_capsule_get_group(self):
        capsule = pal.body.StaticCapsule((0,0,0),(1,1))
        self.assertEqual(capsule.get_group(), 0)

    def test_capsule_set_group(self):
        capsule = pal.body.StaticCapsule((0,0,0),(1,1))
        capsule.set_group(10)
        self.assertEqual(capsule.get_group(), 10)

    def test_capsule_to_string(self):
        capsule = pal.body.StaticCapsule((0,0,0),(1,1))
        self.assertEqual(capsule.__str__(), "A Static Capsule at : 0.00, 0.00, 0.00")

    def test_capsule_get_size(self):
        capsule = pal.body.StaticCapsule((0,0,0),(1.,1.))
        self.assertEqual(capsule.get_size(),(1., 1.))

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
        pal.body.StaticConvex((0,0,0), (0,0,0),self.points)
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_convex_delete(self):
        convex = pal.body.StaticConvex((0,0,0), (0,0,0),self.points)
        convex.delete()
        self.assertEqual(len(pal._pal.all_objects),0)

    def test_convex_get_location(self):
        convex = pal.body.StaticConvex((0,0,0), (0,0,0),self.points)
        self.assertEqual(convex.get_location(), [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1])

    def test_convex_get_position(self):
        convex = pal.body.StaticConvex((0,0,0), (0,0,0),self.points)
        self.assertEqual(convex.get_position(), [0,0,0])

    def test_convex_get_group(self):
        convex = pal.body.StaticConvex((0,0,0), (0,0,0),self.points)
        self.assertEqual(convex.get_group(), 0)

    def test_convex_set_group(self):
        convex = pal.body.StaticConvex((0,0,0), (0,0,0),self.points)
        convex.set_group(10)
        self.assertEqual(convex.get_group(), 10)

    def test_convex_to_string(self):
        convex = pal.body.StaticConvex((0,0,0), (0,0,0),self.points)
        self.assertEqual(convex.__str__(), "A Static Convex at : 0.00, 0.00, 0.00")

class TestStaticCompoundFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()

    def tearDown(self):
        pal.cleanup()

    def test_compound_create(self):
        pal.body.StaticCompound((0,0,0))
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_compound_delete(self):
        compound = pal.body.StaticCompound((0,0,0))
        compound.delete()
        self.assertEqual(len(pal._pal.all_objects),0)

    def test_compound_weakref(self):
        compound = pal.body.StaticCompound((0,0,0))
        self.assertTrue(isinstance(compound,weakref.ProxyType))

    def test_compound_get_location(self):
        compound = pal.body.StaticCompound((0,0,0))
        self.assertEqual(compound.get_location(), [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1])

    def test_compound_get_position(self):
        compound = pal.body.StaticCompound((0,0,0))
        self.assertEqual(compound.get_position(), [0,0,0])

    def test_compound_get_group(self):
        compound = pal.body.StaticCompound((0,0,0))
        self.assertEqual(compound.get_group(), 0)

    def test_compound_set_group(self):
        compound = pal.body.StaticCompound((0,0,0))
        compound.set_group(10)
        self.assertEqual(compound.get_group(), 10)

    def test_compound_to_string(self):
        compound = pal.body.StaticCompound((0,0,0))
        self.assertEqual(compound.__str__(), "A Static Compound Body at : 0.00, 0.00, 0.00")


class TestTerrainPlaneFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()

    def tearDown(self):
        pal.cleanup()

    def test_terrain_plane_create(self):
        pal.body.TerrainPlane((0,0,0),1)
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_terrain_plane_delete(self):
        terrain_plane = pal.body.TerrainPlane((0,0,0),1)
        terrain_plane.delete()
        self.assertEqual(len(pal._pal.all_objects),0)

    def test_terrain_plane_weakref(self):
        terrain_plane = pal.body.TerrainPlane((0,0,0),1)
        self.assertTrue(isinstance(terrain_plane,weakref.ProxyType))

    def test_terrain_plane_get_location(self):
        terrain_plane = pal.body.TerrainPlane((0,0,0),1)
        self.assertEqual(terrain_plane.get_location(), [1,0,0,0,0,1,0,0,0,0,1,0,0,-1,0,1])

    def test_terrain_plane_get_position(self):
        terrain_plane = pal.body.TerrainPlane((0,0,0),1)
        self.assertEqual(terrain_plane.get_position(), [0,-1,0])

    def test_terrain_plane_get_group(self):
        terrain_plane = pal.body.TerrainPlane((0,0,0),1)
        self.assertEqual(terrain_plane.get_group(), 0)

    def test_terrain_plane_set_group(self):
        terrain_plane = pal.body.TerrainPlane((0,0,0),1)
        terrain_plane.set_group(10)
        self.assertEqual(terrain_plane.get_group(), 10)

    def test_terrain_plane_to_string(self):
        terrain_plane = pal.body.TerrainPlane((0,0,0),1)
        self.assertEqual(terrain_plane.__str__(), "A Terrain Plane at : 0.00, -1.00, 0.00")

    def test_terrain_plane_get_size(self):
        terrain_plane = pal.body.TerrainPlane((0,0,0),1)
        self.assertEqual(terrain_plane.get_size(),(1))

class TestOrientatedTerrainPlaneFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()

    def tearDown(self):
        pal.cleanup()

    def test_orientated_terrain_plane_create(self):
        pal.body.OrientatedTerrainPlane((0,0,0),(0,1,0),1)
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_orientated_terrain_plane_delete(self):
        orientated_terrain_plane = pal.body.OrientatedTerrainPlane((0,0,0),(0,1,0),1)
        orientated_terrain_plane.delete()
        self.assertEqual(len(pal._pal.all_objects),0)

    def test_orientated_terrain_plane_weakref(self):
        orientated_terrain_plane = pal.body.OrientatedTerrainPlane((0,0,0),(0,1,0),1)
        self.assertTrue(isinstance(orientated_terrain_plane,weakref.ProxyType))

    def test_orientated_terrain_plane_get_location(self):
        orientated_terrain_plane = pal.body.OrientatedTerrainPlane((0,0,0),(0,1,0),1)
        self.assertEqual(orientated_terrain_plane.get_location(), [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1])

    def test_orientated_terrain_plane_get_position(self):
        orientated_terrain_plane = pal.body.OrientatedTerrainPlane((0,0,0),(0,1,0),1)
        self.assertEqual(orientated_terrain_plane.get_position(), [0,0,0])

    def test_orientated_terrain_plane_get_group(self):
        orientated_terrain_plane = pal.body.OrientatedTerrainPlane((0,0,0),(0,1,0),1)
        self.assertEqual(orientated_terrain_plane.get_group(), 0)

    def test_orientated_terrain_plane_set_group(self):
        orientated_terrain_plane = pal.body.OrientatedTerrainPlane((0,0,0),(0,1,0),1)
        orientated_terrain_plane.set_group(10)
        self.assertEqual(orientated_terrain_plane.get_group(), 10)

    def test_orientated_terrain_plane_to_string(self):
        orientated_terrain_plane = pal.body.OrientatedTerrainPlane((0,0,0),(0,1,0),1)
        self.assertEqual(orientated_terrain_plane.__str__(), "An Orientated Terrain Plane at : 0.00, 0.00, 0.00")

    def test_orientated_terrain_plane_get_size(self):
        orientated_terrain_plane = pal.body.OrientatedTerrainPlane((0,0,0),(0,1,0),1)
        self.assertEqual(orientated_terrain_plane.get_size(),(1))

suite = [unittest.TestLoader().loadTestsFromTestCase(TestStaticBoxFunctions),
         unittest.TestLoader().loadTestsFromTestCase(TestStaticConvexFunctions),
         unittest.TestLoader().loadTestsFromTestCase(TestStaticSphereFunctions),
         unittest.TestLoader().loadTestsFromTestCase(TestStaticCapsuleFunctions),
         unittest.TestLoader().loadTestsFromTestCase(TestStaticCompoundFunctions),
         unittest.TestLoader().loadTestsFromTestCase(TestTerrainPlaneFunctions),
         unittest.TestLoader().loadTestsFromTestCase(TestOrientatedTerrainPlaneFunctions)]

if __name__ == "__main__":
    suite = unittest.TestSuite(suite)
    unittest.TextTestRunner(verbosity=3).run(suite)
