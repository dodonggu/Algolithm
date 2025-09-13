def dfs(month, total):
    global min_result

    # 가지치기
    if total >= min_result:
        return

    # 종료조건
    if month > 12:
        # 최소값 갱신
        min_result = min(total, min_result)
        return

    # 4가지 이용권의 경우
    dfs(month + 1, total + days[month] * cost_day)  # 하루
    dfs(month + 1, total + cost_month)  # 한달
    dfs(month + 3, total + cost_3month)  # 3개월
    dfs(month + 12, total + cost_year)  # 1년


T = int(input())
for tc in range(1, T + 1):
    # 각 이용권 가격
    cost_day, cost_month, cost_3month, cost_year = map(int, input().split())
    # 월별로 이용할 일 수
    days = [0] + list(map(int, input().split()))  # 1월부터 시작
    min_result = float("inf")
    dfs(1, 0)  # 1월부터 시작
    print(f"#{tc} {min_result}")