# 전구 리스트 입력 받음
bulb_lst = list(input().upper()[:])
# print(bulb_lst)

# 1과 0으로 상태 값 변환(나중에 상태 전환을 위해서)
''' 잘못된 코드 예시
for bulb in bulb_lst:
    if bulb == 'Y':
        bulb = 1
    elif bulb == 'N':
        bulb = 0
'''        
for i in range(len(bulb_lst)):
    if bulb_lst[i] == 'Y':
        bulb_lst[i] = 1
    elif bulb_lst[i] == 'N':
        bulb_lst[i] = 0

# print(bulb_lst)

length = len(bulb_lst)
count = 0

# 모든 스위치 순회
for i in range(1, length + 1):
    # i번째 스위치가 켜져있다면
    # index는 i-1
    if bulb_lst[i - 1] == 1:
        # i의 배수 번쨰 스위치 모두 상태 반전
        for idx in range(i-1, length, i):
            bulb_lst[idx] = 1 - bulb_lst[idx]
        # print(bulb_lst)
        count += 1

print(count)