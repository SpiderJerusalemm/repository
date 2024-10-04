import math

result = 0
n = int(input("input n in range 100:\n"))
if n >= 100:
    print("n in range 100!")
else:
    for i in range (n + 1):
        result += i**3
    print (f'finish sum = {result}')

p = int(input("rotate table - 0, usual table - 1:\n"))
if p == 1:
    for i in range (1, 10):
        for n in range (1, 10):
            if i * n < 10:
                print ((i * n), end = '  ')
            else:
                print ((i * n), end = ' ')
        print()
else:
    for i in range (9, 0, -1):
        for n in range (1, 10):
            if i * n < 10:
                print ((i * n), end = '  ')
            else:
                print ((i * n), end = ' ')
        print()


