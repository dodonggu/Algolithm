import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')

# 1. 입력 및 데이터 구조화
N = int(input())
# 1-based index [0] padding
# 구조 분해 할당
T = [0] * (N + 1)
P = [0] * (N + 1)
for i in range(1, N + 1):
    T[i], P[i] = map(int, input().split())

# 해당 날짜에서 얻을 수 있는 최대 수익 저장
# N+1일 경계값까지 넉넉하게 패딩
memo = [-1] * (N + 2)

def dfs(day):
    # 2. 기저 조건 (N+1일은 퇴사일이므로 수익 0)
    if day > N:
        return 0

    # 3. memoization
    if memo[day] != -1:
        return memo[day]

    # 4. 점화식 logic

    # Case A: 오늘 일을 안 함
    res = dfs(day + 1)

    # Case B: 오늘 일을 함 (경계 조건 체크)
    if day + T[day] <= N + 1:
        res = max(res, P[day] + dfs(day + T[day]))

    memo[day] = res
    return res

print(dfs(1))
