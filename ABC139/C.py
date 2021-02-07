N = int(input())
H = [int(x) for x in input().split()]
H = H[::-1]

r = 0
now = -1
result = 0
for h in H:
    if now < 0:
        now = h
        continue
    if h >= now:
        r += 1
        now = h
    else:
        now = h
        if r > result:
            result = r
        r = 0
if r > result:
    result = r
print(result)