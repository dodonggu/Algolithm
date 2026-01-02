from collections import deque


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(start, label):
    sy, sx = start
    q = deque([(sy, sx)])
    graph[sy][sx] = label
    cnt = 1

    while q:
        y, x = q.popleft()

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if not (0 <= ny < N and 0 <= nx < N):
                continue

            if graph[ny][nx] != 1:
                continue

            graph[ny][nx] = label
            cnt += 1
            q.append((ny, nx))

    return cnt


N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]

label = 2
sizes = []

for r in range(N):
    for c in range(N):
        if graph[r][c] == 1:
            result = bfs((r, c), label)
            sizes.append(result)
            label += 1

sizes.sort()
print(label - 2)
print(*sizes, sep='\n')

