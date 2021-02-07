V,T,S,D=map(int, input().split())

if D < V*T:
    print('Yes')
elif D <= V*S:
    print('No')
else:
    print('Yes')