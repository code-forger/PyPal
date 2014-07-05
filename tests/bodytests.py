import pypal as pal

import unittest
import weakref

# _______    ______   __    __        ________  ________   ______  ________   ______  
#|       \  /      \ |  \  |  \      |        \|        \ /      \|        \ /      \ 
#| $$$$$$$\|  $$$$$$\| $$  | $$       \$$$$$$$$| $$$$$$$$|  $$$$$$\\$$$$$$$$|  $$$$$$\
#| $$__/ $$| $$  | $$ \$$\/  $$         | $$   | $$__    | $$___\$$  | $$   | $$___\$$
#| $$    $$| $$  | $$  >$$  $$          | $$   | $$  \    \$$    \   | $$    \$$    \ 
#| $$$$$$$\| $$  | $$ /  $$$$\          | $$   | $$$$$    _\$$$$$$\  | $$    _\$$$$$$\
#| $$__/ $$| $$__/ $$|  $$ \$$\         | $$   | $$_____ |  \__| $$  | $$   |  \__| $$
#| $$    $$ \$$    $$| $$  | $$         | $$   | $$     \ \$$    $$  | $$    \$$    $$
# \$$$$$$$   \$$$$$$  \$$   \$$          \$$    \$$$$$$$$  \$$$$$$    \$$     \$$$$$$ 

class TestBoxFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()

    def tearDown(self):
        pal.cleanup()

    def test_box_create(self):
        pal.body.Box((0,0,0),(1,1,1),mass=1)
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_box_delete(self):
        box = pal.body.Box((0,0,0),(1,1,1),mass=1)
        box.delete()
        self.assertEqual(len(pal._pal.all_objects),0)

    def test_box_weakref(self):
        box = pal.body.Box((0,0,0),(1,1,1),mass=1)
        self.assertTrue(isinstance(box,weakref.ProxyType))

    def test_box_get_location(self):
        box = pal.body.Box((0,0,0),(1,1,1),mass=1)
        self.assertEqual(box.get_location(), [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1])

    def test_box_get_position(self):
        box = pal.body.Box((0,0,0),(1,1,1),mass=1)
        self.assertEqual(box.get_position(), [0,0,0])

    def test_box_get_group(self):
        box = pal.body.Box((0,0,0),(1,1,1),mass=1)
        self.assertEqual(box.get_group(), 0)

    def test_box_set_group(self):
        box = pal.body.Box((0,0,0),(1,1,1),mass=1)
        box.set_group(10)
        self.assertEqual(box.get_group(), 10)

    def test_box_to_string(self):
        box = pal.body.Box((0,0,0),(1,1,1),mass=1)
        self.assertEqual(box.__str__(), "A Box at : 0.00, 0.00, 0.00")

    def test_box_set_position(self):
        box = pal.body.Box((0,0,0),(1,1,1),mass=1)
        box.set_position((10,10,10))
        self.assertEqual(box.get_position(), [10,10,10])

    def test_box_set_orientation(self):
        box = pal.body.Box((0,0,0),(1,1,1),mass=1)
        box.set_orientation((10,10,10))
        self.assertEqual(box.get_location(), [0.7040410041809082, 0.45647263526916504, 0.5440211296081543, 0.0, -0.7048034071922302, 0.5430330634117126, 0.45647263526916504, 0.0, -0.08705419301986694, -0.7048034071922302, 0.7040410041809082, 0.0, 0.0, 0.0, 0.0, 1.,])#TODO

    def test_box_apply_force(self):
        box = pal.body.Box((0,0,0),(1,1,1),mass=1)
        box.apply_force((1,1,1))

    def test_box_apply_torque(self):
        box = pal.body.Box((0,0,0),(1,1,1),mass=1)
        box.apply_torque((1,1,1))

    def test_box_apply_force_pos(self):
        box = pal.body.Box((0,0,0),(1,1,1),mass=1)
        box.apply_force((1,1,1),pos=(1,1,1))

    def test_box_apply_impulse(self):
        box = pal.body.Box((0,0,0),(1,1,1),mass=1)
        box.apply_impulse((1,1,1))

    def test_box_apply_angular_impulse(self):
        box = pal.body.Box((0,0,0),(1,1,1),mass=1)
        box.apply_angular_impulse((1,1,1))

    def test_box_apply_impulse_pos(self):
        box = pal.body.Box((0,0,0),(1,1,1),mass=1)
        box.apply_impulse((1,1,1),pos=(1,1,1))

    def test_box_get_velocity(self):
        box = pal.body.Box((0,0,0),(1,1,1),mass=1)
        self.assertEqual(box.get_linear_velocity(), [0,0,0])

    def test_box_get_angular_velocity(self):
        box = pal.body.Box((0,0,0),(1,1,1),mass=1)
        self.assertEqual(box.get_angular_velocity(), [0,0,0])

    def test_box_set_velocity(self):
        box = pal.body.Box((0,0,0),(1,1,1),mass=1)
        box.set_linear_velocity((10,10,10))
        self.assertEqual(box.get_linear_velocity(), [10,10,10])

    def test_box_set_angular_velocity(self):
        box = pal.body.Box((0,0,0),(1,1,1),mass=1)
        box.set_angular_velocity((10,10,10))
        self.assertEqual(box.get_angular_velocity(), [10,10,10])

    def test_box_is_active(self):
        box = pal.body.Box((0,0,0),(1,1,1),mass=1)
        self.assertTrue(box.is_active())

    def test_box_set_active(self):
        box = pal.body.Box((0,0,0),(1,1,1),mass=1)
        box.set_active(False)
        self.assertTrue(not box.is_active())

    def test_box_get_size(self):
        box = pal.body.Box((0,0,0),(1,1,1),mass=1)
        self.assertEqual(box.get_size(),(1.,1.,1.))

