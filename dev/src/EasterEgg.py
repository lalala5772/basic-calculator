class EasterEgg:
    def __init__(self):
        self.EASTER_EGG = "[EVENT] "
        self.COUNTDOWN_EASTER_EGG_EXPRESSION = '0' # 카운트 다운 이스터에그 표현식, 입력이 '0' 인 경우 "이스터에그"
        self.STUDENT_ID_EASTER_EGG_EXPRESSIONS = { # 학번 이스터에그 표현식, 입력이 아래 학번 중 하나 인 경우 "이스터에그"
            '201918757': '강성택',
            '201918777': '박종민',
            '201912430': '조민서',
            '201912431': '조승호',
            '201917604': '이관호',
            '201912393': '이미르',
            '202146712': '박용수'
        }
        self.SCHOOL_ANNIVERSARY = '1015'

    def start_countdown_easter_egg(self):
        EXIT_TIMER = 3  # 프로그램 종료까지의 시간
        COUNTDOWN_STEP = 1  # 카운트다운
        return self.EASTER_EGG, EXIT_TIMER, COUNTDOWN_STEP

    def start_student_id_easter_egg(self, expression):
        return self.EASTER_EGG + "{}은 ".format(expression) + self.STUDENT_ID_EASTER_EGG_EXPRESSIONS.get(expression) + "의 학번 입니다."

    def start_school_anniversary(self):
        return self.EASTER_EGG + "전북대 개교기념일입니다."

    def is_countdown_easter_egg(self, expression):
        if expression == self.COUNTDOWN_EASTER_EGG_EXPRESSION:
            return True
        return False

    def is_student_id_easter_egg(self, expression):
        if self.STUDENT_ID_EASTER_EGG_EXPRESSIONS.get(expression):
            return True
        return False

    def is_school_anniversary(self, expression):
        if expression == self.SCHOOL_ANNIVERSARY:
            return True
        return False
