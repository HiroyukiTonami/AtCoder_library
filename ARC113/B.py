A,B,C = map(int,input().split())
A = int(str(A)[-1])
if A == 0:
    print(0)
elif A == 1:
    print(1)
elif A == 2:
    if B % 4 == 0:
        print(6)
    elif B % 4 == 1:
        print(2)
    elif B % 4 == 2:
        print(4)
    elif B % 4 == 3:
        print(8)
elif A == 3:
    if B % 4 == 0:
        print(1)
    elif B % 4 == 1:
        print(3)
    elif B % 4 == 2:
        print(9)
    elif B % 4 == 3:
        print(7)
elif A == 4:
    print(6) if B % 2 == 0 else print(4)
elif A == 5:
    print(5)
elif A == 6:
    print(6)
elif A == 7:
    if B % 4 == 0:
        print(1)
    elif B % 4 == 1:
        print(7)
    elif B % 4 == 2:
        print(9)
    elif B % 4 == 3:
        print(3)
elif A == 8:
    if B % 4 == 0:
        print(6)
    elif B % 4 == 1:
        print(8)
    elif B % 4 == 2:
        print(4)
    elif B % 4 == 3:
        print(2)
elif A == 9:
    print(1) if B % 2 == 0 else print(9)
