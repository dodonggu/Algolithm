from collections import deque


# 나이트의 이동 가능한 8방향 벡터
dy = [-1, -2, -2, -1, 1, 2, 2, 1]
dx = [2, 1, -1, -2, -2, -1, 1, 2]


def bfs(start, target, N):  # (시작 위치, 목표 위치, 크기)
    dist = [[-1] * N for _ in range(N)]
    sy, sx = start
    q = deque()
    q.append((sy, sx))
    dist[sy][sx] = 0

    while q:
        y, x = q.popleft()

        # 조건 만족
        if (y, x) == target:
            return dist[y][x]

        for d in range(8):  # 8방향 탐색
            ny = y + dy[d]
            nx = x + dx[d]

            # 범위 체크
            if not (0 <= ny < N and 0 <= nx < N):
                continue

            # 방문 체크
            if dist[ny][nx] != -1:
                continue

            dist[ny][nx] = dist[y][x] + 1
            q.append((ny, nx))

    return -1


T = int(input())
for _ in range(T):
    N = int(input())
    start = tuple(map(int, input().split()))
    target = tuple(map(int, input().split()))
    ans = bfs(start, target, N)  # (시작 위치, 목표 위치, 크기)
    print(ans)
