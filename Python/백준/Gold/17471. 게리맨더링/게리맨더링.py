from itertools import combinations
from collections import deque


def connected(group):
    start = next(iter(group))
    q = deque([start])
    visited = {start}
    while q:
        cur = q.popleft()
        for nxt in neighbors[cur]:
            # 가지치기
            # 그룹의 요소가 아니거나 방문했다면 스킵 
            if nxt not in group or nxt in visited:
                continue
            visited.add(nxt)
            q.append(nxt)
    return len(visited) == len(group)


N = int(input())  # 구역의 개수
values = [0] + list(map(int, input().split()))  # 1-based padding

# 그래프 형태로 안접리스트 구성
neighbors = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    data = list(map(int, input().split()))
    cnt = data[0]
    for j in range(1, cnt + 1):
        neighbors[i].append(data[j])

ALL = set(range(1, N + 1))
INF = 10**18
ans = INF

# 조합을 이용해 모든 분할(A, B)을 전수 조사
for k in range(1, N//2 + 1):  # 대칭 제거
    for comb in combinations(range(1, N + 1), k):
        A = set(comb)
        B = ALL - A

        # 분할된 각각 그룹들이 내부 간선으로 연결되어 있는지 확인
        if not connected(A):
            continue
        if not connected(B):
            continue

        diff = abs(sum(values[i] for i in A) - sum(values[i] for i in B))
        if diff < ans:
            ans = diff

print(-1 if ans == INF else ans)