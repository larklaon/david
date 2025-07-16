# 파이썬 계산기 프로그램 - 초보자용 상세 주석 버전

# 함수 정의란? 
# def 키워드를 사용해서 재사용 가능한 코드 블록을 만드는 것
# 함수는 입력값(매개변수)을 받아서 처리한 후 결과값을 반환(return)할 수 있음

def add(a, b):
    """
    덧셈 함수
    a와 b는 매개변수(parameter) - 함수가 받는 입력값
    return은 함수의 결과값을 돌려주는 키워드
    """
    return a + b  # a + b의 결과를 함수를 호출한 곳으로 돌려줌

def subtract(a, b):
    """
    뺄셈 함수 (a - b)
    첫 번째 숫자에서 두 번째 숫자를 뺀 결과를 반환
    """
    return a - b  # a에서 b를 뺀 결과를 반환

def multiply(a, b):
    """
    곱셈 함수
    두 숫자를 곱한 결과를 반환
    """
    return a * b  # a와 b를 곱한 결과를 반환

def divide(a, b):
    """
    나눗셈 함수 (a / b)
    0으로 나누면 에러가 발생하므로 미리 체크해야 함
    """
    # if문은 조건을 확인하는 키워드
    # b == 0 이면 (만약 b가 0이라면)
    if b == 0:
        # 에러 메시지 문자열을 반환 (숫자가 아닌 문자열!)
        return "Error: Division by zero."
    
    # b가 0이 아니면 정상적으로 나눗셈 실행
    return a / b

def calculate_expression(expression):
    """
    문자열 수식을 해석하여 계산하는 함수
    예: "2 + 3" 같은 문자열을 받아서 계산 결과를 반환
    """
    # try-except는 에러 처리를 위한 구문
    # try 블록에서 에러가 발생하면 except 블록이 실행됨
    try:
        # 문자열 메서드 설명:
        # .strip() - 앞뒤 공백 제거
        # .split() - 공백을 기준으로 문자열을 리스트로 분할
        parts = expression.strip().split()
        
        # len() 함수는 리스트의 길이(항목 개수)를 반환
        # "2 + 3"을 split()하면 ['2', '+', '3'] 이므로 길이는 3
        if len(parts) != 3:
            return "Error: Invalid input format. Use 'number operator number'"
        
        # 리스트 인덱싱: parts[0]은 첫 번째 항목, parts[1]은 두 번째 항목
        # 중첩된 try-except: 숫자 변환 시 에러 처리
        try:
            # float() 함수는 문자열을 실수로 변환
            # 예: "2" -> 2.0, "3.5" -> 3.5
            num1 = float(parts[0])    # 첫 번째 숫자
            operator = parts[1]       # 연산자 (문자열 그대로)
            num2 = float(parts[2])    # 두 번째 숫자
        except ValueError:
            # ValueError는 변환할 수 없는 값일 때 발생하는 에러
            return "Error: Invalid numbers"
        
        # 연산자에 따라 적절한 함수 호출
        # == 는 같은지 비교하는 연산자
        if operator == '+':
            return add(num1, num2)    # add 함수 호출
        elif operator == '-':
            return subtract(num1, num2)  # subtract 함수 호출
        elif operator == '*':
            return multiply(num1, num2)  # multiply 함수 호출
        elif operator == '/':
            result = divide(num1, num2)  # divide 함수 호출
            return result
        else:
            # 위의 연산자가 아닌 경우
            return "Invalid operator."
            
    except Exception as e:
        # Exception은 모든 에러의 부모 클래스
        # 예상하지 못한 에러가 발생했을 때 처리
        return f"Error: {str(e)}"

def main():
    """
    메인 실행 함수
    프로그램의 주요 로직이 들어있는 함수
    """
    # print() 함수는 화면에 문자열을 출력
    print("=== 계산기 프로그램 ===")
    print("1. 개별 입력 모드")
    print("2. 수식 입력 모드")
    
    # input() 함수는 사용자로부터 문자열을 입력받는 함수
    # .strip()으로 앞뒤 공백 제거
    mode = input("모드를 선택하세요 (1 또는 2): ").strip()
    
    # 문자열 비교: mode 변수의 값이 "1"인지 확인
    if mode == "1":
        # 개별 입력 모드
        try:
            # int() 함수는 문자열을 정수로 변환
            # input()은 항상 문자열을 반환하므로 숫자로 사용하려면 변환 필요
            num1 = int(input("첫 번째 숫자를 입력하세요: "))
            num2 = int(input("두 번째 숫자를 입력하세요: "))
            operator = input("연산자를 입력하세요 (+, -, *, /): ").strip()
            
            # 연산자에 따라 해당 함수 호출
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                result = "Invalid operator."
            
            # isinstance() 함수는 변수의 타입을 확인
            # result가 문자열(str) 타입인지 확인
            if isinstance(result, str):
                print(result)  # 에러 메시지 출력
            else:
                # f-string: f"문자열 {변수}" 형태로 변수를 문자열에 포함
                print(f"Result: {result}")
                
        except ValueError:
            # 숫자가 아닌 값을 입력했을 때 발생하는 에러
            print("Error: Invalid input. Please enter valid numbers.")
            
    elif mode == "2":
        # 수식 입력 모드 (보너스 과제)
        expression = input("Enter expression: ")
        result = calculate_expression(expression)
        
        # 결과가 에러 메시지인지 확인
        # .startswith()는 문자열이 특정 문자로 시작하는지 확인
        if isinstance(result, str) and result.startswith("Error"):
            print(result)
        else:
            print(f"Result: {result}")
    else:
        # 1도 2도 아닌 다른 값을 입력했을 때
        print("Invalid mode selection.")

# __name__은 파이썬의 특별한 내장 변수
# 이 파일을 직접 실행하면 __name__의 값은 "__main__"이 됨
# 다른 파일에서 이 파일을 import하면 __name__의 값은 파일명이 됨
# 즉, 이 조건문은 "이 파일을 직접 실행할 때만 main() 함수를 실행하라"는 의미
if __name__ == "__main__":
    main()  # main() 함수 호출하여 프로그램 시작
