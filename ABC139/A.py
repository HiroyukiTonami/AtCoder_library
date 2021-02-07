S = input()
T = input()

r = 0
for i,j in zip(S,T):
    if i==j:
        r += 1

print(r)