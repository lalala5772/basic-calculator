import unittest
from validator import Validator

class TestValidator(unittest.TestCase):
    def setUp(self):
        self.validator = Validator()

    def test_is_factorial_expression_with_factorial(self):
        expression = ["5", "!"]
        result = self.validator.is_factorial_expression(expression)
        self.assertTrue(result)

    def test_is_factorial_expression_without_factorial(self):
        expression = ["5", "+", "3", "="]
        result = self.validator.is_factorial_expression(expression)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
