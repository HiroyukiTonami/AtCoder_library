c = input()

if c.replace(c[0], '') == '':
    print('Won')
else:
    print('Lost')