N = int(input())

xx = []
for i in range(N):
    A, P, X = map(int,input().split())
    if X - A < 1:
        continue
    xx.append(P)

print(-1 if len(xx) == 0 else min(xx))