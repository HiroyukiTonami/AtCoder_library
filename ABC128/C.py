import itertools
N,M = map(int,input().split())
ks = []
for _ in range(M):
    ks.append(input().split())

pList = list(input().split())
result = 0
was = []
cases = list(itertools.product(['1','0'], repeat=N))
for case in cases:
    light = 0
    for p,x in zip(pList,ks):
        k = x[0]
        s = x[1:]
        oncount = 0
        for c in s:
            if case[int(c)-1] == '1':
                oncount += 1
        if oncount%2 == int(p):
            light += 1
    if light == M:
        result += 1
print(result)