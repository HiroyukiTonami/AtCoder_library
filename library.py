# 最大公約数
from fractions import gcd

# 最小公倍数
from fractions import gcd
def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)


# DP
# ナップサック
def knapsack(N,W,weight,value):
    #初期化
    inf=float("inf")
    dp=[[-inf for i in range(W+1)] for j in range(N+1)]
    for i in range(W+1): dp[0][i]=0

    #DP
    for i in range(N):
        for w in range(W+1):
        if weight[i]<=w: #dp[i][w-weight[i]の状態にi番目の荷物が入る可能性がある
            dp[i+1][w]=max(dp[i][w-weight[i]]+value[i], dp[i][w])
        else: #入る可能性はない
            dp[i+1][w]=dp[i][w]
    return dp[N][W]

# 部分和問題
#正の数列の部分わでAになるものはあるか？
def part_sum0(a,A):
    #初期化
    N=len(a)
    dp=[[0 for i in range(A+1)] for j in range(N+1)]
    dp[0][0]=1

    #DP
    for i in range(N):
        for j in range(A+1):
        if a[i]<=j: #i+1番目の数字a[i]を足せるかも
            dp[i+1][j]=dp[i][j-a[i]] or dp[i][j]
        else: #入る可能性はない
            dp[i+1][j]=dp[i][j]
    return dp[N][A]

# Aになるものは何通りあるか？
def part_sum(a,A):
    p=10**9+7
    #初期化
    N=len(a)
    dp=[[0 for i in range(A+1)] for j in range(N+1)]
    dp[0][0]=1

    #DP
    for i in range(N):
        for j in range(A+1):
        if a[i]<=j: #i+1番目の数字a[i]を足せるかも
            dp[i+1][j]=dp[i][j-a[i]]+ dp[i][j]% p
        else: #入る可能性はない
            dp[i+1][j]=dp[i][j]%p
    return dp[N][A]

# LCS
def LCS(S,T):
    #初期化
    dp=[[0 for i in range(len(T)+1)] for j in range(len(S)+1)]

    #DP
    for i in range(len(S)):
        for j in range(len(T)):
        dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
        if S[i]==T[j]:
            dp[i+1][j+1]=max(dp[i+1][j+1],dp[i][j]+1)
    return dp[len(S)][len(T)]