#  ______   _______   __    __  ________  _______   ________        ________  ________   ______  ________   ______  
# /      \ |       \ |  \  |  \|        \|       \ |        \      |        \|        \ /      \|        \ /      \ 
#|  $$$$$$\| $$$$$$$\| $$  | $$| $$$$$$$$| $$$$$$$\| $$$$$$$$       \$$$$$$$$| $$$$$$$$|  $$$$$$\\$$$$$$$$|  $$$$$$\
#| $$___\$$| $$__/ $$| $$__| $$| $$__    | $$__| $$| $$__             | $$   | $$__    | $$___\$$  | $$   | $$___\$$
# \$$    \ | $$    $$| $$    $$| $$  \   | $$    $$| $$  \            | $$   | $$  \    \$$    \   | $$    \$$    \ 
# _\$$$$$$\| $$$$$$$ | $$$$$$$$| $$$$$   | $$$$$$$\| $$$$$            | $$   | $$$$$    _\$$$$$$\  | $$    _\$$$$$$\
#|  \__| $$| $$      | $$  | $$| $$_____ | $$  | $$| $$_____          | $$   | $$_____ |  \__| $$  | $$   |  \__| $$
# \$$    $$| $$      | $$  | $$| $$     \| $$  | $$| $$     \         | $$   | $$     \ \$$    $$  | $$    \$$    $$
#  \$$$$$$  \$$       \$$   \$$ \$$$$$$$$ \$$   \$$ \$$$$$$$$          \$$    \$$$$$$$$  \$$$$$$    \$$     \$$$$$$ 
                                                                                                                   

class TestSphereFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()

    def tearDown(self):
        pal.cleanup()

    def test_sphere_create(self):
        pal.body.Sphere((0,0,0),(1,1,1),mass=1)
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_sphere_delete(self):
        sphere = pal.body.Sphere((0,0,0),(1,1,1),mass=1)
        sphere.delete()
        self.assertEqual(len(pal._pal.all_objects),0)

    def test_sphere_weakref(self):
        sphere = pal.body.Sphere((0,0,0),(1,1,1),mass=1)
        self.assertTrue(isinstance(sphere,weakref.ProxyType))

    def test_sphere_get_location(self):
        sphere = pal.body.Sphere((0,0,0),(1,1,1),mass=1)
        print "responce: ",[x for x in sphere.get_location()]
        self.assertEqual(sphere.get_location(), [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1])

    def test_sphere_get_position(self):
        sphere = pal.body.Sphere((0,0,0),(1,1,1),mass=1)
        self.assertEqual(sphere.get_position(), [0,0,0])

    def test_sphere_get_group(self):
        sphere = pal.body.Sphere((0,0,0),(1,1,1),mass=1)
        self.assertEqual(sphere.get_group(), 0)

    def test_sphere_set_group(self):
        sphere = pal.body.Sphere((0,0,0),(1,1,1),mass=1)
        sphere.set_group(10)
        self.assertEqual(sphere.get_group(), 10)

    def test_sphere_to_string(self):
        sphere = pal.body.Sphere((0,0,0),(1,1,1),mass=1)
        self.assertEqual(sphere.__str__(), "A Sphere at : 0.00, 0.00, 0.00")

    def test_sphere_set_position(self):
        sphere = pal.body.Sphere((0,0,0),(1,1,1),mass=1)
        sphere.set_position((10,10,10))
        self.assertEqual(sphere.get_position(), [10,10,10])

    def test_sphere_set_orientation(self):
        sphere = pal.body.Sphere((0,0,0),(1,1,1),mass=1)
        sphere.set_orientation((10,10,10))
        self.assertEqual(sphere.get_location(), [0.7040410041809082, 0.45647263526916504, 0.5440211296081543, 0.0, -0.7048034071922302, 0.5430330634117126, 0.45647263526916504, 0.0, -0.08705419301986694, -0.7048034071922302, 0.7040410041809082, 0.0, 0.0, 0.0, 0.0, 1.,])#TODO

    def test_sphere_apply_force(self):
        sphere = pal.body.Sphere((0,0,0),(1,1,1),mass=1)
        sphere.apply_force((1,1,1))

    def test_sphere_apply_torque(self):
        sphere = pal.body.Sphere((0,0,0),(1,1,1),mass=1)
        sphere.apply_torque((1,1,1))

    def test_sphere_apply_force_pos(self):
        sphere = pal.body.Sphere((0,0,0),(1,1,1),mass=1)
        sphere.apply_force((1,1,1),pos=(1,1,1))

    def test_sphere_apply_impulse(self):
        sphere = pal.body.Sphere((0,0,0),(1,1,1),mass=1)
        sphere.apply_impulse((1,1,1))

    def test_sphere_apply_angular_impulse(self):
        sphere = pal.body.Sphere((0,0,0),(1,1,1),mass=1)
        sphere.apply_angular_impulse((1,1,1))

    def test_sphere_apply_impulse_pos(self):
        sphere = pal.body.Sphere((0,0,0),(1,1,1),mass=1)
        sphere.apply_impulse((1,1,1),pos=(1,1,1))

    def test_sphere_get_velocity(self):
        sphere = pal.body.Sphere((0,0,0),(1,1,1),mass=1)
        self.assertEqual(sphere.get_linear_velocity(), [0,0,0])

    def test_sphere_get_angular_velocity(self):
        sphere = pal.body.Sphere((0,0,0),(1,1,1),mass=1)
        self.assertEqual(sphere.get_angular_velocity(), [0,0,0])

    def test_sphere_set_velocity(self):
        sphere = pal.body.Sphere((0,0,0),(1,1,1),mass=1)
        sphere.set_linear_velocity((10,10,10))
        self.assertEqual(sphere.get_linear_velocity(), [10,10,10])

    def test_sphere_set_angular_velocity(self):
        sphere = pal.body.Sphere((0,0,0),(1,1,1),mass=1)
        sphere.set_angular_velocity((10,10,10))
        self.assertEqual(sphere.get_angular_velocity(), [10,10,10])

    def test_sphere_is_active(self):
        sphere = pal.body.Sphere((0,0,0),(1,1,1),mass=1)
        self.assertTrue(sphere.is_active())

    def test_sphere_set_active(self):
        sphere = pal.body.Sphere((0,0,0),(1,1,1),mass=1)
        sphere.set_active(False)
        self.assertTrue(not sphere.is_active())

    def test_sphere_get_size(self):
        sphere = pal.body.Sphere((0,0,0),(1,1,1),mass=1)
        self.assertEqual(sphere.get_size(),(1.,1.,1.))

