N = int(input())
S = []
for i in range(N):
    abc = [int(x) for x in input().split()]
    S.append(abc)

score = [0] * N
score[0] = (S[0][0], S[0][1], S[0][2])

for i in range(1, N):
    a = S[i][0] + max(score[i-1][1], score[i-1][2])
    b = S[i][1] + max(score[i-1][0], score[i-1][2])
    c = S[i][2] + max(score[i-1][0], score[i-1][1])
    score[i] = (a,b,c)

print(max(score[-1]))