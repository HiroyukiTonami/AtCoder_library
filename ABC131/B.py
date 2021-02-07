N,L = map(int, input().split())

s = 0
ringo = [0]*N
for i in range(N):
    ringo[i] = L+i

ringo.sort(key= lambda x:abs(x))
ringo[0] = 0
print(sum(ringo))