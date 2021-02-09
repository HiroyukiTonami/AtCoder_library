# PyPyじゃないとTLEする

N = int(input())
A = [int(x) for x in input().split()]

m = 0
for i in range(N):
    x = A[i]
    for j in range(i, N):
        if A[j] < x:
            x = A[j]
        m = max(m, x*(j-i+1))
        if m > x*(j-i+1) + ((N - j - 1) * x):
            break

print(m)