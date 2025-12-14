def flattening(h):
    inventory = B
    time = 0

    for row in range(N):
        for col in range(M):
            target = arr[row][col]
            diff = target - h

            # 높이가 더 높으면 깎아서 인벤에 넣기
            if diff > 0:
                inventory += diff
                time += 2 * diff

            # 높이가 더 낮으면 인벤에서 꺼내 쌓기
            elif diff < 0:
                need = -diff
                inventory -= need
                time += need

            if best_time is not None and time > best_time:
                return None

    # 불가능
    if inventory < 0:
        return None

    return time, h


N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

min_h = min(map(min, arr))
max_h = max(map(max, arr))

ans = None  # (time, height)

for height in range(min_h, max_h + 1):
    best_time = ans[0] if ans else None
    result = flattening(height)
    if result is None:
        continue

    cur_t, cur_h = result
    if ans is None or cur_t < ans[0] or (cur_t == ans[0] and cur_h > ans[1]):
        ans = (cur_t, cur_h)

print(*ans)