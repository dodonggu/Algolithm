T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    psum = [[0] * (N + 1) for _ in range(N + 1)]

    for r in range(1, N + 1):
        for c in range(1, N + 1):
            psum[r][c] = (
                board[r - 1][c - 1]
                + psum[r - 1][c]
                + psum[r][c - 1]
                - psum[r - 1][c - 1]
            )

    max_total = 0
    for r in range(1, N - M + 2):
        for c in range(1, N - M + 2):
            nr, nc = r + M - 1, c + M - 1
            total = (
                psum[nr][nc] - psum[r - 1][nc] - psum[nr][c - 1] + psum[r - 1][c - 1]
            )
            max_total = max(max_total, total)

    print(f"#{tc} {max_total}")
