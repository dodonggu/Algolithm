from collections import deque


dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]


# 땅으로 표현된 모든 칸에 대해서, 어떤 물인 칸으로 이동하기 위한 모든 최소 이동횟수들의 합
def bfs(grid):
    dist = [[-1] * M for _ in range(N)]
    q = deque()

    for i in range(N):
        for j in range(M):
            if grid[i][j] == "W":
                dist[i][j] = 0
                q.append((i, j))

    while q:
        ti, tj = q.popleft()
        for di, dj in dirs:
            wi, wj = ti + di, tj + dj
            if 0 <= wi < N and 0 <= wj < M and dist[wi][wj] == -1:
                dist[wi][wj] = dist[ti][tj] + 1
                q.append((wi, wj))

    res = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == "L":
                res += dist[i][j]
    return res


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 행의 개수, 열의 개수
    lst = [list(input()) for _ in range(N)]
    ans = bfs(lst)
    print(f"#{tc} {ans}")
