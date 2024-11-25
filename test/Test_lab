import unittest
from math import sin, cos, tan, asin, acos, atan, pi
from UIT.Lab import calculate  # Імпортуємо функцію calculate з вашого проекту

class TestCalculator(unittest.TestCase):
    
    def test_sin(self):
        self.assertAlmostEqual(sin(0), 0)
        self.assertAlmostEqual(sin(pi/2), 1)
    
    def test_cos(self):
        self.assertAlmostEqual(cos(0), 1)
        self.assertAlmostEqual(cos(pi/2), 0)
    
    def test_tan(self):
        self.assertAlmostEqual(tan(0), 0)
        self.assertRaises(ValueError, tan, pi/2)  # Перевірка на нескінченність
    
    def test_ctg(self):
        self.assertEqual(1/tan(1), 1/0.5403, places=3)
        self.assertRaises(ZeroDivisionError, lambda: 1/tan(pi/2))  # Перевірка на Undefined
    
    def test_arcsin(self):
        self.assertEqual(asin(0), 0)
        self.assertRaises(ValueError, asin, 2)  # Відмова для значень більше за 1
    
    def test_arccos(self):
        self.assertEqual(acos(0), pi/2)
        self.assertRaises(ValueError, acos, 2)  # Відмова для значень більше за 1
    
    def test_arctg(self):
        self.assertEqual(atan(1), pi/4)
    
    def test_arcctg(self):
        self.assertEqual(pi/2 - atan(1), pi/4)
    
if __name__ == "__main__":
    unittest.main()
