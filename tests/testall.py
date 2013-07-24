import pypalgame as pal

import unittest
import weakref

# import all tests.
import linktests
import bodytests

# grab tests from each module
suite = [] + linktests.suite + bodytests.suite

if __name__ == "__main__":
    suite = unittest.TestSuite(suite)
    unittest.TextTestRunner(verbosity=3).run(suite)
