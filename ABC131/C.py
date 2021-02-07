from fractions import gcd
A,B,C,D=map(int, input().split())
A -= 1

cc = B//C - A//C
dd = B//D - A//D

E = C*D//gcd(C, D)
ee = B//E - A//E

print(B - A - cc - dd + ee)