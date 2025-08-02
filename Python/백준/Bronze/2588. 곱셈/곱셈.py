a = int(input())
b = input()  # 문자열로 입력 받기

# 일의 자리, 십의 자리, 백의 자리 숫자 추출 (문자 → 정수 변환)
one = int(b[-1])
ten = int(b[-2])
hundred = int(b[-3])

print(a * one)
print(a * ten)
print(a * hundred)
print(a * int(b))