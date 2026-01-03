import sys

input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')


def dfs(day, profit):

    if day == N + 1:
        global best_profit
        best_profit = max(profit, best_profit)
        return

    # 그 날에 일을 하지 않았을 경우
    dfs(day + 1, profit)

    # 그 날에 일을 했을 경우
    if day + arr[day][0] <= N + 1:
        dfs(day + arr[day][0], profit + arr[day][1])


N = int(input())
arr = [[0]] + [list(map(int, input().split())) for _ in range(N)]  # 1-based paddng

best_profit = 0
dfs(1, 0)  # (날짜, 수익) 초기값은 각각 1일과 0원
print(best_profit)
