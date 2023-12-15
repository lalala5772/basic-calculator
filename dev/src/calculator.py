class Calculator:

    def factorial_calculate(self, expression):
        result = 1
        for number in range(1, int(expression[0]) + 1):
            result *= number

        return result


    def calculate(self, expression):
        result = None
        operator = None

        for sequence in range(len(expression) - 1): # '=' 이 아닐때 까지 계산
            if expression[sequence].isdigit():
                number = int(expression[sequence])

                if result == None:
                    result = number
                else:
                    if operator == '+':
                        result = self.add(result, number)

                    elif operator == '-':
                        result = self.sub(result, number)

                    elif operator == '*':
                        result = self.multi(result, number)
            else:
                operator = expression[sequence]

        return result

    def add(self, result, number):
        return result + number

    def sub(self, result, number):
        return result - number

    def multi(self, result, number):
        return result * number
