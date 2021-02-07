S = input()

move = 10**100
RL = []
maxlen = 0
l = 0
SS = 'R'
Smember = []
rr = 0
ll = 1
mem = 0
nowR = True
for i,c in enumerate(S):
    if nowR and c=='L':
        nowR = False
    elif not nowR and c=='R':
        # calc
        a = 0
        b = 0
        for i in range(max(rr,ll)):
            if i % 2 == 0:
                a += int(rr>0)
                b += int(ll>0)
            else:
                a += int(ll>0)
                b += int(rr>0)
            rr -= 1
            ll -= 1
        Smember.append(a)
        Smember.append(b)
        rr = 1
        ll = 1
        nowR = True
    else:
        if c == 'R':
            rr += 1
        else:
            ll += 1

a = 0
b = 0
for i in range(max(rr,ll)+1):
    if i % 2 == 0:
        a += int(rr>0)
        b += int(ll>0)
    else:
        a += int(ll>0)
        b += int(rr>0)
    rr -= 1
    ll -= 1
Smember.append(a)
Smember.append(b)

i = 0
flg = False
for a,b in zip(S,S[1:]):
    if a == 'R' and b == 'L':
        print(Smember[i], end=' ')
        flg = True
        i += 1
    elif flg:
        print(Smember[i], end=' ')
        flg = False
        i += 1
    else:
        print(0, end=' ')
if flg:
    print(Smember[-1])
else:
    print(0)