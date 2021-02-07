# 標準入力から受け取るところのメモ

# 固定個の整数
H,W = map(int,input().split())

# いくつかの整数
aList = [int(x) for x in input().split()]

# いくつかの整数、縦長
A = [0]*N
for i in range(N):
    A[i] = int(input())

# 2次元配列
H,W = map(int,input().split())
S = []
for i in range(H):
    S.append([x for x in input().split()])