#  ______    ______   _______    ______   __    __  __        ________        ________  ________   ______  ________   ______  
# /      \  /      \ |       \  /      \ |  \  |  \|  \      |        \      |        \|        \ /      \|        \ /      \ 
#|  $$$$$$\|  $$$$$$\| $$$$$$$\|  $$$$$$\| $$  | $$| $$      | $$$$$$$$       \$$$$$$$$| $$$$$$$$|  $$$$$$\\$$$$$$$$|  $$$$$$\
#| $$   \$$| $$__| $$| $$__/ $$| $$___\$$| $$  | $$| $$      | $$__             | $$   | $$__    | $$___\$$  | $$   | $$___\$$
#| $$      | $$    $$| $$    $$ \$$    \ | $$  | $$| $$      | $$  \            | $$   | $$  \    \$$    \   | $$    \$$    \ 
#| $$   __ | $$$$$$$$| $$$$$$$  _\$$$$$$\| $$  | $$| $$      | $$$$$            | $$   | $$$$$    _\$$$$$$\  | $$    _\$$$$$$\
#| $$__/  \| $$  | $$| $$      |  \__| $$| $$__/ $$| $$_____ | $$_____          | $$   | $$_____ |  \__| $$  | $$   |  \__| $$
# \$$    $$| $$  | $$| $$       \$$    $$ \$$    $$| $$     \| $$     \         | $$   | $$     \ \$$    $$  | $$    \$$    $$
#  \$$$$$$  \$$   \$$ \$$        \$$$$$$   \$$$$$$  \$$$$$$$$ \$$$$$$$$          \$$    \$$$$$$$$  \$$$$$$    \$$     \$$$$$$ 
                                                                                                                             

class TestCapsuleFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()

    def tearDown(self):
        pal.cleanup()

    def test_capsule_create(self):
        pal.body.Capsule((0,0,0),(1,1,1),mass=1)
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_capsule_delete(self):
        capsule = pal.body.Capsule((0,0,0),(1,1,1),mass=1)
        capsule.delete()
        self.assertEqual(len(pal._pal.all_objects),0)

    def test_capsule_weakref(self):
        capsule = pal.body.Capsule((0,0,0),(1,1,1),mass=1)
        self.assertTrue(isinstance(capsule,weakref.ProxyType))

    def test_capsule_get_location(self):
        capsule = pal.body.Capsule((0,0,0),(1,1,1),mass=1)
        print "responce: ",[x for x in capsule.get_location()]
        self.assertEqual(capsule.get_location(), [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1])

    def test_capsule_get_position(self):
        capsule = pal.body.Capsule((0,0,0),(1,1,1),mass=1)
        self.assertEqual(capsule.get_position(), [0,0,0])

    def test_capsule_get_group(self):
        capsule = pal.body.Capsule((0,0,0),(1,1,1),mass=1)
        self.assertEqual(capsule.get_group(), 0)

    def test_capsule_set_group(self):
        capsule = pal.body.Capsule((0,0,0),(1,1,1),mass=1)
        capsule.set_group(10)
        self.assertEqual(capsule.get_group(), 10)

    def test_capsule_to_string(self):
        capsule = pal.body.Capsule((0,0,0),(1,1,1),mass=1)
        self.assertEqual(capsule.__str__(), "A Capsule at : 0.00, 0.00, 0.00")

    def test_capsule_set_position(self):
        capsule = pal.body.Capsule((0,0,0),(1,1,1),mass=1)
        capsule.set_position((10,10,10))
        self.assertEqual(capsule.get_position(), [10,10,10])

    def test_capsule_set_orientation(self):
        capsule = pal.body.Capsule((0,0,0),(1,1,1),mass=1)
        capsule.set_orientation((10,10,10))
        self.assertEqual(capsule.get_location(), [0.7040410041809082, 0.45647263526916504, 0.5440211296081543, 0.0, -0.7048034071922302, 0.5430330634117126, 0.45647263526916504, 0.0, -0.08705419301986694, -0.7048034071922302, 0.7040410041809082, 0.0, 0.0, 0.0, 0.0, 1.,])#TODO

    def test_capsule_apply_force(self):
        capsule = pal.body.Capsule((0,0,0),(1,1,1),mass=1)
        capsule.apply_force((1,1,1))

    def test_capsule_apply_torque(self):
        capsule = pal.body.Capsule((0,0,0),(1,1,1),mass=1)
        capsule.apply_torque((1,1,1))

    def test_capsule_apply_force_pos(self):
        capsule = pal.body.Capsule((0,0,0),(1,1,1),mass=1)
        capsule.apply_force((1,1,1),pos=(1,1,1))

    def test_capsule_apply_impulse(self):
        capsule = pal.body.Capsule((0,0,0),(1,1,1),mass=1)
        capsule.apply_impulse((1,1,1))

    def test_capsule_apply_angular_impulse(self):
        capsule = pal.body.Capsule((0,0,0),(1,1,1),mass=1)
        capsule.apply_angular_impulse((1,1,1))

    def test_capsule_apply_impulse_pos(self):
        capsule = pal.body.Capsule((0,0,0),(1,1,1),mass=1)
        capsule.apply_impulse((1,1,1),pos=(1,1,1))

    def test_capsule_get_velocity(self):
        capsule = pal.body.Capsule((0,0,0),(1,1,1),mass=1)
        self.assertEqual(capsule.get_linear_velocity(), [0,0,0])

    def test_capsule_get_angular_velocity(self):
        capsule = pal.body.Capsule((0,0,0),(1,1,1),mass=1)
        self.assertEqual(capsule.get_angular_velocity(), [0,0,0])

    def test_capsule_set_velocity(self):
        capsule = pal.body.Capsule((0,0,0),(1,1,1),mass=1)
        capsule.set_linear_velocity((10,10,10))
        self.assertEqual(capsule.get_linear_velocity(), [10,10,10])

    def test_capsule_set_angular_velocity(self):
        capsule = pal.body.Capsule((0,0,0),(1,1,1),mass=1)
        capsule.set_angular_velocity((10,10,10))
        self.assertEqual(capsule.get_angular_velocity(), [10,10,10])

    def test_capsule_is_active(self):
        capsule = pal.body.Capsule((0,0,0),(1,1,1),mass=1)
        self.assertTrue(capsule.is_active())

    def test_capsule_set_active(self):
        capsule = pal.body.Capsule((0,0,0),(1,1,1),mass=1)
        capsule.set_active(False)
        self.assertTrue(not capsule.is_active())

    def test_capsule_get_size(self):
        capsule = pal.body.Capsule((0,0,0),(1,1,1),mass=1)
        self.assertEqual(capsule.get_size(),(1.,1.,1.))

#  ______    ______   __       __  _______    ______   __    __  __    __  _______         ________  ________   ______  ________   ______  
# /      \  /      \ |  \     /  \|       \  /      \ |  \  |  \|  \  |  \|       \       |        \|        \ /      \|        \ /      \ 
#|  $$$$$$\|  $$$$$$\| $$\   /  $$| $$$$$$$\|  $$$$$$\| $$  | $$| $$\ | $$| $$$$$$$\       \$$$$$$$$| $$$$$$$$|  $$$$$$\\$$$$$$$$|  $$$$$$\
#| $$   \$$| $$  | $$| $$$\ /  $$$| $$__/ $$| $$  | $$| $$  | $$| $$$\| $$| $$  | $$         | $$   | $$__    | $$___\$$  | $$   | $$___\$$
#| $$      | $$  | $$| $$$$\  $$$$| $$    $$| $$  | $$| $$  | $$| $$$$\ $$| $$  | $$         | $$   | $$  \    \$$    \   | $$    \$$    \ 
#| $$   __ | $$  | $$| $$\$$ $$ $$| $$$$$$$ | $$  | $$| $$  | $$| $$\$$ $$| $$  | $$         | $$   | $$$$$    _\$$$$$$\  | $$    _\$$$$$$\
#| $$__/  \| $$__/ $$| $$ \$$$| $$| $$      | $$__/ $$| $$__/ $$| $$ \$$$$| $$__/ $$         | $$   | $$_____ |  \__| $$  | $$   |  \__| $$
# \$$    $$ \$$    $$| $$  \$ | $$| $$       \$$    $$ \$$    $$| $$  \$$$| $$    $$         | $$   | $$     \ \$$    $$  | $$    \$$    $$
#  \$$$$$$   \$$$$$$  \$$      \$$ \$$        \$$$$$$   \$$$$$$  \$$   \$$ \$$$$$$$           \$$    \$$$$$$$$  \$$$$$$    \$$     \$$$$$$ 

class TestCompoundFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()

    def tearDown(self):
        pal.cleanup()

    def test_compound_create(self):
        pal.body.Compound((0,0,0))
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_compound_delete(self):
        compound = pal.body.Compound((0,0,0))
        compound.delete()
        self.assertEqual(len(pal._pal.all_objects),0)

    def test_compound_weakref(self):
        compound = pal.body.Compound((0,0,0))
        self.assertTrue(isinstance(compound,weakref.ProxyType))

    def test_compound_get_location(self):
        compound = pal.body.Compound((0,0,0))
        print "responce: ",[x for x in compound.get_location()]
        self.assertEqual(compound.get_location(), [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1])

    def test_compound_get_position(self):
        compound = pal.body.Compound((0,0,0))
        self.assertEqual(compound.get_position(), [0,0,0])

    def test_compound_get_group(self):
        compound = pal.body.Compound((0,0,0))
        self.assertEqual(compound.get_group(), 0)

    def test_compound_set_group(self):
        compound = pal.body.Compound((0,0,0))
        compound.set_group(10)
        self.assertEqual(compound.get_group(), 10)

    def test_compound_to_string(self):
        compound = pal.body.Compound((0,0,0))
        self.assertEqual(compound.__str__(), "A CompoundBody at : 0.00, 0.00, 0.00")

    def test_compound_set_position(self):
        compound = pal.body.Compound((0,0,0))
        compound.set_position((10,10,10))
        self.assertEqual(compound.get_position(), [10,10,10])

    def test_compound_set_orientation(self):
        compound = pal.body.Compound((0,0,0))
        compound.set_orientation((10,10,10))
        self.assertEqual(compound.get_location(), [0.7040410041809082, 0.45647263526916504, 0.5440211296081543, 0.0, -0.7048034071922302, 0.5430330634117126, 0.45647263526916504, 0.0, -0.08705419301986694, -0.7048034071922302, 0.7040410041809082, 0.0, 0.0, 0.0, 0.0, 1.,])#TODO

    def test_compound_apply_force(self):
        compound = pal.body.Compound((0,0,0))
        compound.add_box((0,0,0,1,1,1), 1)
        compound.finalize()
        compound.apply_force((1,1,1))

    def test_compound_apply_torque(self):
        compound = pal.body.Compound((0,0,0))
        compound.add_box((0,0,0,1,1,1), 1)
        compound.finalize()
        compound.apply_torque((1,1,1))

    def test_compound_apply_force_pos(self):
        compound = pal.body.Compound((0,0,0))
        compound.add_box((0,0,0,1,1,1), 1)
        compound.finalize()
        compound.apply_force((1,1,1),pos=(1,1,1))

    def test_compound_apply_impulse(self):
        compound = pal.body.Compound((0,0,0))
        compound.add_box((0,0,0,1,1,1), 1)
        compound.finalize()
        compound.apply_impulse((1,1,1))

    def test_compound_apply_angular_impulse(self):
        compound = pal.body.Compound((0,0,0))
        compound.add_box((0,0,0,1,1,1), 1)
        compound.finalize()
        compound.apply_angular_impulse((1,1,1))

    def test_compound_apply_impulse_pos(self):
        compound = pal.body.Compound((0,0,0))
        compound.add_box((0,0,0,1,1,1), 1)
        compound.finalize()
        compound.apply_impulse((1,1,1),pos=(1,1,1))

    def test_compound_get_velocity(self):
        compound = pal.body.Compound((0,0,0))
        compound.add_box((0,0,0,1,1,1), 1)
        compound.finalize()
        self.assertEqual(compound.get_linear_velocity(), [0,0,0])

    def test_compound_get_angular_velocity(self):
        compound = pal.body.Compound((0,0,0))
        compound.add_box((0,0,0,1,1,1), 1)
        compound.finalize()
        self.assertEqual(compound.get_angular_velocity(), [0,0,0])

    def test_compound_set_velocity(self):
        compound = pal.body.Compound((0,0,0))
        compound.add_box((0,0,0,1,1,1), 1)
        compound.finalize()
        compound.set_linear_velocity((10,10,10))
        self.assertEqual(compound.get_linear_velocity(), [10,10,10])

    def test_compound_set_angular_velocity(self):
        compound = pal.body.Compound((0,0,0))
        compound.add_box((0,0,0,1,1,1), 1)
        compound.finalize()
        compound.set_angular_velocity((10,10,10))
        self.assertEqual(compound.get_angular_velocity(), [10,10,10])

    def test_compound_is_active(self):
        compound = pal.body.Compound((0,0,0))
        compound.add_box((0,0,0,1,1,1), 1)
        compound.finalize()
        self.assertTrue(compound.is_active())

    def test_compound_set_active(self):
        compound = pal.body.Compound((0,0,0))
        compound.add_box((0,0,0,1,1,1), 1)
        compound.finalize()
        compound.set_active(False)
        self.assertTrue(not compound.is_active())


