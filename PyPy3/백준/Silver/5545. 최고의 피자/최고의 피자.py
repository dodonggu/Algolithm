N = int(input())
A, B = map(int, input().split())
C = int(input())
D = [int(input()) for _ in range(N)]

D.sort(reverse=True)

cal = C
price = A
max_v = C // A

for d in D:
    cal += d
    price += B

    new_v = cal // price

    if new_v >= max_v:
        max_v = new_v
    else:
        break

print(max_v)

