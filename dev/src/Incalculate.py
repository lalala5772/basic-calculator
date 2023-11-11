
class Incalculate:
    def calculate(self, expression):
        expression = expression.rstrip('=').strip()# = 제거
        operators = ['+', '-', '*']

        numbers = []
        operators_stack = []

        current_number = None

        for char in expression:
            if char.isdigit():
                current_number = int(char) if current_number is None else current_number * 10 + int(char)# 숫자면 current number에 넣어주기
            elif char in operators:
                if current_number is not None:# 연산자 같은경우 current number가 아니기때문에 perform operation을 불러옵니다.
                    numbers.append(current_number)
                    current_number = None

                    while operators_stack and self.get_precedence(operators_stack[-1]) >= self.get_precedence(char):
                        self.calculate_stack(numbers, operators_stack) # 연산자 우선순위, 우선순위가 높은 애들먼저 처리해줍니다

                    operators_stack.append(char)

        if current_number is not None: # 현재 number가 None이 아니면 numbers 에 추가해줍니다 
            numbers.append(current_number)

        while operators_stack: 
            self.calculate_stack(numbers, operators_stack)

        return numbers[0] if numbers else None

    def get_precedence(self, operator): # 연산자 우선순위 표시 
        if operator == '*':
            return 2
        elif operator == '+' or operator == '-':
            return 1
        else:
            return 0

    def calculate_stack(self, numbers, operators_stack):
        operator = operators_stack.pop()
        num2 = numbers.pop()
        num1 = numbers.pop()
        calculator = Calculation(operator)

        if operator == '+':
            numbers.append(calculator.Add(num1, num2))# Add 사용
        elif operator == '-':
            numbers.append(calculator.Sub(num1, num2))# Sub 사용
        elif operator == '*':
            numbers.append(calculator.Mul(num1, num2))# Mul 사용

# 사용 예
#incal = Incalculate()
#result = incal.calculate("2+3*2=")
#print(result)
#8
