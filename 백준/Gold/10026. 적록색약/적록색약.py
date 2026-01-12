import sys
from collections import  deque

# sys.stdin = open('input2.txt', 'r')
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x, visited, is_rg):
    q = deque([(y, x)])
    visited[y][x] = True
    cur_color = grid[y][x]

    while q:
        cy, cx = q.popleft()

        for d in range(4):
            ny, nx = cy + dy[d], cx + dx[d]

            if not (0 <= ny < N and 0 <= nx < N):
                continue

            if visited[ny][nx]:
                continue

            nxt_color = grid[ny][nx]

            if is_rg:
                # 적록색약인 경우: R과 G를 한 묶음으로 취급
                if cur_color in ['R', 'G']:
                    if nxt_color in ['R', 'G']:
                        q.append((ny, nx))  # 3. 튜플로 append
                        visited[ny][nx] = True
                else:
                    # 파란색인 경우
                    if cur_color == nxt_color:
                        q.append((ny, nx))
                        visited[ny][nx] = True
            else:
                # 일반인인 경우: 색이 정확히 같아야 함
                if cur_color == nxt_color:
                    q.append((ny, nx))
                    visited[ny][nx] = True


N = int(input())
grid = [list(input().strip()) for _ in range(N)]
visited_normal = [[False] * N for _ in range(N)]
visited_rg = [[False] * N for _ in range(N)]

normal_cnt = 0
rg_cnt = 0
for y in range(N):
    for x in range(N):
        # 방문하지 않은 노드를 탐색
        if not visited_normal[y][x]:
            bfs(y, x, visited_normal, False)
            normal_cnt += 1

        if not visited_rg[y][x]:
            bfs(y, x, visited_rg, True)
            rg_cnt += 1


print(f'{normal_cnt} {rg_cnt}')
