N = int(input())
sp = {}
for i in range(1,N+1):
    s, p = input().split()
    p = int(p)
    if s in sp:
        sp[s].append((p,i))
    else:
        sp[s] = [(p,i)]

sp = sorted(sp.items(), key=lambda x:x[0])

for x in sp:
    s, v = x
    v.sort(key=lambda x:x[0], reverse=True)
    for p,i in v:
        print(i)