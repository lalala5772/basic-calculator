from view import InputView, OutputView
from EasterEgg import EasterEgg

class InputCheck:
    def __init__(self):
        self.inputView = InputView()
        self.easterEgg = EasterEgg()
        self.outputView = OutputView()
    
    def check(self):
        final_expression = []
        
        while True:
            expression = self.inputView.read_date() # 입력 받아오기
            final_expression.append(expression)

            if self.easterEgg.is_countdown_easter_egg(expression): # 카운트 다운 이스터에그 체크
                easterEggMessage, timer, countdown_step = self.easterEgg.start_countdown_easter_egg()
                self.outputView.print_count_down_easter_egg(easterEggMessage, timer, countdown_step) # 카운트다운 이스터에그 출력
                return

            if self.easterEgg.is_student_id_easter_egg(expression): # 학번 이스터에그 체크
                self.outputView.print_easter_egg(self.easterEgg.start_student_id_easter_egg(expression)) # 학번 이스터에그 출력
                return

            if self.easterEgg.is_school_anniversary(expression): # 개교 기념일 체크
                self.outputView.print_easter_egg(self.easterEgg.start_school_anniversary()) # 개교 기념일 이스터에그 출력
                return

            if self.is_equal_sign(expression): # 입력이 '=' 면 반복문 종료
                break
        
        return final_expression

    def is_equal_sign(self, expression):
        return expression == '='
