# minmax_calculator.py

def find_min_max(numbers):
    
    # 만약 리스트가 비어있으면 None을 반환 (안전장치)
    if not numbers:  # numbers가 빈 리스트 []인 경우
        return None, None
    
    # 첫 번째 숫자를 최소값과 최대값의 초기값으로 설정
    # 왜냐하면 비교할 기준이 필요하기 때문
    minimum = numbers[0]  # 리스트의 첫 번째 원소를 최소값으로 가정
    maximum = numbers[0]  # 리스트의 첫 번째 원소를 최대값으로 가정
    
    # for 반복문: 리스트의 모든 숫자를 하나씩 확인
    for num in numbers:  # numbers 리스트의 각 숫자를 num 변수에 저장하며 반복
        
        # 현재 숫자(num)가 지금까지의 최소값보다 작으면
        if num < minimum:
            minimum = num  # 최소값을 현재 숫자로 업데이트
        
        # 현재 숫자(num)가 지금까지의 최대값보다 크면
        if num > maximum:
            maximum = num  # 최대값을 현재 숫자로 업데이트
    
    # 찾은 최소값과 최대값을 반환 (튜플 형태로 반환)
    return minimum, maximum

def main():
    """
    메인 함수: 프로그램의 핵심 로직이 실행되는 곳
    """
    
    # try-except 블록: 오류가 발생할 수 있는 코드를 안전하게 실행
    try:
        # 사용자로부터 입력받기
        # input() 함수: 사용자가 키보드로 입력한 내용을 문자열로 받음
        user_input = input("숫자들을 공백으로 구분하여 입력하세요: ")
        
        # 입력받은 문자열을 공백을 기준으로 분리
        # 예: "3 9 1 4 2" → ["3", "9", "1", "4", "2"]
        input_strings = user_input.split()
        
        # 빈 리스트 생성: 변환된 숫자들을 저장할 공간
        numbers = []
        
        # 각 문자열을 숫자(float)로 변환
        for s in input_strings:  # input_strings 리스트의 각 문자열을 s 변수에 저장하며 반복
            # float() 함수: 문자열을 소수점 숫자로 변환
            # 예: "3" → 3.0, "9" → 9.0
            converted_number = float(s)
            # 변환된 숫자를 numbers 리스트에 추가
            numbers.append(converted_number)
        
        # 위에서 만든 find_min_max 함수 호출
        # 함수가 반환하는 두 값을 minimum, maximum 변수에 저장
        minimum, maximum = find_min_max(numbers)
        
        # 결과를 화면에 출력
        # f-string: 변수 값을 문자열에 삽입하는 방법
        print(f"Min: {minimum}, Max: {maximum}")
        
    # ValueError 예외처리: float() 변환 중 오류가 발생한 경우
    # 예: "abc"를 숫자로 변환하려고 할 때
    except ValueError:
        print("Invalid input.")  # 잘못된 입력이라는 메시지 출력
    
    # 그 외 모든 예외처리: 예상치 못한 오류가 발생한 경우
    except Exception as e:
        print("Invalid input.")  # 일관된 오류 메시지 출력

if __name__ == "__main__":
    main()  # 메인 함수 실행
