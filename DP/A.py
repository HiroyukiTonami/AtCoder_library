N = int(input())
hList = [int(x) for x in input().split()]

costs = [0] * N
costs[1] = abs(hList[0] - hList[1])

for i in range(2, N):
    a = costs[i-1] + abs(hList[i-1] - hList[i])
    b = costs[i-2] + abs(hList[i-2] - hList[i])
    costs[i] = min(a, b)

print(costs[-1])