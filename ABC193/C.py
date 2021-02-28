import math

N = int(input())
maxi = int(math.sqrt(N)) + 2

was = set()
for i in range(2, maxi):
    if i ** 2 > N:
        break
    for j in range(2, maxi):
        res = i**j
        if res > N:
            break
        if res not in was:
            was.add(res)

print(N-len(was))