from collections import deque



def bfs(start, graph):
    q = deque([start])
    visited = [False for _ in range(N + 1)]
    visited[start] = True
    cnt = 0

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:

            # 가지치기
            if visited[nxt]:
                continue

            visited[nxt] = True
            cnt += 1
            q.append(nxt)

    return cnt


N, M = map(int, input().split())  # 학생수, 비교 횟수

g = [[] for _ in range(N + 1)]
rg = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    rg[b].append(a)

ans = 0
for i in range(1, N + 1):
    taller = bfs(i, g)
    shorter = bfs(i, rg)

    if taller + shorter == N - 1:
        ans += 1

print(ans)


