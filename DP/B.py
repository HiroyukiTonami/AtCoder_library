# pypyなら通るけどPythonは通らない

N, K = map(int,input().split())
hList = [int(x) for x in input().split()]

costs = [0] * N

for i in range(1, N):
    was = [10**9] * (K + 1)
    for j in range(1, K + 1):
        if i - j < 0:
            break
        was[j] = costs[i-j] + abs(hList[i-j] - hList[i])
    costs[i] = min(was)

print(costs[-1])