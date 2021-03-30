from math import factorial

K = int(input())

"""約数を高速に列挙する"""
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
        print(lower_divisors + upper_divisors[::-1])
    return lower_divisors + upper_divisors[::-1]

result = 0
for i in range(1, K+1):
    divs = len(make_divisors(i))
    if i == 1:
        result += 1
    elif i == 2:
        result += 3
    else:
        result += factorial(divs) // factorial(divs - 3)

print(result)