#  ______    ______   __    __  __     __  ________  __    __        ________  ________   ______  ________   ______  
# /      \  /      \ |  \  |  \|  \   |  \|        \|  \  |  \      |        \|        \ /      \|        \ /      \ 
#|  $$$$$$\|  $$$$$$\| $$\ | $$| $$   | $$| $$$$$$$$| $$  | $$       \$$$$$$$$| $$$$$$$$|  $$$$$$\\$$$$$$$$|  $$$$$$\
#| $$   \$$| $$  | $$| $$$\| $$| $$   | $$| $$__     \$$\/  $$         | $$   | $$__    | $$___\$$  | $$   | $$___\$$
#| $$      | $$  | $$| $$$$\ $$ \$$\ /  $$| $$  \     >$$  $$          | $$   | $$  \    \$$    \   | $$    \$$    \ 
#| $$   __ | $$  | $$| $$\$$ $$  \$$\  $$ | $$$$$    /  $$$$\          | $$   | $$$$$    _\$$$$$$\  | $$    _\$$$$$$\
#| $$__/  \| $$__/ $$| $$ \$$$$   \$$ $$  | $$_____ |  $$ \$$\         | $$   | $$_____ |  \__| $$  | $$   |  \__| $$
# \$$    $$ \$$    $$| $$  \$$$    \$$$   | $$     \| $$  | $$         | $$   | $$     \ \$$    $$  | $$    \$$    $$
#  \$$$$$$   \$$$$$$  \$$   \$$     \$     \$$$$$$$$ \$$   \$$          \$$    \$$$$$$$$  \$$$$$$    \$$     \$$$$$$ 



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
        pal.body.Convex((0,0,0),self.points,mass=1)
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_convex_create_triangles(self):
        pal.body.Convex((0,0,0),self.points,self.triangles,mass=1)
        self.assertEqual(len(pal._pal.all_objects),1)

    #def test_convex_delete(self):
    #    convex = pal.body.Convex((0,0,0),self.points,mass=1)
    #    convex.delete()
    #    self.assertEqual(len(pal._pal.all_objects),0)

    def test_convex_weakref(self):
        convex = pal.body.Convex((0,0,0),self.points,mass=1)
        self.assertTrue(isinstance(convex,weakref.ProxyType))

    def test_convex_get_location(self):
        convex = pal.body.Convex((0,0,0),self.points,mass=1)
        print "responce: ",[x for x in convex.get_location()]
        self.assertEqual(convex.get_location(), [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1])

    def test_convex_get_position(self):
        convex = pal.body.Convex((0,0,0),self.points,mass=1)
        self.assertEqual(convex.get_position(), [0,0,0])

    def test_convex_get_group(self):
        convex = pal.body.Convex((0,0,0),self.points,mass=1)
        self.assertEqual(convex.get_group(), 0)

    def test_convex_set_group(self):
        convex = pal.body.Convex((0,0,0),self.points,mass=1)
        convex.set_group(10)
        self.assertEqual(convex.get_group(), 10)

    def test_convex_to_string(self):
        convex = pal.body.Convex((0,0,0),self.points,mass=1)
        self.assertEqual(convex.__str__(), "A ConvexBody at : 0.00, 0.00, 0.00")

    def test_convex_set_position(self):
        convex = pal.body.Convex((0,0,0),self.points,mass=1)
        convex.set_position((10,10,10))
        self.assertEqual(convex.get_position(), [10,10,10])

    def test_convex_set_orientation(self):
        convex = pal.body.Convex((0,0,0),self.points,mass=1)
        convex.set_orientation((10,10,10))
        self.assertEqual(convex.get_location(), [0.7040410041809082, 0.45647263526916504, 0.5440211296081543, 0.0, -0.7048034071922302, 0.5430330634117126, 0.45647263526916504, 0.0, -0.08705419301986694, -0.7048034071922302, 0.7040410041809082, 0.0, 0.0, 0.0, 0.0, 1.,])#TODO

    def test_convex_apply_force(self):
        convex = pal.body.Convex((0,0,0),self.points,mass=1)
        convex.apply_force((1,1,1))

    def test_convex_apply_torque(self):
        convex = pal.body.Convex((0,0,0),self.points,mass=1)
        convex.apply_torque((1,1,1))

    def test_convex_apply_force_pos(self):
        convex = pal.body.Convex((0,0,0),self.points,mass=1)
        convex.apply_force((1,1,1),pos=(1,1,1))

    def test_convex_apply_impulse(self):
        convex = pal.body.Convex((0,0,0),self.points,mass=1)
        print "DEBUG APPLYING IMPULSE" 
        convex.apply_impulse((1,1,1))

    def test_convex_apply_angular_impulse(self):
        convex = pal.body.Convex((0,0,0),self.points,mass=1)
        convex.apply_angular_impulse((1,1,1))

    def test_convex_apply_impulse_pos(self):
        convex = pal.body.Convex((0,0,0),self.points,mass=1)
        convex.apply_impulse((1,1,1),pos=(1,1,1))

    def test_convex_get_velocity(self):
        convex = pal.body.Convex((0,0,0),self.points,mass=1)
        self.assertEqual(convex.get_linear_velocity(), [0,0,0])

    def test_convex_get_angular_velocity(self):
        convex = pal.body.Convex((0,0,0),self.points,mass=1)
        self.assertEqual(convex.get_angular_velocity(), [0,0,0])

    def test_convex_set_velocity(self):
        convex = pal.body.Convex((0,0,0),self.points,mass=1)
        convex.set_linear_velocity((10,10,10))
        self.assertEqual(convex.get_linear_velocity(), [10,10,10])

    def test_convex_set_angular_velocity(self):
        convex = pal.body.Convex((0,0,0),self.points,mass=1)
        convex.set_angular_velocity((10,10,10))
        self.assertEqual(convex.get_angular_velocity(), [10,10,10])

    def test_convex_is_active(self):
        convex = pal.body.Convex((0,0,0),self.points,mass=1)
        self.assertTrue(convex.is_active())

    def test_convex_set_active(self):
        convex = pal.body.Convex((0,0,0),self.points,mass=1)
        convex.set_active(False)
        self.assertTrue(not convex.is_active())

