import sys

input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

while True:
    M, N = map(int, input().split())
    if M == 0 and N == 0:
        break

    edges = []
    total_cost = 0

    for _ in range(N):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
        total_cost += w

    # 1. 가중치(w) 기준 오름차순 정렬
    edges.sort()

    # 2. 부모 테이블 초기화 (자기 자신을 부모로)
    parent = [i for i in range(M)]

    mst_cost = 0
    edges_count = 0

    # 3. 간선을 하나씩 확인하며 사이클이 생기지 않으면 연결
    for w, u, v in edges:
        # 두 정점의 루트가 다르면 (사이클이 생기지 않으면)
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst_cost += w
            edges_count += 1
            # MST 간선의 수는 항상 (정점 개수 - 1)개 입니다.
            if edges_count == M - 1:
                break

    # 전체 비용에서 MST 비용을 뺀 '절약 액수' 출력
    print(total_cost - mst_cost)
