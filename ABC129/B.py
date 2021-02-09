N = int(input())
W = [int(x) for x in input().split()]

result = 10**6
for i in range(N):
    x = abs(sum(W[0:i]) - sum(W[i:]))
    if x < result:
        result = x
print(result)