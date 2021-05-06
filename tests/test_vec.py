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

    def test_equal(self):
        ''' Tests the equality operator.
        '''
        self.assertNotEqual(self.v1, self.v2)
        self.assertEqual(self.v1, self.v1)
        self.assertNotEqual(self.v3, self.v4)

    def test_add(self):
        ''' Tests the addition operator.
        '''
        pass

    def test_sub(self):
        ''' Tests the subtraction operator.
        '''
        pass

    def test_mul(self):
        ''' Tests the multiplication operator.
        '''
        pass

    def test_div(self):
        ''' Tests the multiplication operator.
        '''
        pass
    

if __name__ == "__main__":
    unittest.main()