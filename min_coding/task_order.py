import sys
from collections import deque


sys.stdin = open('task_order.txt', 'r')


def topo_sort():
    topo_order = []
    q = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        cur = q.popleft()
        topo_order.append(cur)
        for nxt in graph[cur]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

    # 사이클이 있으면 어떤 경우든 답은 -1
    if len(topo_order) != N:
        print(f'#{tc} -1')
        return

    return topo_order


def dp_solve(topo_order):
    ans = float('inf')

    for i in range(1, N + 1):
        modified = worktime[:]
        modified[i] //= 2

        # dp[u] : u번 업무를 끝마칠 때까지 걸리는 최소 시간
        dp = [0] * (N + 1)

        for u in topo_order:
            if not pre[u]:
                dp[u] = modified[u]
            else:
                max_pre = 0
                for p in pre[u]:
                    if dp[p] > max_pre:
                        max_pre = dp[p]
                dp[u] = max_pre + modified[u]

        total_time = max(dp[1:])  # 가장 오래 걸리는 시간
        if total_time < ans:
            ans = total_time

    print(f'#{tc} {ans}')


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 완료해야 하는 작업의 수 == 노드의 수

    # pre[i] : i번 업무의 선행 작업 리스트
    pre = [[] for _ in range(N + 1)]
    worktime = [0] * (N + 1)

    for i in range(1, N + 1):
        data = list(map(int, input().split()))
        worktime[i] = data[0]
        M = data[1]  # 선행 업무 개수
        for k in range(M):
            prenum = data[2 + k]
            pre[i].append(prenum)

    # 진입 차수
    indegree = [0] * (N + 1)
    # 각 노드에 연결된 정보를 담기 위한 인접 리스트
    graph = [[] for _ in range(N + 1)]

    for i in range(1, N + 1):
        for p in pre[i]:
            graph[p].append(i)
            indegree[i] += 1

    result = topo_sort()
    if result is None:  # 사이클 발생 시
        continue
    dp_solve(result)
