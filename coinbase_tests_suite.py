import unittest
from coinbase_tests import *


suite = unittest.TestSuite()
suite.addTest(HomePageProducts('testProductsExist'))

for i in range(10):
    suite.addTest(HomePageProducts('testProductsLink'))


if __name__ == "__main__": 
    runner = unittest.TextTestRunner()
    runner.run(suite)
