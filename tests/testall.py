import pypalgame as pal

import unittest
import weakref

# import all tests.
import actuatortests
import bodytests
import geometrytests
import linktests
import sensortests
import staticbodytests

# grab tests from each module
suite = [] +\
        actuatortests.suite +\
        bodytests.suite +\
        geometrytests.suite +\
        linktests.suite +\
        sensortests.suite +\
        staticbodytests.suite

if __name__ == "__main__":
    suite = unittest.TestSuite(suite)
    unittest.TextTestRunner(verbosity=3).run(suite)
