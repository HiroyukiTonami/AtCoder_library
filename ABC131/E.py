import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N, K = map(int, input().split())
if N > 2:
    x = combinations_count(N-1, 2)
else:
    x = 0
if x < K:
    print('-1')
    quit()
