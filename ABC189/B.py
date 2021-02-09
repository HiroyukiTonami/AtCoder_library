N, X = map(int,input().split())
X = X * 100

for n in range(N):
    V, P = map(int,input().split())
    X -= V*P
    if X < 0:
        print(n+1)
        quit()

print(-1)