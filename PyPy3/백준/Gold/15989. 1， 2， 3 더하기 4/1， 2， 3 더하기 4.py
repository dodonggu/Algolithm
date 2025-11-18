T = int(input())
for tc in range(1, T+1):
    n = int(input())

    dp = [[0] * 4 for _ in range(n + 1)]

    if n >= 1:
        for k in range(1, n + 1):
            dp[k][1] = 1
            dp[k][2] = k // 2 + 1
            if k <= 4:
                dp[k][3] = k

            elif k > 4:
                dp[k][3] = dp[k][2] + dp[k - 3][3]

    print(dp[n][3])