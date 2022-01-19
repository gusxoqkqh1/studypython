#exception_handle.py
# 예외처리!! 가장 중요!

def add(a, b):
    return a + b

def minus(a, b):
    return a-b 

def multi(a, b):
    return a * b

def divide(a, b):
    return a/b


print("사칙연산 시작")

a,b = 4,1
numbers = [3, 6, 9] # 리스트 생성``

try :
    print(f'나누기 결과: {divide(a,b)}')
    res = int(numbers[1]) * 8

except ZeroDivisionError as e:
    print(f"예외 발생!1 {e}")
except IndexError as e:
    print(print(f"예외 발생!2 {e}"))

finally:
    print(f'곱하기 결과: {multi(a,b)}')
    print(f'뺴기 결과: {minus(a,b)}')
    print(f'더하기 결과: {add(a,b)}')



