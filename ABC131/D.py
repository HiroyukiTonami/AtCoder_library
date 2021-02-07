
N = int(input())

AB = [0]*N
for i in range(N):
    AB[i] = list(map(int, input().split()))

AB.sort(key=lambda x:x[1])
time = 0
for a,b in AB:
    time += a
    if time > b:
        print('No')
        quit()
print('Yes')