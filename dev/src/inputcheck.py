from view import InputView, OutputView
from EasterEgg import EasterEgg

class InputCheck:
    def __init__(self):
        self.inputView = InputView()
        self.easterEgg = EasterEgg()
        self.outputView = OutputView()
    
    def input_check(self):
        final_expression = []
        
        while True:
            expression = self.inputView.readLine() # 입력 받아오기
            final_expression.append(expression)

            if self.easterEgg.isCountdownEasterEgg(expression): # 카운트 다운 이스터에그 체크
                easterEggMessage, timer, countdown_step = self.easterEgg.startCountdownEasterEgg()
                self.outputView.countdownPrint(easterEggMessage, timer, countdown_step) # 카운트다운 이스터에그 출력
                return

            elif self.easterEgg.isStudentIdEasterEgg(expression): # 학번 이스터에그 체크
                self.outputView.print(self.easterEgg.startStudentIdEasterEgg(expression)) # 학번 이스터에그 출력
                return

            if expression == "=": # 입력이 '=' 면 반복문 종료
                break
        
        return final_expression