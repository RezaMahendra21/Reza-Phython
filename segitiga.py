print('1')
a = 5
for i in range(0, a):
    for j in range(0, i + 1):
        print('* ' , end='')
    print('')

print('\n\n2')
a = 6
for i in range(0, a):
    for j in range(0, a - 1):
        print('* ' , end='')
    a -= 1
    print('')

print('\n\n3')
a = 5
s = 2 * a - 2 # for spaces
for i in range(0, a):
    for j in range(0, s):
        print(' ',end='')
    s -= 2
    for j in range(0, i + 1):
        print('* ', end='')
    print('')

print('\n\n4')
a = 5
s = 0 # for spaces
for i in range(0, a):
    for j in range(0, s):
        # print(j, end='')
        print(' ',end='')
    s += 2
    for j in range(0, a):
        print('* ' , end='')
    a -= 1
    print('')

print('\n\n5')
a = 5
s = a - 1 # for spaces
for i in range(0, a):
    for j in range(0, s):
        print(' ', end='')
    s -= 1
    for j in range(0, i + 1):
        print('* ', end='')

    print('')

print('\n\n6')
a = 5
s = 0 # for spaces
for i in range(0, a):
    for j in range(0, s):
        print(' ',end='')
    s += 1
    for j in range(0, a):
        print('* ' , end='')
    a -= 1
    print('')