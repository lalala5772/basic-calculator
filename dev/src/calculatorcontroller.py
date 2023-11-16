class CalculatorController:
    def __init__(self):
        self.validator = Validator()
        self.outputView = OutputView()
        self.calculator = Calculator()
        self.inputcheck = InputCheck()


    def run(self):
        final_expression = self.inputcheck.input_check()

        if final_expression != None:
            try:
                self.validator.validate(final_expression) # 최종 표현 검증 예시) "1+2+3=, 정상", "1+=, 예외"

                calculation_result = self.calculator.calculate(final_expression) # 계산기 결과 실행

                self.outputView.print(calculation_result) # 이외의 경우, 계산 결과 출력

            except Exception as exception:
                self.outputView.print(exception)
