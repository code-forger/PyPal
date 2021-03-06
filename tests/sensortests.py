import pypal as pal

import unittest
import weakref

class TestCompassFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()
        self.sphere = pal.body.Sphere((0,0,0),(1,),mass=1)

    def tearDown(self):
        pal.cleanup()

    def test_compass_create(self):
        compass = pal.sensor.Compass(self.sphere,[0,1,0])
        self.assertEqual(len(pal._pal.all_objects),2)

    def test_compass_delete(self):
        compass = pal.sensor.Compass(self.sphere,[0,1,0])
        compass.delete()
        self.assertEqual(len(pal._pal.all_objects),1)

    def test_compass_get_angle(self):
        compass = pal.sensor.Compass(self.sphere,[0,1,0])
        self.assertEqual(compass.get_angle(),0)

class TestInclinometerFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()
        self.sphere = pal.body.Sphere((0,0,0),(1,),mass=1)

    def tearDown(self):
        pal.cleanup()

    def test_inclinometer_create(self):
        inclinometer = pal.sensor.Inclinometer(self.sphere,[0,1,0],[0,1,0],[0,1,0])
        self.assertEqual(len(pal._pal.all_objects),2)

    def test_inclinometer_get_angle(self):
        inclinometer = pal.sensor.Inclinometer(self.sphere,[0,1,0],[0,1,0],[0,1,0])
        self.assertEqual(inclinometer.get_angle(),0)

class TestPSDFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()
        self.sphere = pal.body.Sphere((0,0,0),(1,),mass=1)

    def tearDown(self):
        pal.cleanup()

    def test_psd_create(self):
        psd = pal.sensor.PSD(self.sphere,[0,1,0],[0,1,0])
        self.assertEqual(len(pal._pal.all_objects),2)

    def test_psd_get_angle(self):
        psd = pal.sensor.PSD(self.sphere,[0,1,0],[0,1,0])
        self.assertEqual(psd.get_distance(),0)

class TestGPSFunctions(unittest.TestCase):
    def setUp(self):
        pal.init()
        self.sphere = pal.body.Sphere((0,0,0),(1,),mass=1)

    def tearDown(self):
        pal.cleanup()

    def test_gps_create(self):
        gps = pal.sensor.GPS(self.sphere,100,10,10)
        self.assertEqual(len(pal._pal.all_objects),2)

    def test_gps_get_angle(self):
        self.box = pal.body.Box((0,0,0),(1,1,1),mass=1)
        gps = pal.sensor.GPS(self.box,100,10,10)
        self.assertEqual(gps.get_string().split(",")[2],'A')


suite = [unittest.TestLoader().loadTestsFromTestCase(TestCompassFunctions),
         unittest.TestLoader().loadTestsFromTestCase(TestInclinometerFunctions),
         unittest.TestLoader().loadTestsFromTestCase(TestGPSFunctions),
         unittest.TestLoader().loadTestsFromTestCase(TestPSDFunctions)]

if __name__ == "__main__":
    suite = unittest.TestSuite(suite)
    unittest.TextTestRunner(verbosity=3).run(suite)