#  ______                                           __                  ________  ________   ______  ________   ______  
# /      \                                         |  \                |        \|        \ /      \|        \ /      \ 
#|  $$$$$$\  ______   _______    ______    ______   \$$  _______        \$$$$$$$$| $$$$$$$$|  $$$$$$\\$$$$$$$$|  $$$$$$\
#| $$ __\$$ /      \ |       \  /      \  /      \ |  \ /       \         | $$   | $$__    | $$___\$$  | $$   | $$___\$$
#| $$|    \|  $$$$$$\| $$$$$$$\|  $$$$$$\|  $$$$$$\| $$|  $$$$$$$         | $$   | $$  \    \$$    \   | $$    \$$    \ 
#| $$ \$$$$| $$    $$| $$  | $$| $$    $$| $$   \$$| $$| $$               | $$   | $$$$$    _\$$$$$$\  | $$    _\$$$$$$\
#| $$__| $$| $$$$$$$$| $$  | $$| $$$$$$$$| $$      | $$| $$_____          | $$   | $$_____ |  \__| $$  | $$   |  \__| $$
# \$$    $$ \$$     \| $$  | $$ \$$     \| $$      | $$ \$$     \         | $$   | $$     \ \$$    $$  | $$    \$$    $$
#  \$$$$$$   \$$$$$$$ \$$   \$$  \$$$$$$$ \$$       \$$  \$$$$$$$          \$$    \$$$$$$$$  \$$$$$$    \$$     \$$$$$$ 

