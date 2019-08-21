import unittest
from listutil import unique
 
class ListUtilTest(unittest.TestCase):

    """ Test cases for unique function """

    def test_empty_list(self):
        self.assertEqual([], unique([]))
    
    def test_one_item_list(self):
        self.assertListEqual([-9], unique([-9]))
        self.assertListEqual([11], unique([11]))
        self.assertListEqual([3.14], unique([3.14]))
        self.assertListEqual(['Python'], unique(['Python']))
        self.assertListEqual([None], unique([None]))
        self.assertListEqual([True], unique([True]))
        self.assertListEqual([False], unique([False]))

    def test_one_item_with_duplication_list(self):
        self.assertListEqual([-1], unique([-1, -1, -1]))
        self.assertListEqual([1], unique([1, 1, 1, 1, 1]))
        self.assertListEqual([3.14], unique([3.14, 3.14]))
        self.assertListEqual(['Hello'], unique(['Hello', 'Hello', 'Hello']))
        self.assertListEqual([None], unique([None, None]))
        self.assertListEqual([True], unique([True, True, True, True]))
        self.assertListEqual([False], unique([False, False]))
    
    def test_two_items_list(self):
        self.assertListEqual([-1, -2], unique([-1, -2]))
        self.assertListEqual([1, 2], unique([1, 2]))
        self.assertListEqual([1.99, 2.99], unique([1.99, 2.99]))
        self.assertListEqual(['a', 'b'], unique(['a', 'b']))
        self.assertListEqual([None, 'A'], unique([None, 'A']))
        self.assertListEqual([True, False], unique([True, False]))
    
    def test_two_items_with_duplication_and_order_list(self):
        self.assertListEqual([-2, -1], sorted(unique([-1, -1, -1, -2])))
        self.assertListEqual([1, 3], sorted(unique([3, 3, 3, 1])))
        self.assertListEqual([2.00, 2.01], sorted(unique([2.00, 2.00, 2.01, 2.01])))
        self.assertListEqual(['x', 'y'], sorted(unique(['y', 'y', 'y', 'x', 'x'])))
        # Cannot sort 'int' with 'string'

    def test_multiple_items_list(self):
        self.assertListEqual([-1, -2, -4, -5], unique([-1, -2, -4, -5]))
        self.assertListEqual([5, 4, 3, 2], unique([5, 4, 3, 2]))
        self.assertListEqual([3.32, 0.33, 9.22], unique([3.32, 0.33, 9.22]))
        self.assertListEqual(['a', 'b', 'c', 'd'], unique(['a', 'b', 'c', 'd']))
    
    def test_multiple_items_with_duplication_and_order_list(self):
        self.assertListEqual([-2, -1, 0], sorted(unique([-1, 0, 0, -1, -1, -2])))
        self.assertListEqual([1, 3, 5], sorted(unique([5, 5, 3, 3, 3, 1])))
        self.assertListEqual([0.19, 2.00, 2.01], sorted(unique([2.00, 2.00, 2.01, 0.19, 0.19, 2.01])))
        self.assertListEqual(['A', 'B', 'E'], sorted(unique(['E', 'E', 'B', 'A', 'A'])))
        self.assertListEqual(['A', 'B', 'a', 'b'], sorted(unique(['a', 'b', 'B', 'A', 'A'])))
        # Cannot sort 'int' with 'string'
    
    def test_one_nested_list(self):
        self.assertListEqual([5, [2, 3, 4]], unique([5, [2, 3, 4]]))
        self.assertListEqual([['a', 'b'], 'apple'], unique([['a', 'b'], 'apple']))
    
    def test_one_nested_with_duplication_list(self):
        self.assertListEqual([1, [2, 3, 4]], unique([1, 1, 1, [2, 3, 4], [2, 3, 4]]))
        self.assertListEqual(['banana', ['a', 'b'], 'apple'], unique(['banana', 'banana', ['a', 'b'], 'apple']))
    
    def test_multiple_nested_list(self):
        self.assertListEqual([[1], [2], 1.99], unique([[1], [2], 1.99]))
        self.assertListEqual(['q', 'w', ['banana', 'apple', 'orange'], ['python', 'java'], ['hello']], 
        unique(['q', 'w', ['banana', 'apple', 'orange'], ['python', 'java'], ['hello']]))

    def test_argument_not_a_list(self):
        with self.assertRaises(TypeError):
            unique(-123)
        with self.assertRaises(TypeError):
            unique(999)
        with self.assertRaises(TypeError):
            unique(3.14)
        with self.assertRaises(TypeError):
            unique('ISP')
        with self.assertRaises(TypeError):
            unique()
        with self.assertRaises(TypeError):
            unique(True)
        with self.assertRaises(TypeError):
            unique(None)
    

if __name__ == '__main__':
    unittest.main()