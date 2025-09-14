def recur(cur, total, cnt):
    global min_result

    # 가지 치기
    if total >= min_result:
        return

    # 종료 조건
    if cnt == N:
        # 출발점(0)으로 복귀
        total += arr[cur][0]
        min_result = min(total, min_result)
        return

    for nxt in range(1, N):
        if not visited[nxt]:
            visited[nxt] = True
            recur(nxt, total + arr[cur][nxt], cnt + 1)
            visited[nxt] = False


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    visited[0] = True
    min_result = float("inf")
    recur(0, 0, 1)  # 행과 합

    print(f"#{tc} {min_result}")
