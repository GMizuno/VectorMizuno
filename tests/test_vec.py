'''Test code.
'''
# pylint: disable=import-error
import unittest

from VectorMizuno import Vectors


class VectorsTest(unittest.TestCase):
    def setUp(self):
        self.v1 = Vectors([0, 0, 0])
        self.v2 = Vectors([1, 1, 20])
        self.v3 = Vectors([1.9, .1, 0.1])
        self.v4 = Vectors([0, 0])
        self.v5 = Vectors([-1, 20])

    def test_equal(self):
        ''' Tests the equality operator.
        '''
        self.assertNotEqual(self.v1, self.v2)
        self.assertEqual(self.v1, self.v1)
        self.assertNotEqual(self.v3, self.v4)

    def test_add(self):
        ''' Tests the addition operator.
        '''
        self.assertEqual(self.v1 + self.v2, Vectors([1, 1, 20]))
        self.assertNotEqual(self.v3 + Vectors([0, 0, 0]), self.v1)
        self.assertEqual(self.v5 + Vectors([20, 30]), Vectors([19, 50]))
        self.assertNotEqual(self.v5 + Vectors([20, 30]), Vectors([20, 30]))

    def test_mul(self):
        ''' Tests the multiplication operator.
        '''
        self.assertEqual(self.v1*1, self.v1)
        self.assertEqual(self.v3*Vectors([0, 0, 0]), Vectors([0, 0, 0]))
        self.assertEqual(self.v5*Vectors([20, 30]), Vectors([-20, 600]))


if __name__ == "__main__":
    unittest.main()
