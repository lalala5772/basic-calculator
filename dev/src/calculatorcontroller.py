from validator import Validator, FactorialException, DefaultException
from view import OutputView
from calculator import Calculator
from inputcheck import InputCheck

class CalculatorController:
    def __init__(self):
        self.validator = Validator()
        self.outputView = OutputView()
        self.calculator = Calculator()
        self.inputCheck = InputCheck()

    def run(self):
        final_expression = self.inputCheck.check()

        if final_expression is not None:
            try:
                if self.validator.is_factorial_expression(final_expression): # '!' 가 포함된 경우 팩토리얼 검증, 검증 성공하면 팩토리얼 계산
                    self.validator.factorial_validate(final_expression)
                    calculation_result = self.calculator.factorial_calculate(final_expression)
                else:
                    self.validator.default_validate(final_expression) # '!' 가 포함되 있지 않은 기본 계산기 검증, 검증 성공하면 기본 계산기 계산
                    calculation_result = self.calculator.calculate(final_expression)
                self.outputView.print_calulation_result(calculation_result)  # 이외의 경우, 계산 결과 출력

            except FactorialException as exception:
                self.outputView.print_error_message(exception)
            except DefaultException as exception:
                self.outputView.print_error_message(exception)
