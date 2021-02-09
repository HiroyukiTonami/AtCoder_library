# 再帰上限あげとく
import sys
sys.setrecursionlimit(10**6)
    
# 値入力
mod = 7+10**9
N,M = map(int, input().split())
a = [0]*M
for i in range(M):
    a[i] = int(input())

# メモ化フィボナッチ
# 参考:http://python-remrin.hatenadiary.jp/entry/2017/05/19/153228
fib_memo = {}
def fib(n):
    if n < 3: return 1
    if n not in fib_memo:
        fib_memo[n] = fib(n-1) + fib(n-2)
    return fib_memo[n]

now = 0 # 今いる場所と考える
count = 1
for i in a:
    count *= fib(i-now)
    count = count%mod
    if now == i:
        print(0)
        quit()
    now = i+1 # 穴を超えた次の段に移動する

# 最上段までを計算
count *= fib(N-now+1)
print(count%mod)