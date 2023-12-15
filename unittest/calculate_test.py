import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_calculate_addition(self):
        expression = ['5','+','3','=']
        result = self.calculator.calculate(expression)
        self.assertEqual(result, 8)

    def test_calculate_subtraction(self):
        expression = ['10','-','2','=']
        result = self.calculator.calculate(expression)
        self.assertEqual(result, 8)

    def test_calculate_multiplication(self):
        expression = ['4','*','6','=']
        result = self.calculator.calculate(expression)
        self.assertEqual(result, 24)

    def test_calculate_complex_expression(self):
        expression = ["5","+","3","*","2","-","4","="]
        result = self.calculator.calculate(expression)
        self.assertEqual(result, 12)

if __name__ == '__main__':
    unittest.main()
