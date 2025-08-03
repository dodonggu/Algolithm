# 전구 상태 입력받음
bulb_state_list = list(input()[:])
length = len(bulb_state_list)

# 'Y'와 'N'으로 이루어진 요소들 '1'과 '0'으로 변환
# 나중에 상태 전환을 위해서
for i in range(length):
    if bulb_state_list[i] == 'Y':
        bulb_state_list[i] = 1
    elif bulb_state_list[i] == 'N':
        bulb_state_list[i] = 0

count = 0

# 모든 전구 순회
for i in range(length):
    if bulb_state_list[i] == 1:
        # (i+1)의 배수 번쨰 값 상태 전환
        for idx in range(i, length, i+1):
            bulb_state_list[idx] = 1 - bulb_state_list[idx]
        count += 1
print(count)
