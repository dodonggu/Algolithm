def solution(n, computers):
    visited = [False] * n    # 각 노드의 방문 여부를 기록하기 위한 배열
    
    # DFS를 사용해 모든 노드 탐색하며, 방문하지 않은 노드를 새 네트워크로 간주
    count = 0
    for i in range(n):
        if not visited[i]:  # 방문하지 않은 노드에 대해
            dfs(i, visited, computers, n)  # DFS 실행으로 연결된 모든 노드 탐색
            count += 1  # 네트워크 개수 증가
    
    return count

# dfs함수 정의
def dfs(node, visited, computers, n):
    visited[node] = True    # 현재 노드 방문 처리
    for i in range(n):
        # 현재 노드가 아닌 다른 노드 중 연결된 노드가 있고, 방문하지 않은 경우에 재귀 호출
        if node != i and computers[node][i] == 1 and not visited[i]:
            dfs(i, visited, computers, n)
            
    
    