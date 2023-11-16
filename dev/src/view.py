import time

class InputView:
    def readLine(self):
        expression = input("수식을 입력하세요 (종료하려면 '=' 입력): ")
        return expression

class OutputView:
    def print(self, message):
        print(message)

    def countdownPrint(self, message, timer, countdown_step):
        print(message)
        for count in range(timer, 0, -countdown_step):
            print(f"{count}초 후 프로그램을 종료합니다")
            time.sleep(countdown_step)
        print("종료")