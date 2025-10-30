import unittest
from funciones import *

class Testeo_def(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(5,4,1), 7)

    def test_mult(self):
        self.assertEqual(mult(5,5), 65)

