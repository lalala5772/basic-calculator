from easteregg import EasterEgg

class CalculatorInput:
    def __init__(self, input_str):
        self.input_str = input_str

    def cal_input(self):
        # 정수인지 판단 - 양수 or 음수
        egg = EasterEgg() # easteregg 객체선언
        if self.input_str.isdigit() or (self.input_str[1:].isdigit() and self.input_str[0] == '-'):
            egg.checkEasterEgg(self.input_str) # input값이 easteregg인지 체크
            return "Integer"
        # 기호인지 판단
        elif self.input_str in ['+', '-', '*']:
            return "Operator"
        # '='인지 판단
        elif self.input_str == '=':
            return "Equal"
        # 그외 판단
        else:
            return "Other"

# 사용 예시
# user_input = input("숫자 또는 기호를 입력하세요: ")
# cal_class = CalculatorInput(user_input)
# result = cal_class.cal_input()
# print(f"입력된 값은 {result}입니다.")
