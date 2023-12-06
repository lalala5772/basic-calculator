import unittest
from validator import Validator, DefaultException  # your_module은 실제 모듈의 이름으로 대체되어야 합니다.

class TestValidator(unittest.TestCase):
    def setUp(self):
        self.validator = Validator()
            
    def test_default_validate_valid_expression(self):
        expression = ["5", "+", "3", "="]
        result = self.validator.default_validate(expression)
        self.assertTrue(result)

    def test_default_validate_single_character(self):
        expression = ["="]
        with self.assertRaises(DefaultException):
            self.validator.default_validate(expression)

    def test_default_validate_invalid_first_character(self):
        expression = ["=", "5", "+", "3", "="]
        with self.assertRaises(DefaultException):
            self.validator.default_validate(expression)

    def test_default_validate_invalid_number_sequence(self):
        expression = ["5", "+", "3", "=", "+"]
        with self.assertRaises(DefaultException):
            self.validator.default_validate(expression)

    def test_default_validate_invalid_operator_sequence(self):
        expression = ["5", "+", "+", "3", "="]
        with self.assertRaises(DefaultException):
            self.validator.default_validate(expression)

    def test_default_validate_invalid_operator(self):
        expression = ["5", "&", "3", "="]
        with self.assertRaises(DefaultException):
            self.validator.default_validate(expression)

if __name__ == '__main__':
    unittest.main()
