import sys

# input = sys.stdin.readline
# result = None

class calculatorIsError:
    def __init__(self):
        self.operators = {'+': 1, '-': 1, '*': 1} # 허용되는 연산자 종류, 성능 향상을 위해 Dictionary 사용
        self.isError = False

    def operatorBeforeNumber(self, beforeInput, inputStr): # 숫자가 없는데 연산자가 입력 될 때
        if inputStr in self.operators and not beforeInput:
            self.isError = True
        return self.isError

    def notOperator(self, beforeInput, inputNum): # 연속으로 숫자가 오거나 연속으로 연산자가 입력 될 때
        if type(beforeInput) == type(inputNum):
            self.isError = True
        return self.isError

    def invalidOperator(self, inputStr): # 허용되지 않은 연산자가 입력될 때
        if not inputStr in self.operators: # Hash Table에서 key를 이용해 원하는 값 찾을 수 있음, O(1)의 시간 소요
            self.isError = True
        return self.isError

# def test():
#     calcError = calculatorIsError()

# if __name__ == "__main__":
#     test()
