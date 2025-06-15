import unittest

from simple_calculator import SimpleCalculator # type: ignore

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, 1), -4)
        self.assertEqual(self.calc.add(2, 5), -3)
        
        
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(5, 5), 0)
        self.assertEqual(self.calc.subtract(5, 10), -5)
        self.assertEqual(self.calc.subtract(-9, 2), 7)
        
        
    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(10, 5), 50)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(5, -5), -25)
        self.assertEqual(self.calc.multiply(1, 5), 5)
        
        
    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(5, 0))
        self.assertEqual(self.calc.divide(5, 10), 0.5)
        self.assertEqual(self.calc.divide(9, 2), 2.5)
        