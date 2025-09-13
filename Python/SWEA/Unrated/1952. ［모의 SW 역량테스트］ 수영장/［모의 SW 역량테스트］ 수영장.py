T = int(input())
for tc in range(1, T + 1):
    # 이용권 가격들
    cost_day, cost_month, cost_month3, cost_year = map(int, input().split())
    # 월별 이용 계획 일수
    days = [0] + list(map(int, input().split()))

    # 합을 기록해나갈 dp 리스트
    dp = [0] * 13

    dp[1] = min(days[1] * cost_day, cost_month)
    dp[2] = dp[1] + min(days[2] * cost_day, cost_month)

    for month in range(3, 13):
        dp[month] = min(
            dp[month - 1] + days[month] * cost_day,
            dp[month - 1] + cost_month,
            dp[month - 3] + cost_month3,
        )

    answer = min(dp[12], cost_year)

    print(f"#{tc} {answer}")
