result = None # 결과 값을 저장할 변수, 초기에는 아무 값도 없음
operator = ''  # 현재 선택된 연산자를 저장할 변수, 초기에는 없음

while True:
    expression = input("수식을 입력하세요 (종료하려면 '=' 입력): ")

    # 입력이 '=' 면 반복문 종료
    if expression == "=":
        break

    # 연산자 +, -, * 이고, 초기 값이 존재하면 연산자 초기화
    if expression in ('+', '-', '*'):
        if result is not None:
            operator = expression
    else:
        num = int(expression)

        # result  인 경우 result = num
        if result is None:
            result = num

        # result 가 있고, 연산자가 들어오면 해당 연산
        else:
            if operator == '+':
                result += num
            elif operator == '-':
                result -= num
            elif operator == '*':
                result *= num

print(f"결과: {result}")