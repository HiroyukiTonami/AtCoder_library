N, K = map(int,input().split())
aList = [int(x) for x in input().split()]

base = K // N
bonus = K % N

sorted_a = sorted(aList)
th = sorted_a[bonus - 1] if bonus > 0 else -1

for a in aList:
    if a <= th:
        print(base + 1)
    else:
        print(base)