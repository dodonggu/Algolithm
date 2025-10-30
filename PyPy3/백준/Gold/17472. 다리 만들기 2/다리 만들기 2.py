import sys
from collections import deque

input = sys.stdin.readline
# 문제 정의
# 1. 출발점을 어디로 잡을까?

# 방향 쌍 배열 상수 선언
DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


# 섬 라벨링
def bfs_label(y, x, id_, board, lab, N, M):
    q = deque([(y, x)])
    # 초기값 라벨링
    lab[y][x] = id_
    while q:
        cy, cx = q.popleft()
        for dy, dx in DIRS:
            ny, nx = cy + dy, cx + dx
            # 범위 밖이면 스킵
            if not(0 <= ny < N and 0 <= nx < M):
                continue

            # 육지가 아니거나 이미 라벨링이 되었다면 스킵
            if not(board[ny][nx] == 1 and lab[ny][nx] == 0):
                continue

            lab[ny][nx] = id_
            q.append((ny, nx))


def label_islands(board):
    N, M = len(board), len(board[0])
    lab = [[0]*M for _ in range(N)]
    cur_id = 0
    for y in range(N):
        for x in range(M):
            if board[y][x] == 1 and lab[y][x] == 0:
                cur_id += 1
                bfs_label(y, x, cur_id, board, lab, N, M)
    return lab, cur_id


def collect_edges(lab, island_cnt):
    N, M = len(lab), len(lab[0])
    edges = {}

    # 섬 경계 추출
    for y in range(N):
        for x in range(M):
            a = lab[y][x]
            # 바다면 탐색 종료
            if a == 0:
                continue

            # 경계
            for dy, dx in DIRS:
                ny, nx = y + dy, x + dx
                if not (0 <= ny < N and 0 <= nx < M):
                    continue
                if lab[ny][nx] != 0:
                    continue

                # 직선 방향 스캔
                length = 0
                ty, tx = ny, nx
                while 0 <= ty < N and 0 <= tx < M:
                    if lab[ty][tx] == 0:
                        length += 1
                        ty += dy
                        tx += dx
                        continue

                    b = lab[ty][tx]
                    if b != a and length >= 2:
                        u, v = (a, b) if a < b else (b, a)
                        prev = edges.get((u, v))
                        if prev is None or length < prev:
                            edges[(u, v)] = length
                    # 범위 이탈은 실패로 무시
                    break
    return [(w, u, v) for (u, v), w in edges.items()]

class DSU:
    def __init__(self, n):
        self.p = list(range(n + 1))
        self.r = [0] * (n + 1)

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb: return False
        if self.r[ra] < self.r[rb]:
            ra, rb = rb, ra
        self.p[rb] = ra
        if self.r[ra] == self.r[rb]:
            self.r[ra] += 1
        return True

def kruskal(edges, island_cnt):
    # 간선 없거나 섬이 1개면 예외 처리
    if island_cnt <= 1:
        return 0
    edges.sort()  # w, u, v
    dsu = DSU(island_cnt)
    used = 0
    total = 0
    for w, u, v in edges:
        if dsu.union(u, v):
            total += w
            used += 1
            if used == island_cnt - 1:
                return total
    # 모든 섬 연결 못함
    return -1

    # 다리 후보 탐색

# 간선 정리


# 입력받기
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# 섬 라벨링
lab, island_cnt = label_islands(board)
# 섬 경계 추출
edges = collect_edges(lab, island_cnt)
ans = kruskal(edges, island_cnt)
print(ans)
