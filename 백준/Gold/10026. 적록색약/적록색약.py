import sys
from collections import deque

# 로컬 테스트용 (제출 시에는 주석 처리하거나 삭제하세요)
# sys.stdin = open('input2.txt', 'r')
input = sys.stdin.readline

# 상하좌우 이동을 위한 벡터
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x, visited, is_rg):
    q = deque([(y, x)])
    visited[y][x] = True
    current_color = grid[y][x]
    
    while q:
        cy, cx = q.popleft()
        
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                target_color = grid[ny][nx]
                
                if not is_rg:
                    # 일반인: 색상이 정확히 일치해야 함
                    if target_color == current_color:
                        visited[ny][nx] = True
                        q.append((ny, nx))
                else:
                    # 적록색약: R과 G를 같은 것으로 취급
                    if current_color == 'R' or current_color == 'G':
                        if target_color == 'R' or target_color == 'G':
                            visited[ny][nx] = True
                            q.append((ny, nx))
                    else:
                        # 파란색은 일반인과 동일하게 처리
                        if target_color == current_color:
                            visited[ny][nx] = True
                            q.append((ny, nx))

N = int(input())
grid = [list(input().strip()) for _ in range(N)]

# 방문 여부를 체크할 배열을 각각 생성
visited_normal = [[False] * N for _ in range(N)]
visited_rg = [[False] * N for _ in range(N)]

normal_count = 0
rg_count = 0

for y in range(N):
    for x in range(N):
        # 일반인 기준 구역 탐색
        if not visited_normal[y][x]:
            bfs(y, x, visited_normal, False)
            normal_count += 1
            
        # 적록색약 기준 구역 탐색
        if not visited_rg[y][x]:
            bfs(y, x, visited_rg, True)
            rg_count += 1

print(f'{normal_count} {rg_count}')