import unittest
from calculator import calculate
from math import pi

class TestCalculator(unittest.TestCase):
    def test_sin(self):
        self.assertAlmostEqual(calculate("sin", 0), 0)

    def test_cos(self):
        self.assertAlmostEqual(calculate("cos", 0), 1)

    def test_tg(self):
        self.assertAlmostEqual(calculate("tg", 0), 0)

    def test_ctg(self):
        self.assertNotEqual(calculate("ctg", 0), "Undefined")
        self.assertEqual(calculate("ctg", pi / 4), 1)

    def test_arcsin(self):
        self.assertAlmostEqual(calculate("arcsin", 0), 0)
        self.assertEqual(calculate("arcsin", 2), "Undefined")

    def test_arccos(self):
        self.assertAlmostEqual(calculate("arccos", 1), 0)
        self.assertEqual(calculate("arccos", -2), "Undefined")

    def test_arctg(self):
        self.assertAlmostEqual(calculate("arctg", 1), pi / 4)

    def test_arcctg(self):
        self.assertAlmostEqual(calculate("arcctg", 1), pi / 4)

    def test_invalid_operation(self):
        self.assertEqual(calculate("invalid", 0), "Unsupported operation")

if __name__ == "__main__":
    unittest.main()
