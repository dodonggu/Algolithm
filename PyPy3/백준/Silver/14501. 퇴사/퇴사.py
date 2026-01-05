import sys

# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 1. 상태 정의 및 전처리
N = int(input())
# 날짜 계산 실수 방지를 위한 padding
# 1-based index
T = [0] * (N + 1) # 상담에 걸리는 시간
P = [0] * (N + 1) # 상담 했을 때 얻는 수익
for i in range(1, N + 1):
    T[i], P[i] = map(int, input().split())

dp = [-1] * (N + 2)

# 2. 핵심 로직
def dfs(day):
    # 3. 종료 조건
    if day > N:
        return 0

    # 4. memoization
    # 이미 최대 수익을 기록했다면 return
    if dp[day] != -1:
        return dp[day]

    # 4. 점화식
    # Case A: 상담을 하지 않았을 경우
    res = dfs(day + 1)

    # Case B: 상담을 했을 경우
    if day + T[day] <= N + 1:
        # (오늘 수익 + 상담 종료일 이후의 수익) vs Case A의 수익
        res = max(res, P[day] + dfs(day + T[day]))

    dp[day] = res
    return res

# 결과 출력
print(dfs(1))

