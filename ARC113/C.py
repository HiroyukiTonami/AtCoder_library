S = input()

ans = 0
was = {S[-1]: 1}
for i in range(len(S)-2, -1, -1):
    if S[i] == S[i+1]:
        ans += max(len(S) - i - 2 - (was[S[i]] - 1), 0)
        was = {S[i]: len(S) - i - 1}
    if S[i] in was:
        was[S[i]] += 1
    else:
        was[S[i]] = 1
print(ans)