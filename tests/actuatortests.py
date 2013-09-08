import pypalgame as pal

import unittest
import weakref

class TestDCMotorFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()
        self.sphere = pal.body.Sphere((0,0,0,1),mass=1)
        self.ssphere = pal.body.StaticSphere((5,0,0,1))
        self.link = pal.link.Revolute(self.ssphere, self.sphere,
                                      self.ssphere.get_position(),[0,1,0],
                                      True)

    def tearDown(self):
        pal.cleanup()

    def test_dcmotor_create(self):
        dcmotor = pal.actuator.DCMotor(self.link,100,1,1)
        self.assertEqual(len(pal._pal.all_objects),4)

    def test_dcmotor_turn_on(self):
        dcmotor = pal.actuator.DCMotor(self.link,100,1,1)
        dcmotor.turn_on()
        self.assertEqual(len(pal.get_actions()),1)

    def test_dcmotor_run(self):
        dcmotor = pal.actuator.DCMotor(self.link,100,1,1)
        dcmotor.run()

class TestSpringFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()
        self.sphere = pal.body.Sphere((0,0,0,1),mass=1)
        self.ssphere = pal.body.Sphere((5,0,0,1),mass=1)

    def tearDown(self):
        pal.cleanup()

    def test_spring_create(self):
        spring = pal.actuator.Spring(self.sphere,self.ssphere,5,10,1)
        self.assertEqual(len(pal._pal.all_objects),3)

    def test_spring_run(self):
        spring = pal.actuator.Spring(self.sphere,self.ssphere,5,10,1)
        spring.run()

class TestImpulseFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()
        self.sphere = pal.body.Sphere((0,0,0,1),mass=1)

    def tearDown(self):
        pal.cleanup()

    def test_impulse_create(self):
        impulse = pal.actuator.Impulse(self.sphere,self.sphere.get_position(),[0,1,0])
        self.assertEqual(len(pal._pal.all_objects),2)

    def test_impulse_run(self):
        impulse = pal.actuator.Impulse(self.sphere,self.sphere.get_position(),[0,1,0])
        impulse.run()

    def test_impulse_set_impulse(self):
        impulse = pal.actuator.Impulse(self.sphere,self.sphere.get_position(),[0,1,0])
        impulse.set_impulse(10)

class TestForceFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()
        self.sphere = pal.body.Sphere((0,0,0,1),mass=1)

    def tearDown(self):
        pal.cleanup()

    def test_force_create(self):
        force = pal.actuator.Force(self.sphere,self.sphere.get_position(),[0,1,0])
        self.assertEqual(len(pal._pal.all_objects),2)

    def test_force_run(self):
        force = pal.actuator.Force(self.sphere,self.sphere.get_position(),[0,1,0])
        force.run()

    def test_force_set_force(self):
        force = pal.actuator.Force(self.sphere,self.sphere.get_position(),[0,1,0])
        force.set_force(10)

class TestFakeBuoyancyFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()
        self.sphere = pal.body.Sphere((0,0,0,1),mass=1)

    def tearDown(self):
        pal.cleanup()

    def test_fake_buoyancy_create(self):
        fake_buoyancy = pal.actuator.FakeBuoyancy(self.sphere)
        self.assertEqual(len(pal._pal.all_objects),2)

    def test_fake_buoyancy_run(self):
        fake_buoyancy = pal.actuator.FakeBuoyancy(self.sphere)
        fake_buoyancy.run()

class TestHydrofoilFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()
        self.sphere = pal.body.Sphere((0,0,0,1),mass=1)

    def tearDown(self):
        pal.cleanup()

    def test_hydrofoil_create(self):
        hydrofoil = pal.actuator.Hydrofoil(self.sphere,self.sphere.get_position(),(0,0,0),(0,1,0),10,1,1,1,1)
        self.assertEqual(len(pal._pal.all_objects),2)

    def test_hydrofoil_run(self):
        hydrofoil = pal.actuator.Hydrofoil(self.sphere,self.sphere.get_position(),(0,0,0),(0,1,0),10,1,1,1,1)
        hydrofoil.run()

    def test_hydrofoil_set_angle(self):
        hydrofoil = pal.actuator.Hydrofoil(self.sphere,self.sphere.get_position(),(0,0,0),(0,1,0),10,1,1,1,1)
        hydrofoil.set_angle(10)


suite = [unittest.TestLoader().loadTestsFromTestCase(TestDCMotorFunctions),
         unittest.TestLoader().loadTestsFromTestCase(TestSpringFunctions),
         unittest.TestLoader().loadTestsFromTestCase(TestImpulseFunctions),
         unittest.TestLoader().loadTestsFromTestCase(TestForceFunctions),
         unittest.TestLoader().loadTestsFromTestCase(TestFakeBuoyancyFunctions),
         unittest.TestLoader().loadTestsFromTestCase(TestHydrofoilFunctions)]

if __name__ == "__main__":
    suite = unittest.TestSuite(suite)
    unittest.TextTestRunner(verbosity=3).run(suite)
