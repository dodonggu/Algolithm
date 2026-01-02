import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))
# arr.sort() 오름차순 보장

# 투 포인터를 위한 변수 초기화
i, j = 0, N - 1
best_i, best_j = i, j
best_val = arr[i] + arr[j]

# 교차 전까지 반복
while i < j:
    cur_val = arr[i] + arr[j]

    # 새로운 값이 기존 값보다 더 좋을 경우
    if abs(cur_val) < abs(best_val):
        best_val = cur_val
        best_i, best_j = i, j

    if cur_val == 0:
        break
    elif cur_val < 0:
        i += 1
    else:
        j -= 1

print(arr[best_i], arr[best_j])
