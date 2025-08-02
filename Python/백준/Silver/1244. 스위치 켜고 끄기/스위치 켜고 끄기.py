switch_count = int(input())
switch_states = list(map(int, input().split()))

student_count = int(input())

for _ in range(student_count):
    gender, number = map(int, input().split())

    if gender == 1:  # 남학생: 배수 위치 스위치 상태 반전
        for i in range(number - 1, switch_count, number):
            switch_states[i] = 1 - switch_states[i]

    else:  # 여학생: 좌우 대칭 상태 반전
        pos = number - 1
        switch_states[pos] = 1 - switch_states[pos]

        left, right = pos - 1, pos + 1
        while left >= 0 and right < switch_count and switch_states[left] == switch_states[right]:
            switch_states[left] = 1 - switch_states[left]
            switch_states[right] = 1 - switch_states[right]
            left -= 1
            right += 1

# 출력: 20개씩 줄바꿈
for i in range(switch_count):
    print(switch_states[i], end=' ')
    if (i + 1) % 20 == 0:
        print()
