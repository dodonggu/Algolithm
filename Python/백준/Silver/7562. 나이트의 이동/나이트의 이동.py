from collections import deque

# 나이트가 이동가능한 경우의 수 8가지 매핑
dy = [1, 2, 2, 1, -1, -2, -2, -1]
dx = [2, 1, -1, -2, -2, -1, 1, 2]


def bfs(start, end, l):
    if start == end:
        return 0

    dist = [[-1] * l for _ in range(l)]
    sy, sx = start
    ey, ex = end

    q = deque()
    q.append((sy, sx))
    dist[sy][sx] = 0

    while q:
        y, x = q.popleft()

        for d in range(8):
            ny = y + dy[d]
            nx = x + dx[d]

            if not (0 <= ny < l and 0 <= nx < l):
                continue
            if dist[ny][nx] != -1:
                continue

            dist[ny][nx] = dist[y][x] + 1

            if (ny, nx) == (ey, ex):
                return dist[ny][nx]

            q.append((ny, nx))

    return -1


T = int(input())
for _ in range(T):
    l = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    ans = bfs(start, end, l)

    print(ans)