class TestGenericFunctions(unittest.TestCase):
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

    def test_generic_create(self):
        pal.body.GenericBody((0,0,0))
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_generic_delete(self):
        generic = pal.body.GenericBody((0,0,0))
        generic.delete()
        self.assertEqual(len(pal._pal.all_objects),0)

    def test_generic_get_location(self):
        generic = pal.body.GenericBody((0,0,0))
        self.assertEqual(generic.get_location(), [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1])

    def test_generic_get_position(self):
        generic = pal.body.GenericBody((0,0,0))
        self.assertEqual(generic.get_position(), [0,0,0])

    def test_generic_get_group(self):
        generic = pal.body.GenericBody((0,0,0))
        self.assertEqual(generic.get_group(), 0)

    def test_generic_set_group(self):
        generic = pal.body.GenericBody((0,0,0))
        generic.set_group(10)
        self.assertEqual(generic.get_group(), 10)

    def test_generic_to_string(self):
        generic = pal.body.GenericBody((0,0,0))
        self.assertEqual(generic.__str__(), "A Generic at : 0.00, 0.00, 0.00")

    def test_generic_set_position(self):
        generic = pal.body.GenericBody((0,0,0))
        generic.set_position((10,10,10))
        self.assertEqual(generic.get_position(), [10,10,10])

    def test_generic_set_orientation(self):
        generic = pal.body.GenericBody((0,0,0))
        generic.set_orientation((10,10,10))
        self.assertEqual(generic.get_location(), [0.7040410041809082, 0.45647263526916504, 0.5440211296081543, 0.0, -0.7048034071922302, 0.5430330634117126, 0.45647263526916504, 0.0, -0.08705419301986694, -0.7048034071922302, 0.7040410041809082, 0.0, 0.0, 0.0, 0.0, 1.,])#TODO

    def test_generic_apply_force(self):
        generic = pal.body.GenericBody((0,0,0))
        generic.apply_force((1,1,1))

    def test_generic_apply_torque(self):
        generic = pal.body.GenericBody((0,0,0))
        generic.apply_torque((1,1,1))

    def test_generic_apply_force_pos(self):
        generic = pal.body.GenericBody((0,0,0))
        generic.apply_force((1,1,1),pos=(1,1,1))

    def test_generic_apply_impulse(self):
        generic = pal.body.GenericBody((0,0,0))
        generic.apply_impulse((1,1,1))

    def test_generic_apply_angular_impulse(self):
        generic = pal.body.GenericBody((0,0,0))
        generic.apply_angular_impulse((1,1,1))

    def test_generic_apply_impulse_pos(self):
        generic = pal.body.GenericBody((0,0,0))
        generic.apply_impulse((1,1,1),pos=(1,1,1))

    def test_generic_get_velocity(self):
        generic = pal.body.GenericBody((0,0,0))
        self.assertEqual(generic.get_linear_velocity(), [0,0,0])

    def test_generic_get_angular_velocity(self):
        generic = pal.body.GenericBody((0,0,0))
        self.assertEqual(generic.get_angular_velocity(), [0,0,0])

    def test_generic_set_velocity(self):
        generic = pal.body.GenericBody((0,0,0))
        generic.set_linear_velocity((10,10,10))
        self.assertEqual(generic.get_linear_velocity(), [10,10,10])

    def test_generic_set_angular_velocity(self):
        generic = pal.body.GenericBody((0,0,0))
        generic.set_angular_velocity((10,10,10))
        self.assertEqual(generic.get_angular_velocity(), [10,10,10])

    def test_generic_is_active(self):
        generic = pal.body.GenericBody((0,0,0))
        self.assertTrue(generic.is_active())

    def test_generic_set_active(self):
        generic = pal.body.GenericBody((0,0,0))
        generic.set_active(False)
        self.assertTrue(not generic.is_active())

    def test_generic_dynamics_type(self):
        generic = pal.body.GenericBody((0,0,0))
        generic.dynamics_type = "static"
        self.assertEqual(generic.dynamics_type,"static")

    def test_generic_gravity(self):
        generic = pal.body.GenericBody((0,0,0))
        generic.gravity_enabled = False
        self.assertEqual(generic.gravity_enabled,False)

    def test_generic_collision(self):
        generic = pal.body.GenericBody((0,0,0))
        generic.collision_response = False
        self.assertEqual(generic.collision_response,False)

    def test_generic_mass(self):
        generic = pal.body.GenericBody((0,0,0))
        generic.mass = 100
        self.assertEqual(generic.mass,100)

    def test_generic_inertia(self):
        generic = pal.body.GenericBody((0,0,0))
        generic.inertia = (100,100,100)
        self.assertEqual(generic.inertia,[100,100,100])

    def test_generic_linear_damping(self):
        generic = pal.body.GenericBody((0,0,0))
        generic.linear_damping = 100
        self.assertEqual(generic.linear_damping,1)

    #def test_generic_angular_damping(self):
    #    generic = pal.body.GenericBody((0,0,0))
    #    generic.angular_damping = 100
    #    pal.update(1)
    #    self.assertEqual(generic.angular_damping,1)

    def test_generic_connect_box_geometry(self):
        generic = pal.body.GenericBody((0,0,0))
        geometry = pal.geometry.Box((0,0,0),(1,1,1))  
        generic.connect_geometry(geometry)

    def test_generic_connect_capsule_geometry(self):
        generic = pal.body.GenericBody((0,0,0))
        geometry = pal.geometry.Capsule((0,0,0),(1,1))  
        generic.connect_geometry(geometry)

    def test_generic_connect_convex_geometry(self):
        generic = pal.body.GenericBody((0,0,0))
        geometry = pal.geometry.Convex((0,0,0),self.points, self.triangles)  
        generic.connect_geometry(geometry)

    def test_generic_connect_concave_geometry(self):
        generic = pal.body.GenericBody((0,0,0))
        geometry = pal.geometry.Concave((0,0,0),(1,1,1))  
        generic.connect_geometry(geometry)

    def test_generic_connect_sphere_geometry(self):
        generic = pal.body.GenericBody((0,0,0))
        geometry = pal.geometry.Sphere((0,0,0),(1,))  
        generic.connect_geometry(geometry)

    #def test_generic_remove_geometry(self):
    #    generic = pal.body.GenericBody((0,0,0))
    #    geometry = pal.geometry.Box((0,0,0),(1,1,1)) 
    #    generic.connect_geometry(geometry)  
    #    generic.remove_geometry(geometry)

    def test_generic_get_geometry(self):
        generic = pal.body.GenericBody((0,0,0))
        geometry = pal.geometry.Box((0,0,0),(1,1,1))  
        generic.connect_geometry(geometry)
        self.assertEqual(generic.get_geometries(),[geometry])


suite = [unittest.TestLoader().loadTestsFromTestCase(TestBoxFunctions),
         unittest.TestLoader().loadTestsFromTestCase(TestSphereFunctions),
         unittest.TestLoader().loadTestsFromTestCase(TestCapsuleFunctions),
         unittest.TestLoader().loadTestsFromTestCase(TestCompoundFunctions),
         unittest.TestLoader().loadTestsFromTestCase(TestConvexFunctions),
         unittest.TestLoader().loadTestsFromTestCase(TestGenericFunctions)]

if __name__ == "__main__":
    suite = unittest.TestSuite(suite)
    unittest.TextTestRunner(verbosity=3).run(suite)
