A,B = map(int, input().split())
cost = 0
if B == 1:
    print(cost)
    quit()
B = B - A
cost += 1
if B < 0:
    print(cost)
    quit()
else:
    while B > 0:
        B -= A-1
        cost += 1
print(cost)