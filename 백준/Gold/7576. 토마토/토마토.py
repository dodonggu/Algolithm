import sys
from collections import deque

# 입력 속도 향상을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    # M: 가로(열), N: 세로(행)
    m, n = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    
    queue = deque()
    
    # 1. 초기 상태에서 익은 토마토(1)의 위치를 모두 큐에 삽입
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append((i, j))
                
    # 상하좌우 이동을 위한 방향 벡터
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 2. BFS 탐색 시작
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 창고 범위 내에 있고, 아직 익지 않은 토마토(0)인 경우
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                # 익은 날짜를 이전 값 + 1로 갱신 (거리를 측정하는 역할)
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                
    # 3. 결과 확인
    max_days = 0
    for row in graph:
        for cell in row:
            if cell == 0:
                # 익지 않은 토마토가 남아있다면 -1 출력
                print(-1)
                return
            max_days = max(max_days, cell)
            
    # 처음에 1부터 시작했으므로 결과값에서 1을 빼줌
    print(max_days - 1)

solve()