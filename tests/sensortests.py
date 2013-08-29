import pypalgame as pal

import unittest
import weakref

class TestCompassFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()
        self.box = pal.body.Box((0,0,0,1,1,1),mass=1)

    def tearDown(self):
        pal.cleanup()

    def test_compass_create(self):
        compass = pal.sensor.Compass(self.box,[0,1,0])
        self.assertEqual(len(pal._pal.all_objects),2)

    def test_compass_get_angle(self):
        compass = pal.sensor.Compass(self.box,[0,1,0])
        self.assertEqual(compass.get_angle(),0)

class TestInclinometerFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()
        self.box = pal.body.Box((0,0,0,1,1,1),mass=1)

    def tearDown(self):
        pal.cleanup()

    def test_inclinometer_create(self):
        inclinometer = pal.sensor.Inclinometer(self.box,[0,1,0],[0,1,0],[0,1,0])
        self.assertEqual(len(pal._pal.all_objects),2)

    def test_inclinometer_get_angle(self):
        inclinometer = pal.sensor.Inclinometer(self.box,[0,1,0],[0,1,0],[0,1,0])
        self.assertEqual(inclinometer.get_angle(),0)


suite = [unittest.TestLoader().loadTestsFromTestCase(TestCompassFunctions),
         unittest.TestLoader().loadTestsFromTestCase(TestInclinometerFunctions)]

if __name__ == "__main__":
    suite = unittest.TestSuite(suite)
    unittest.TextTestRunner(verbosity=3).run(suite)
