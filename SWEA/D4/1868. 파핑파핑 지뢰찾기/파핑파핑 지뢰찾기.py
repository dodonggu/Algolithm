# import sys
from collections import deque

# sys.stdin = open('input.txt', 'r')

# 8방향 벡터
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

T = int(input())
for t_c in range(1, T + 1):
    N = int(input())
    raw_data = [list(input().strip()) for _ in range(N)]

    # 1. 주변 지뢰 개수를 담을 board 만들기
    board = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if raw_data[y][x] == '.':
                mine_count = 0
                for d in range(8):
                    ny, nx = y + dy[d], x + dx[d]
                    if 0 <= ny < N and 0 <= nx < N:
                        if raw_data[ny][nx] == '*':
                            mine_count += 1
                board[y][x] = mine_count
            else:
                board[y][x] = -1  # 지뢰인 칸은 -1로 표시

    visited = [[False] * N for _ in range(N)]
    cnt = 0

    # 2. 주변 지뢰가 0개인 칸부터 클릭해서 BFS 연쇄 반응
    for y in range(N):
        for x in range(N):
            if board[y][x] == 0 and not visited[y][x]:
                cnt += 1
                # BFS 시작
                queue = deque([(y, x)])
                visited[y][x] = True

                while queue:
                    cy, cx = queue.popleft()

                    # 현재 칸이 0일 때만 인접 8방향으로 전파
                    if board[cy][cx] == 0:
                        for d in range(8):
                            ny, nx = cy + dy[d], cx + dx[d]
                            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                                if board[ny][nx] != -1:  # 지뢰가 아니면 무조건 방문
                                    visited[ny][nx] = True
                                    # 인접한 칸이 0이라면 그 칸에서도 또 전파되어야 하므로 큐에 추가
                                    if board[ny][nx] == 0:
                                        queue.append((ny, nx))

    # 3. 0인 칸에 의해 터지지 않은 나머지 '.' 칸들 클릭
    for y in range(N):
        for x in range(N):
            if board[y][x] != -1 and not visited[y][x]:
                cnt += 1

    print(f'#{t_c} {cnt}')