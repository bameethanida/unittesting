import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):

    """Test the methods and constructor of the Fraction class. """

    def test_init(self):
        with self.assertRaises(TypeError):
            Fraction(3.14, 3)
        with self.assertRaises(TypeError):
            Fraction(9, 11.19)
        with self.assertRaises(TypeError):
            Fraction(0.99, 1.01)
        with self.assertRaises(TypeError):
            Fraction('hello', 9)
        with self.assertRaises(TypeError):
            Fraction(12, 'hello')
        with self.assertRaises(TypeError):
            Fraction('apple', 'banana')
        with self.assertRaises(TypeError):
            Fraction(True, 5)
        with self.assertRaises(TypeError):
            Fraction(5, False)
        with self.assertRaises(TypeError):
            Fraction(True, False)
    
    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        f = Fraction(1, -12)
        self.assertEqual("-1/12", f.__str__())
        f = Fraction(-1, -9)
        self.assertEqual("1/9", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())
        f = Fraction(0, 0)
        self.assertEqual("0/0", f.__str__())
        f = Fraction(1, 0)
        self.assertEqual("1/0", f.__str__())
        f = Fraction(-1, 0)
        self.assertEqual("-1/0", f.__str__())

    def test_add(self):
        self.assertEqual(Fraction(3, 4), Fraction(1, 12) + Fraction(2, 3))
        self.assertEqual(Fraction(5, 7), Fraction(5, 7) + Fraction(0))
        self.assertEqual(Fraction(0, 0), Fraction(0, 0) + Fraction(1, 2))
        self.assertEqual(Fraction(-3, 10), Fraction(-1, 2) + Fraction(1, 5))
        self.assertEqual(Fraction(1, 4), Fraction(5, 6) + Fraction(7, -12))
        self.assertEqual(Fraction(-5, 6), Fraction(-1, 2) + Fraction(-1, 3))
        self.assertEqual(Fraction(0, 0), Fraction(1, 0) + Fraction(-1, 0))

    def test_sub(self):
        self.assertEqual(Fraction(7, 20), Fraction(3, 4) - Fraction(2, 5))
        self.assertEqual(Fraction(5, 7), Fraction(5, 7) - Fraction(0))
        self.assertEqual(Fraction(-7, 19), Fraction(0) - Fraction(7, 19))
        self.assertEqual(Fraction(0, 0), Fraction(0, 0) - Fraction(1, 2))
        self.assertEqual(Fraction(-19, 20), Fraction(-3, 4) - Fraction(1, 5))
        self.assertEqual(Fraction(5, 6), Fraction(1, 2) - Fraction(1, -3))
        self.assertEqual(Fraction(-1, 6), Fraction(-1, 2) - Fraction(-1, 3))
        self.assertEqual(Fraction(0, 0), Fraction(1, 0) - Fraction(-1, 0))
    
    def test_mul(self):
        pass
    
    def test_gt(self):
        pass
    
    def test_neg(self):
        pass
    
    def test_eq(self):
        f = Fraction(1,2)
        g = Fraction(-40,-80)
        h = Fraction(10000,20001) # not quite 1/2
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        #TODO write more tests using other cases.
        # Consider special values like 0, 1/0, -1/0
