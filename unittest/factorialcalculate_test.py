import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_factorial_calculate(self):
        expression = ["5", "!"]
        result = self.calculator.factorial_calculate(expression)
        self.assertEqual(result, 120)
        
        expression = ["1", "!"]
        result = self.calculator.factorial_calculate(expression)
        self.assertEqual(result, 1)
        
        expression = ["10", "!"]
        result = self.calculator.factorial_calculate(expression)
        self.assertEqual(result, 3628800)


if __name__ == '__main__':
    unittest.main()
