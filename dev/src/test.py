import sys
from incalculate import Incalculate
from calculation import Calculation
from easterEgg import EasterEgg
from input import CalculatorInput
from isError import calculatorIsError


if __name__ == "__main__":

  before_input = ''

  while True:

    #입력받기
    user_input = input("숫자 또는 기호를 입력하세요: ")

    #필요한 객체 생성
    calculator_input = CalculatorInput(user_input) #오류 유무 확인
    input_error_message = calculatorIsError() #오류메세지
    #calculator = Calculation() #계산
    #incalculator = Incalculate()
    #easteregg = easterEgg() -> input에서 처리하기로

    input_check = calculator_input.cal_input()

    if input_check != "Equal"  :
      #calculate 실행 및 출력 
      break #종료

    #에러 유무 확인
    if input_check == 'Other' :
      #error 메세지 출력
      #beforeInput은 함수 선언할 때 전달 -> but 어떤 함수가 호출될지는 파일 안에서 판별 , 외부에서 언제 어떻게 전달? 

    else: 
      #그 외에 값은 calculate?? 대체 어디에 넘기라는건지
    
    before_input = user_input

