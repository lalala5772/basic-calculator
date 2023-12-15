import time

class InputView:
    def read_date(self):
        expression = input("수식을 입력하세요 (종료하려면 '=' 입력): ")
        return expression

class OutputView:
    def print_calulation_result(self, message):
        print(message)

    def print_easter_egg(self, message):
        print(message)

    def print_count_down_easter_egg(self, message, timer, countdown_step):
        print(message)
        for count in range(timer, 0, -countdown_step):
            print(f"{count}초 후 프로그램을 종료합니다")
            time.sleep(countdown_step)
        print("종료")

    def print_error_message(self, message):
        print(message)
