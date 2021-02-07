N = int(input())
H = [int(x) for x in input().split()]

for i in range(1,N):
    if H[i-1] <= H[i]:
        continue
    else:
        H[i] += 1
        if H[i] < H[i-1]:
            print('No')
            quit()

print('Yes')