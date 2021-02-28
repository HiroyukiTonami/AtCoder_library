def score(hand):
    s = 0
    for i in range(9):
        s += (i+1) * (10 ** hand[i])
    return s

K = int(input())
S = input()
T = input()

t_hand = [0] * 9
for c in S[:4]:
    t_hand[int(c) - 1] += 1


a_hand = [0] * 9
for c in T[:4]:
    a_hand[int(c) - 1] += 1

win_pattern = 0
for t_hide in range(9):
    for a_hide in range(9):
        t_hand[t_hide] += 1
        a_hand[a_hide] += 1
        t_score = score(t_hand)
        a_score = score(a_hand)
        if t_score > a_score:
            # 勝った。実現可能か見る。
            t_ondeck = K - (S.count(str(t_hide + 1)) + T.count(str(t_hide + 1)))
            a_ondeck = K - (S.count(str(a_hide + 1)) + T.count(str(a_hide + 1)) + int(t_hide == a_hide))

            if t_ondeck > 0 and a_ondeck > 0:
                win_pattern += t_ondeck * a_ondeck
        
        # 後処理
        t_hand[t_hide] -= 1
        a_hand[a_hide] -= 1

all_pattern = ((9 * K) - 8) * ((9 * K) - 9)
print(win_pattern / all_pattern)