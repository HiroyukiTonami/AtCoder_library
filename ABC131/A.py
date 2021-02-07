S = input()
was = ''
for c in S:
    if c == was:
        print('Bad')
        quit()
    was = c
print('Good')