from collections import deque
from sys import stdin

input = stdin.readline


def printer_queue(priority, location):
  queue = deque([(p, i) for i, p in enumerate(priority)])
  answer = 0

  while queue:
    current = queue.popleft()
    if any(current[0] < q[0] for q in queue):
      queue.append(current)
    else:
      answer += 1
      if current[1] == location:
        return answer


if __name__ == '__main__':
  t = int(input())
  for _ in range(t):
    n, location = map(int, input().split())
    priority = list(map(int, input().strip().split()))
    print(printer_queue(priority, location))
