"""
Unittest the ensemble class
"""
import time

from aerotech import Ensemble
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        ip = 'localhost'
        port = 8000
        self.my_ensemble = Ensemble(ip, port)
        self.my_ensemble.connect()
        self.my_ensemble.move(1, 10, 5.5)
        time.sleep(2)

    def test_ensemble(self):
        self.assertEqual(self.my_ensemble.get_positions()['X'], 1.0)

    def tearDown(self):
        self.my_ensemble.close()

if __name__ == '__main__':
    unittest.main()
