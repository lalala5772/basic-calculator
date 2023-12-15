class FactorialException(Exception):
    pass

class DefaultException(Exception):
    pass

class Validator:
    def is_factorial_expression(self, expression):
        NOT_FONUD = -1
        return str(expression).find('!') != NOT_FONUD

    def factorial_validate(self, expression):
        ERROR_MESSAGE_INPUT = '[ERROR] Input Error'
        ERROR_MESSAGE_NEGATIVE = '[ERROR] Out Of Range'
        MAX_ELEMENT_SIZE = 3

        if expression[0] == '-': # 음수 팩토 리얼
            raise FactorialException(ERROR_MESSAGE_NEGATIVE)

        if len(expression) > MAX_ELEMENT_SIZE: # 원소 개수가 4개 이상('=' 포함)인 경우 예외, 두 개 이상의 숫자
            raise FactorialException(ERROR_MESSAGE_INPUT)

        if not expression[0].isdigit() or expression[1] != '!': # 첫번째 원소가 숫자가 아니 거나, 두번째 원소가 팩토리얼이 아닌 경우 예외, 공통 예외
            raise FactorialException(ERROR_MESSAGE_INPUT)

        return True


    def default_validate(self, expression): # 에러 체크 메서드
        ERROR_MESSAGE = "[SYSTEM] ERROR!"

        if not expression[0].isdigit(): # expression이 한 글자이고, 숫자가 아닌 경우, 예시) '='
            raise DefaultException(ERROR_MESSAGE)

        if self.is_invalid_expression(expression): # 표현식의 개수가 홀 수 인 경우, 예시) 1 + =
            raise DefaultException(ERROR_MESSAGE)

        for sequence in range(len(expression) - 1): # 마지막 문자열은 '=' 이므로, 마지막 sequence 제외
            if self.is_number_sequence(sequence):  # sequence가 짝수일때 표현식은 피연산자
                if not expression[sequence].isdigit():
                    raise DefaultException(ERROR_MESSAGE)

            elif self.is_operator_sequence(sequence): # sequence가 홀수일때 표현식은 연산자
                if not expression[sequence] in ('+', '-', '*'):  # 지원하는 연산자가 아닐 경우
                    raise DefaultException(ERROR_MESSAGE)
        return True

    def is_invalid_expression(self, expression):
        return len(expression) % 2 == 1

    def is_number_sequence(self, sequence):
        return sequence % 2 == 0

    def is_operator_sequence(self, sequence):
        return sequence % 2 == 1
