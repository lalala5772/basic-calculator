import sys
import time

class EasterEgg:
    def __init__(self):
        pass
    def checkEasterEgg(self, expression): 
        #input이 0이라면 프로그램 종료(이스터에그 기능2)
        if expression == "0":
            for i in range(3, 0, -1):
                print(f"{i}초 후 프로그램을 종료합니다")
                time.sleep(1)
            print("프로그램 종료")
            sys.exit()
        #input이 정해진 학번이라면 학생 이름 출력(이스터에그 기능1)    
        else:                   
            students = {
                '201918757': '강성택',
                '201918777': '박종민',
                '201912430': '조민서',
                '201912431': '조승호',
                '201917604': '이관호',
                '201912393': '이미르',
                '202146712': '박용수'
            }
            student_name = students.get(expression)
            if student_name:
                print(student_name)
            else:
                pass    

## result = None # 결과 값을 저장할 변수, 초기에는 아무 값도 없음
# operator = ''  # 현재 선택된 연산자를 저장할 변수, 초기에는 없음
#easterEgg Tester
# easter_egg = EasterEgg() #이스터 에그 확인용 임시코드(나중에 코드 리팩토링 할때 수정부탁)

#init code
# while True:
#     expression = input("수식을 입력하세요 (종료하려면 '=' 입력): ")
#     easter_egg.checkEasterEgg(expression) #이스터 에그 확인용 임시코드(나중에 코드 리팩토링 할때 수정부탁)
#     # 입력이 '=' 면 반복문 종료
#     if expression == "=":
#         break
#     # 연산자 +, -, * 이고, 초기 값이 존재하면 연산자 초기화
#     if expression in ('+', '-', '*'):
#         if result is not None:
#             operator = expression
#     else:
#         num = int(expression)
#         # result  인 경우 result = num
#         if result is None:
#             result = num

#         # result 가 있고, 연산자가 들어오면 해당 연산
#         else:
#             if operator == '+':
#                 result += num
#             elif operator == '-':
#                 result -= num
#             elif operator == '*':
#                 result *= num
# print(f"결과: {result}")
