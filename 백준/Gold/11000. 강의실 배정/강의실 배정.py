import heapq
import sys

def solve():
    # 빠른 입력을 위해 sys.stdin.readline 사용
    n = int(sys.stdin.readline())
    lectures = []
    
    for _ in range(n):
        lectures.append(list(map(int, sys.stdin.readline().split())))

    # 1. 시작 시간 기준으로 정렬
    lectures.sort()

    # 2. 우선순위 큐 생성 (첫 강의의 종료 시간을 먼저 삽입)
    room = []
    heapq.heappush(room, lectures[0][1])

    # 3. 두 번째 강의부터 확인
    for i in range(1, n):
        # 현재 가장 빨리 끝나는 강의실의 종료 시간과 다음 강의 시작 시간 비교
        if lectures[i][0] >= room[0]:
            heapq.heappop(room)  # 강의실을 이어서 사용할 수 있으므로 기존 종료 시간 제거
        
        # 새로운(혹은 갱신된) 종료 시간 삽입
        heapq.heappush(room, lectures[i][1])

    # 4. 큐에 남아있는 원소의 개수가 필요한 강의실 수
    print(len(room))

solve()