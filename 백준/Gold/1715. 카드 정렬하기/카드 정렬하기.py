import sys
from heapq import heappush, heappop

input = sys.stdin.readline
# sys.stdin = open('input3.txt', 'r')

# 1. 상태정의 및 전처리
N = int(input())
lst = [int(input()) for _ in range(N)]

lst.sort()

ans = 0
# 2.
if N == 1:
    ans = 0

elif N == 2:
    ans = sum(lst)

else:
    for _ in range(N - 1):
        a = heappop(lst)
        b = heappop(lst)
        new_num = a + b
        ans += new_num
        heappush(lst, new_num)
print(ans)