class Validator:
    def validate(self, expression): # 에러 체크 메서드
        if not expression[0].isdigit(): # expression이 한 글자이고, 숫자가 아닌 경우, 예시) '='
            raise Exception('[ERROR]')

        if self.isInvalidExpression(expression): # 표현식의 개수가 홀 수 인 경우, 예시) 1 + =
            raise Exception('[ERROR]')

        for sequence in range(len(expression) - 1): # 마지막 문자열은 '=' 이므로, 마지막 sequence 제외
            if self.isNumberSequence(sequence):  # sequence가 짝수일때 표현식은 피연산자
                if not expression[sequence].isdigit():
                    raise Exception('[ERROR]')

            elif self.isOperatorSequence(sequence): # sequence가 홀수일때 표현식은 연산자
                if not expression[sequence] in ('+', '-', '*'):  # 지원하는 연산자가 아닐 경우
                    raise Exception('[ERROR]')

    def isInvalidExpression(self, expression):
        return len(expression) % 2 == 1

    def isNumberSequence(self, sequence):
        return sequence % 2 == 0

    def isOperatorSequence(self, sequence):
        return sequence % 2 == 1
