import sys

input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))

# 투 포인터를 위한 변수 초기화
best_i = 0
best_j = N - 1
best_sum = arr[0] + arr[N - 1]

# 포인터 이동
i = 0
j = N - 1
for _ in range(N - 1):  # 배열 모두 순회
    new_sum = arr[i] + arr[j]

    # 새로운 값이 기존 값보다 더 좋을 경우
    if abs(new_sum) < abs(best_sum):
        best_sum = new_sum
        best_i = i
        best_j = j
    # print(f'i = {arr[i]}, j = {arr[j]}, sum = {new_sum}')

    if new_sum == 0:
        best_i = i
        best_j = j
        break
    elif new_sum < 0:
        i += 1
    else:
        j -= 1

print(f'{arr[best_i]} {arr[best_j]}')
