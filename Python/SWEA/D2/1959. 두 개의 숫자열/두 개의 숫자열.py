T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M:
        A, B = B, A
        N, M = M, N

    max_v = -float("inf")

    for i in range(M - N + 1):
        total = 0
        for j in range(N):
            total += A[j] * B[i + j]
        max_v = max(total, max_v)

    print(f"#{tc} {max_v}")
