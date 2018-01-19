import unittest
from flatmapy import *


class TestCore(unittest.TestCase):
    """
    @classmethod
    def setUpClass(cls):
        # procedures before tests are started. This code block is executed only once

    @classmethod
    def tearDownClass(cls):
        # procedures after tests are finished. This code block is executed only once

    def setUp(self):
        # procedures before every tests are started. This code block is executed every time

    def tearDown(self):
        # procedures after every tests are finished. This code block is executed every time
    """

    def test_flatmap_list(self):
        # one test case. here. 
        # You must “test_” prefix always. Unless, unittest ignores
        self.assertEqual(flatmap(str, [[1,2,3], [4,5,6]]), ['1','2','3','4','5','6'])
        self.assertEqual(flatmap(lambda x: x > 3, [[1,2,3], [4,5,6]]), [False, False, False, True, True, True])
    
    def test_flatmap_tuple(self):
        self.assertEqual(flatmap(str, ((1,2,3), (4,5,6))), ('1','2','3','4','5','6'))
        self.assertEqual(flatmap(lambda x: x > 3, ((1,2,3), (4,5,6))), (False, False, False, True, True, True))        

    def test_flatten_list(self):
        self.assertEqual(flatten([[1,2,3], [4,5,6]]), [1,2,3,4,5,6])
        self.assertEqual(flatten([[1,2,3], [4,[5,6]]]), [1,2,3,4,[5,6]])

    def test_flatten_tuple(self):
        self.assertEqual(flatten(((1,2,3), (4,5,6))), (1,2,3,4,5,6))
        self.assertEqual(flatten(((1,2,3), (4,(5,6)))), (1,2,3,4,(5,6)))        

    def test_flat_all_list(self):
        self.assertEqual(flat_all(((1,2,3), (4,5,6))), (1,2,3,4,5,6))
        self.assertEqual(flat_all(((1,2,3), (4,(5,6)))), (1,2,3,4,5,6))

    def test_flat_all_tuple(self):
        self.assertEqual(flat_all(((1,2,3), (4,5,6))), (1,2,3,4,5,6))
        self.assertEqual(flat_all(((1,2,3), (4,(5,6)))), (1,2,3,4,5,6))


if __name__ == '__main__':
    unittest.main()
