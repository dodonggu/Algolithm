import sys
from heapq import heappush, heappop

input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')


N = int(input())
arr = []  # 동적 배열

for _ in range(N):
    arr.append(list(map(int, input().split())))

# 1. 시작 시간 순 정렬
arr.sort()

# 2. 우선 순위 큐
pq = []
heappush(pq, arr[0][1])  # 첫 강의의 종료 시간 삽입

# 3. 종료 시간 비교 로직
#
for i in range(1, N):
    # 새 강의의 시작 시간과 이전 강의의 종료 시간 비교
    if arr[i][0] >= pq[0]:
        heappop(pq)  # 이전 강의 종료

    heappush(pq, arr[i][1])  # 새 강의 시작

print(len(pq))